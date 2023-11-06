#### Description
Temporal correlation statement checks for all the events matching the expression array within the time frame defined.  If the boolean value `ordered` is set to `true`, then all the events are expected to occur in the given order.  The result may also contain count of events for each group specified by `group_by` separately.

#### Syntax and Functions

```bash
... | temporal(<ordered-param>) [ <expression> || <expression> || ... ] <timespan-param> <group-by-clause> <where-clause>
```

_Ordered parameter_: `order` is assigned either `true` or `false` as value (e.g. `ordered=true`) to specify whether the events are expected to match expression array order.
_Expression array_: The array consists of one or more expressions separated by double-pipe `||` character (e.g. `[ field1="valu*" || field3 < 100 AND field4=false>]`)

#### Temporal Examples
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
          {"field1":"value1", "field2":99}
          {"field1":"value1", "field2":124}
          {"field1":"value2", "field2":123}
          {"field1":"value2", "field2":125}
        ```
      </td>
      <td class="align-middle">
        ```bash
          temporal [ field1?="value" || field2 < 100 ] timespan=2m
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "padasRule": "myrule8",
            "padasTemporal": {
              "result": {
                "field1?=\"value\"": [
                  {
                    "field1": "value1",
                    "field2": 99
                  },
                  {
                    "field1": "value1",
                    "field2": 124
                  },
                  {
                    "field1": "value2",
                    "field2": 123
                  },
                  {
                    "field1": "value2",
                    "field2": 125
                  },
                ],
                "field2<100": [
                  {
                    "field1": "value1",
                    "field2": 99
                  }
                ]
              }
            }
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```json
          {"field1":"sometext", "field2":90}
          {"field1":"value1", "field2":124}
          {"field1":"value2", "field2":95}
          {"field1":"value2", "field2":123}
        ```
      </td>
      <td class="align-middle">
        ```bash
          temporal(ordered=true) [ field1?="value" || field2 < 100 ] timespan=2m group_by field2
        ```
      </td>
      <td class="align-middle">
        ```json
            {
              "padasRule": "myrule9",
              "padasTemporal": {
                "groupBy": {
                  "field2": 95
                },
                "result": {
                  "field2<100": [
                    {
                      "field1": "value2",
                      "field2": 95
                    }
                  ],
                  "field1?=\"value\"": [
                    {
                      "field1": "value2",
                      "field2": 95
                    }
                  ]
                }
              }
            }
        ```
      </td>
    </tr>
    </tbody>
  </table>