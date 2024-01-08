#### Description
The eval expression is used to modify or compute one or more fields in the data (separated by comma `,` character).  The expression must start with `eval` keyword.

#### Syntax and Functions
Eval expression requires the `eval` keyword followed by a field name and an assignment with `=` character.  Right side of the assignment can be an `if` function or a calculated field value using literals (string, number) or field names.
```bash
... | eval <fieldName>=<ifFunction>
... | eval <fieldName>=<fieldValue> <arithmeticFunction> <fieldValue>
```

The following list provides available evaluation expression functionality and operators:

<table>
  <thead>
    <tr>
      <th scope="col">Supported Function and Syntax</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        ```
          if(<query>, <true evaluationExpression> , <false evaluationExpression>)
        ```
      </td>
      <td class="align-middle">
        If <code>&lt;query&gt;</code> expression matches the event (see <a href="/pdl-reference#query">query</a> for details), returns the value of <code>&lt;true evaluationExpression&gt;</code>, otherwise the function returns the <code>&lt;false evaluationExpression</code>&gt;.
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```
          <fieldValue> <evaluationOperator> <fieldValue>
        ```
      </td>
      <td class="align-middle">
        Where <code>&lt;fieldValue&gt;</code> can be a String or Number literal as well as a field name from JSON even data.  The following are the list of supported <code>&lt;evaluationOperator&gt;</code> values:
        <br/>
        <ul>
          <li><code>+</code>: Addition for numbers and concatenation for string values.</li>
          <li><code>-</code>: Substraction for number fields only.</li>
          <li><code>*</code>: Multiplication for number fields only.</li>
          <li><code>/</code>: Division for number fields only.</li>
        </ul>
      </td>
    </tr>
  </tbody>
  </table>

#### Eval Examples
The following table provides examples of available functionality based on the following JSON value:

```json
{
  "field1":"value1",
  "field2":123
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
        ```
          eval myfield=field2 - 3
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":"value1",
            "field2":123,
            "myfield":120
          }
        ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```
          eval myfield=if(field2 < 150, field1 + "xyz", "N/A"), mytag="sometag"
        ```
      </td>
      <td class="align-middle">
        ```json
          {
            "field1":"value1",
            "field2":123,
            "myfield":"value1xyz",
            "mytag":"sometag"
          }
        ```
      </td>
    </tr>
  </tbody>
  </table>