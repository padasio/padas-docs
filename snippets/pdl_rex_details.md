#### Description
This command is used to extract fields using regular expression named groups from a given field in the event data.

#### Syntax and Operators

```bash
... | rex <fieldName> "<regex>"
```

_Arguments_

- `fieldName`: It refers to the field name where the regular expression will be applied to.
- `regex`: This is the named capturing group regular expression, in quotes, to extract new fields.  


#### Rex Examples
The following table provides examples of available functionality based on the following event data:

```json
{
  "field1": {
    "subfield1":"subvalue1",
    "subfield2":"sub value2"
    }, 
    "field2": "value2", 
    "field3": 123
}
```

<table>
  <thead>
    <tr>
      <th scope="col">Expression</th>
      <th scope="col">Expected Output</th>
      <th scope="col">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        ```bash
          rex field2 "(?<field2Text>\w+)(?<field2Number>\d+)"
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1": {
              "subfield1":"subvalue1",
              "subfield2":"sub value2"
            }, 
            "field2": "value2", 
            "field3": 123,
            "field2Text": "value",
            "field2Number": 2
          }
        ```
      </td>
      <td> Regular expression is applied to <code>field1</code> value, which is <code>"value2"</code>.  The regular expression separates text with ending number and puts them in 2 different fields (namely <code>field2Text</code> and <code>field2Number</code>).
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```bash
          rex field1.subfield2 "\w+\s(?<field1subfield3>\w+)"
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1": {
              "subfield1":"subvalue1",
              "subfield2":"sub value2"
            }, 
            "field2": "value2", 
            "field3": 123,
            "field1subfield3": "value2"
          }
        ```
      </td>
      <td>Regular expression is applied to <code>field1.subfield2</code> nested field value, which is <code>"sub value2"</code>.  The regular expression skips the first word including the following space character and captures the remaining word as <code>field1subfield3</code>.
      </td>
    </tr>
  </tbody>
  </table>