#### Description
The `parse_kv` expression is used to properly parse the values of a specific Key-Value encoded field from the given eventdata.  Newly parsed fields are added to the event. Some example values that can be parsed:

- `key1=value1 key2=value2 key3=value3`
- `key1=value1 key2 = value2 key3= 123` (Last one is parsed as Integer in JSON)
- `key1=value1 key2="value2" key3=value3` (Optional quoted values for Strings.)
- `key1:value1 key2 :value2 key3:value3` (Using custom delimiters, e.g. `:`)

#### Syntax and Functions

```bash
... | parse_kv <fieldName> [delimiter=<delimiterValue>]
```

Arguments:

- `fieldName`: Field name to parse.
- `delimiterValue`: Must be a String in quotes (e.g. `":"`).  Delimiter value to use for KV encoded data.  Default is `"="`

#### Fields Examples
The following table provides examples of available functionality based on the following JSON value:

```json
{
  "field1":
    {
      "subfield1":"subvalue1",
      "subfield2":"sub value2"
    }, 
  "field2": "kvField1=aaa kvField2=123 kvField3=ccc", 
  "field3": 123,
  "field4": "kvField1 : xxx kvField2: 456 kvField3:\"yyy\"",
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
          parse_csv field2
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
            "field2": "kvField1=aaa kvField2=123 kvField3=ccc", 
            "field3": 123,
            "field4": "kvField1 : xxx kvField2: 456 kvField3:\"yyy\"",
            "kvField1": "aaa",
            "kvField2": 123,
            "kvField3": "ccc"
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```bash
          parse_kv field4 delimiter=":"
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
            "field2": "kvField1=aaa kvField2=123 kvField3=ccc", 
            "field3": 123,
            "field4": "kvField1 : xxx kvField2: 456 kvField3:\"yyy\"",
            "kvField1": "xxx",
            "kvField2": 456,
            "kvField3": "yyy"
          }
        ```
      </td>
    </tr>
  </tbody>
  </table>