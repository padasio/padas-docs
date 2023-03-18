#### Description
The fields expression is used to keep or remove fields from the data. 

#### Syntax and Functions

```bash
... | fields <fieldsFunction> <fieldName>, ...
```

Supported functions are:

- `keep`: to keep the list of fields only
- `remove`: to remove the list of fields and keep the rest

#### Fields Examples
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
          fields remove field2, field3.subfield1
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":"value1",
            "field3": {
              "subfield2": "value2"
            }
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```bash
          fields keep field2, field3.subfield1
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field2":123,
            "field3": {
              "subfield1": 456
            }
          }
        ```
      </td>
    </tr>
  </tbody>
  </table>