#### Description
Counts number of distinct values in a field defined by `fieldName` and stores the result in `padasAggregation.valueCount` field.  The result may also contain count of events for each group specified by `group_by` separately.

#### Syntax and Functions

```bash
... | value_count(<fieldName>) <timespan-param> <group-by-clause> <where-clause>
```

_Field Name parameter_:
This is the field name where count of distinct values are calculated.

#### Value Count Examples
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
          {"field1":"value2", "field2":123}
        ```
      </td>
      <td class="align-middle">
        ```bash
          value_count(field1) timespan=60s
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "padasRule": "myrule6",
            "padasAggregation": {
              "field": "field1",
              "valueCount": 2,
              "result": {
                "field1": {
                  "value1": 2,
                  "value2": 3
                }
              },
              "eventCount": 5
            }
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```json
          {"field1":"value1", "field2":123}
          {"field1":"value1", "field2":123}
          {"field1":"value2", "field2":123}
          {"field1":"value2", "field2":123}
          {"field1":"value3", "field2":123}
        ```
      </td>
      <td class="align-middle">
        ```bash
          value_count(field1) timespan=60s  group_by field2
        ```
      </td>
      <td class="align-middle">
        ```json
            {
              "padasRule": "myrule2",
              "padasAggregation": {
                "groupBy": {
                  "field2": 123
                },
                "field": "field1",
                "valueCount": 3,
                "result": {
                  "field1": {
                    "value1": 2,
                    "value2": 2,
                    "value3": 1
                  }
                },
                "eventCount": 5
              }
            }
        ```
      </td>
    </tr>
    </tbody>
  </table>