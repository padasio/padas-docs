#### Description
The `parse_csv` expression is used to properly parse the values of a specific CSV encoded field from the given eventdata.  Newly parsed fields are added to the event. Some example values that can be parsed:

- `value1, value2, value3`
- `value1, value2, 123` (Last one is parsed as Integer in JSON)
- `"value 1", "value 2", value 3` (Optional quoted values for Strings.)
- `"value 1"| "value 2"| value 3` (Using custom delimiters, e.g. `|`)

#### Syntax and Functions

```bash
... | parse_csv <fieldName> header=<headerValue> [delimiter=<delimiterValue>]
```

_Arguments_

- `fieldName`: Field name to parse.
- `headerValue`: Must be a comma separated String in quotes (e.g. `"myfield1, myfield2, myfield3"`).  Represents the header values to be used as new field names for the parsed CSV encoded data.
- `delimiterValue`: Must be a String in quotes (e.g. `";"`).  Delimiter value to use for CSV encoded data.  Default is `","`

#### Fields Examples
The following table provides examples of available functionality based on the following JSON value:

```json
{
  "field1":
    {
      "subfield1":"subvalue1",
      "subfield2":"sub value2"
    }, 
  "field2": "aaa; 123 ; ccc", 
  "field3": 123,
  "field4": "xxx, 456 , yyy"
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
          parse_csv field2 header="csvField1, csvField2, csvField3" delimiter=";"
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":
              {
                "subfield1":"subvalue1",
                "subfield2":"sub value2"
              }, 
            "field2": "aaa; 123 ; ccc", 
            "field3": 123,
            "field4": "xxx, 456 , yyy",
            "csvField1": "aaa",
            "csvField2": 123,
            "csvField3": "ccc"
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```bash
          parse_csv field4 header="csvField1, csvField2, csvField3" 
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":
              {
                "subfield1":"subvalue1",
                "subfield2":"sub value2"
              }, 
            "field2": "aaa; 123 ; ccc", 
            "field3": 123,
            "field4": "xxx, 456 , yyy",
            "csvField1": "xxx",
            "csvField2": 456,
            "csvField3": "yyy"
          }
        ```
      </td>
    </tr>
  </tbody>
  </table>