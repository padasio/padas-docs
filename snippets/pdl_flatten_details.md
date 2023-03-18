#### Description
The flatten expression is used to flatten nested JSON event data. 

#### Syntax and Operators
This expression does not have any functions/operators and expects JSON input.

```bash
... | flatten
```


#### Flatten Examples
The following table provides examples of available functionality with sample JSON value:

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
          {
            "field1":"value1",
            "field2":123,
            "field3": [4, 5, 6]
          }
        ```
      </td>
      <td class="align-middle">
        ```bash
          | flatten
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":"value1",
            "field2":123,
            "field3": [4, 5, 6]
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```json
          {
            "field1":"value1",
            "field2":123,
            "field3": {
              "subfield1": 456,
              "subfield2": "value2"
            }
          }
        ```
      </td>
      <td class="align-middle">
        ```bash
          | flatten
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":"value1",
            "field2":123,
            "field3_subfield1": 456,
            "field3_subfield2": "value2"
          }
        ```
      </td>
    </tr>
  </tbody>
  </table>