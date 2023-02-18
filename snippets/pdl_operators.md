Below table provides examples based on the following JSON value:
```json
{
  "field1":"value1",
  "field2":"value2 text2 value2",
  "field3":123,
  "field4":["item1","item2","item3"]
}
```

| Operator/Keyword  | Description                                                           | Example (evaluates to `true`) |
| ----------------- | --------------------------------------------------------------------- | ----------------------------- |
| `NOT`             | Negates the result.                                                   | `NOT (field1 = "valueXXX")`   |
| `AND`             | Expects both sides of the expression to be `true`.                    | `field1="value1" AND field3=123` |
| `OR`              | Expects at least one side of the expression to be `true`.             | `field1="xyz" OR field3=123`  |
| `IN`              | Returns `true` if the field value exists within the provided array. Note that all array values must be one value type (either **String** or **Integer**). | `field3 IN [111, 222, 123, 444]` |
| `=`               | **Equals**, returns `true` if the value is an exact match.<br/>A single wildcard `*` is also accepted for string values. | `field1="value1"`<br/>`field1="val*"`<br/>`field1="*"` |
| `!=`              | **Not Equals**, returns `true` if the value does not match.           | `field3 != 456`  <br/>`field4 != ["other1","item3"]` |
| `?=`              | **Contains**, checks whether the string value contains the text.  For arrays, it checks for the array item. | `field2 ?= "text2"` <br/>`field4 ?= "item2"`           |
| `>`               | **Greater than**, returns `true` if query comparison value is greater than event field value. | `field3 > 100` |
| `<`               | **Less than**, returns `true` if query comparison value is less than event field value. | `field3 < 200` |
| `>=`              | **Greater than or equals**, returns `true` if query comparison value is greater than or equals to the event field value. | `field3 >= 123` |
| `<=`              | **Less than or equals**, returns `true` if query comparison value is less than or equals to the event field value. | `field3 <= 123 `|


