
`action: correlation` is the unique key-value pair that indicates if it is Meta Rule. `type`, `fieled`, `group-by`, `timespan`, `condition`, `ordered`, `aliases` fields are used in this process.

Which function (`event_count`, `value_count`, `temporal`) will be used, is indicacted from `type` field by conversion `sigma_v2_to_padas.py` script. Functions meanings are same as in the Sigma rules. Detailed information can be found in below table.
<table>
  <thead>
    <tr>
      <th style="text-align: center;" scope="col">Function</th>
      <th style="text-align: center;" scope="col">Meaning</th>
        <th style="text-align: center;" scope="col">Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        ```
          event_count
        ```
      </td>
      <td class="align-middle">
        Counts events with conditions.
      </td>
     <td class="align-middle">
        ````
        | event_count <condition>
        ````
      </td>
    </tr>
  </tbody>  
    <tbody>
    <tr>
      <td class="align-middle">
        ```
          value_count
        ```
      </td>
      <td class="align-middle">
        Counts a specific field with conditions.
      </td>
     <td class="align-middle">
        ````
        | value_count(<fieldname>) <condition>
        ````
      </td>
    </tr>
  </tbody>
      <tbody>
    <tr>
      <td class="align-middle">
        ```
          temporal
        ```
      </td>
      <td class="align-middle">
        Counts events in specific conditions.
      </td>
     <td class="align-middle">
        ````
        | temporal(<fieldname>, [<value>,<value>, ...], ordered_boolean)
        ````
      </td>
    </tr>
  </tbody>
</table>  

The `field` field is appeared only with `value_count` function in the rule. It keeps the `<fieldname>` for `value_count`function. On the other hand `group-by`, `timespan`, `condition`, `ordered`, `aliases` fields can be found with all `type` Meta rules. PDL can be written with information about which fields will be grouped (`group-by`), under what conditions (`condition`), how long the events will be received (`timespan`), whether there will be a temporal ordering (`ordered`), and the matching status of the fields (`aliases`). You can see some examples without modifiers in the below table. 


<table>
  <thead>
    <tr>
      <th style="text-align: center;" scope="col">#</th>
      <th style="text-align: center;" scope="col">Meta Rule</th>
      <th style="text-align: center;" scope="col">Padas Rule</th>
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
            "pdl": "padas_rule IN [\"5638f7c0-ac70-491d-8465-2a65075e0d86\", \"5638f7c0-ac70-491d-8465-2a65075e0d87\"] | event_count timespan=1h group_by ComputerName where _count>=100 AND _count<=200",
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
            "pdl": "value_count(User) timespan=1d group_by ComputerName, WorkstationName where _count>= 100",
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
                    "pdl": "eval internal_ip=if(padas_rule=\"internal_error\", destination.ip, if(padas_rule=\"new_network_connection\", source.ip, \"\")) | eval remote_ip=if(padas_rule=\"internal_error\", source.ip, if(padas_rule=\"new_network_connection\", destination.ip, \"\")) | temporal(ordered=true) [padasRule=\"select01\" || padasRule=\"select02\"] timespan=10s group_by internal_ip, remote_ip",
                    "enabled": false
                }
            }
        ```
      </td>
    </tr>
  </tbody>      
</table>