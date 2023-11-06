#### Description
Counts events occurring in the given time frame and stores the result in `padasAggregation.eventCount` field.  The result may also contain count of events for each group specified by `group_by` separately.

#### Syntax and Functions

```bash
... | event_count <timespan-param> <group-by-clause> <where-clause>
```

#### Event Count Examples
The following table provides examples of available functionality based on the following JSON value:

<table>
  <thead>
    <tr>
      <th scope="col">JSON Input</th>
      <th scope="col">Expression</th>
      <th scope="col">Expected Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        ```json
          {"field1":"value1", "field2":123}
          {"field1":"value1", "field2":124}
          {"field1":"value2", "field2":123}
          {"field1":"value2", "field2":123}
        ```
      </td>
      <td class="align-middle">
        ```bash
          event_count timespan=1m
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "padasRule":"myrule1",
            "padasAggregation": {
              "result":{},
              "eventCount":4
            }
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```json
          {"field1":"value1", "field2":123}
          {"field1":"value1", "field2":124}
          {"field1":"value2", "field2":123}
          {"field1":"value2", "field2":123}
        ```
      </td>
      <td class="align-middle">
        ```bash
          event_count timespan=5m group_by field1 where padasAggregation.eventCount > 1
        ```
      </td>
      <td class="align-middle">
        ```json
            {
              "padasRule": "myrule2",
              "padasAggregation": {
                "groupBy": {
                  "field1": "value1"
                },
                "result": {
                  "field1": {
                    "value1": 2
                  }
                },
                "eventCount": 2
              }
            }
      
            {
              "padasRule": "myrule2",
              "padasAggregation": {
                "groupBy": {
                  "field1": "value2"
                },
                "result": {
                  "field1": {
                    "value2": 2
                  }
                },
                "eventCount": 2
              }
            }
        ```
      </td>
    </tr>
  </tbody>
  </table>