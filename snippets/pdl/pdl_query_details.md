#### Description
The query expression is used to filter data based on a specified condition. If the query matches (evaluates to `true`), then the event data is returned. 

#### Syntax and Operators
Query syntax consists of field name and value comparisons that may include boolean operators and grouping with paranthesis.  Note that all operators are case sensitive.

Following are supported syntax for query expression:

- `NOT <query>`
- `<query> AND|OR <query>`
- `<fieldName> <comparisonOperator> <fieldvalue>`

_Comparison Operators_

- `IN`: Returns `true` if the field value exists within the provided array. Note that all array values must be one value type (either **String** or **Integer**).
- `=`: **Equals**, returns `true` if the value is an exact match. A single wildcard `*` is also accepted for string values. 
- `!=`: **Not Equals**, returns `true` if the value does not match.
- `?=`: **Contains**, checks whether the string value contains the text.  For arrays, it checks for the array item.
- `~=`: **Regex**, checks whether the string value matches the given Regular Expression.
- `>`: **Greater than**, returns `true` if query comparison value is greater than event field value. 
- `<`: **Less than**, returns `true` if query comparison value is less than event field value.
- `>=`: **Greater than or equals**, returns `true` if query comparison value is greater than or equals to the event field value.
- `<=`: **Less than or equals**, returns `true` if query comparison value is less than or equals to the event field value.

_Boolean Operators_

- `NOT`: Negates the result of following (grouped) query
- `AND`: Expects both sides of the expression to be `true`. 
- `OR`: Expects at least one side of the expression to be `true`. 

#### Supported JSON Data Types
PDL comparisons work on **String**, **Number**, **Boolean**, and **Array** JSON value data types.  **String** comparisons MUST be defined in quotes `"` within PDL query definition.  **Array** comparisons are limited to **Equals** (`=`), **Not Equals** (`!=`), and **Contains** (`?=`) operators.

Examples:

- PDL query with `field1="123"` will compare `"123"` as a **String** JSON data type.
- PDL query with `field2=123` will compare `123` as a **Number** JSON data type.
- PDL query with `field3=true` will compare `true` as an **Boolean** JSON data type.
- PDL query with `field4=[5,6,7]` will compare `[5,6,7]` as an **Array** JSON data type and expect `field4` to be an array as well.

#### Wildcard Support
PDL supports a single wildcard `*` with Equals operator (`=`) for **String** JSON values.  Following are valid PDL query examples with wildcard usage:

```
field1="val*1"
field1="val*"
field1="*ue1"
field1="*"
```

#### Grouped arguments
Sometimes the syntax must display arguments as a group to show that the set of arguments are used together. Parenthesis `( )` are used to group arguments.

For example in this syntax:
`(field1="val1" OR field2=123) AND field3="value3"`

The grouped argument is `(field1="val1" OR field2=123)` and its results are evaluated as a whole.


#### Query Examples
The following table provides descriptions and examples of available operators based on the following JSON value:

```json
{
  "field1":"value1",
  "field2":"value2 text2 value2",
  "field3":123,
  "field4":["item1","item2","item3"]
}
```

| Operator/Keyword  | Example (evaluates to `true`) |
| ----------------- | ----------------------------- |
| `NOT`             | `NOT (field1 = "valueXXX")`   |
| `AND`             | `field1="value1" AND field3=123` |
| `OR`              | `field1="xyz" OR field3=123`  |
| `IN`              | `field3 IN [111, 222, 123, 444]` |
| `=`               | `field1="value1"`<br/>`field1="val*"`<br/>`field1="*"` |
| `!=`              | `field3 != 456`  <br/>`field4 != ["other1","item3"]` |
| `?=`              | `field2 ?= "text2"` <br/>`field4 ?= "item2"`           |
| `~=`              | `field2 ~= "\stext"` <br/>`field4 ~= "\d\stext\d\s"`           |
| `>`               | `field3 > 100` |
| `<`               | `field3 < 200` |
| `>=`              | `field3 >= 123` |
| `<=`              | `field3 <= 123 `|

