
Sigma Meta Rule with `action: correlation` fields are converted only.  The following table provides information on Sigma Meta Rule functions and their corresponding [PDL correlation](pdl-correlation.md).

| Sigma Meta Rule Function | PDL Correlation Usage | 
| ------------------------ | --------------------- |
| `event_count`            | `| event_count <condition>` | 
| `value_count`            | `| value_count(<fieldname>) <condition>` |
| `temporal`               | `| temporal(<fieldname>, [<value>,<value>, ...], ordered_boolean)` |



The following table provides some examples on Sigma Meta Rule to PDL Expression/Correlation conversions.
<table>
  <thead>
    <tr>
      <th style="text-align: center;" scope="col">#</th>
      <th style="text-align: center;" scope="col">Meta Rule</th>
      <th style="text-align: center;" scope="col">PDL Expression/Correlation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        1
      </td>
      <td class="align-middle">
        ```yaml
        title: Event Count
        id: "0e00016d"
        action: correlation
        type: event_count
        rules:
            - 5638f7c0-ac70-491d-8465-2a65075e0d86
            - 5638f7c0-ac70-491d-8465-2a65075e0d87
        group-by:
            - ComputerName
        timespan: 1h
        condition:
            range: 100..200
        ```
      </td>
      <td class="align-middle">
        ```json
            "id": "0e00016d",
            "name": "Event Count",
            "description":"",
            "datamodel":"padas_alert",
            "annotations": [""],
            "pdl": "padas_rule IN [\"5638f7c0-ac70-491d-8465-2a65075e0d86\", \"5638f7c0-ac70-491d-8465-2a65075e0d87\"] 
                    | event_count timespan=1h group_by ComputerName where padasAggregation.eventCount>=100 AND padasAggregation.eventCount<=200",
            "enabled": false

                
        ```
      </td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        2
      </td>
      <td class="align-middle">
        ```yaml
        title: Value Count
        id: "0e00017d"
        action: correlation
        type: value_count
        field: User
        group-by:
            - ComputerName
            - WorkstationName
        timespan: 1d
        condition:
            gte: 100
        ```
      </td>
      <td class="align-middle">
        ```json
            "id": "0e00017d",
            "name": "Value Count",
            "description":"",
            "datamodel":"padas_alert",
            "annotations": [""],
            "pdl": "value_count(User) timespan=1d group_by ComputerName, WorkstationName where padasAggregation.valueCount>= 100",
            "enabled": false
        ```
      </td>
    </tr>
  </tbody>   
   <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        3
      </td>
      <td class="align-middle">
        ```yaml
        title: internal_error
        id: "0e00018d"
        name: select01
        detection:
          selection:
            http.response.status_code: 500
          condition: selection
        ---
        title: new_network_connection
        id: "0e00019d"
        name: select02
        detection:
          selection:
            event.category: network
            event.type: connection
            event.outcome: success
          condition: selection
        ---
        title: Temporal
        id: "0e00020d"
        action: correlation
        type: temporal
        rule:
          - select01
          - select02
        group-by:
          - internal_ip
          - remote_ip
        timespan: 10s
        ordered: true
        aliases:
          internal_ip:
            internal_error: destination.ip
            new_network_connection: source.ip
          remote_ip:
            internal_error: source.ip
            new_network_connection: destination.ip
        ```
      </td>
      <td class="align-middle">
        ```json
             {
              {
                    "id": "0e00018d",
                    "name": "select01",
                    "description":"",
                    "datamodel":"",
                    "annotations": [""],
                    "pdl": "http.response.status_code=500",
                    "enabled": false
                },
                {
                    "id": "0e00019d",
                    "name": "select02",
                    "description":"",
                    "datamodel":"",
                    "annotations": [""],
                    "pdl": "((event.category=\"network\") AND (event.type=\"connection\") AND (event.outcome=\"success\"))",
                    "enabled": false
                },
                {
                    "id": "0e00020d",
                    "name": "Temporal",
                    "description":"",
                    "datamodel":"padas_alert",
                    "annotations": [""],
                    "pdl": "eval internal_ip=if(padas_rule=\"internal_error\", destination.ip, if(padas_rule=\"new_network_connection\", source.ip, \"\")) 
                        | eval remote_ip=if(padas_rule=\"internal_error\", source.ip, if(padas_rule=\"new_network_connection\", destination.ip, \"\")) 
                        | temporal(ordered=true) [padasRule=\"select01\" || padasRule=\"select02\"] timespan=10s group_by internal_ip, remote_ip",
                    "enabled": false
                }
            }
        ```
      </td>
    </tr>
  </tbody>      
</table>