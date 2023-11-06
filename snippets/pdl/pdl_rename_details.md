#### Description
The rename expression is used to rename one or more fields in the data. This command is useful for giving fields more meaningful names, such as "processId" instead of "pid".

#### Syntax and Operators

```bash
... | rename <fieldName> AS <fieldName>
```

_Operators_

- `AS`: This operator is used to define the new name of the field.


#### Rename Examples
The following table provides examples of available functionality based on the following JSON value:

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

<table>
  <thead>
    <tr>
      <th scope="col">Expression</th>
      <th scope="col">Expected Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        ```bash
          rename field1 AS myField
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "myField":"value1",
            "field2":123,
            "field3": {
              "subfield1": 456,
              "subfield2": "value2"
            }
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```bash
          rename field2 AS myField2, field3.subfield1 AS mySubfield
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":"value1",
            "myField2":123,
            "mySubfield": 456,
            "field3": {
              "subfield2": "value2"
            }
          }
        ```
      </td>
    </tr>
  </tbody>
  </table>