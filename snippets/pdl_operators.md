Below table provides examples based on the following JSON value:
<pre>
{
  "field1":"value1",
  "field2":"value2 text2 value2",
  "field3":123
}

</pre>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Operator/Keyword</th>
      <th scope="col">Description</th>
      <th scope="col">Example (<code>true</code>)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>NOT</code></td>
      <td>NOT, negates the result</td>
      <td><code>NOT (field1 = "valueXXX")</code></td>
    </tr>
    <tr>
      <td><code>AND</code></td>
      <td>AND, expects both sides to be <code>true</code></td>
      <td><code>field1="value1" AND field3=123</code></td>
    </tr>
    <tr>
      <td><code>OR</code></td>
      <td>OR, expects at least one side to be <code>true</code></td>
      <td><code>field1="xyz" OR field3=123</code></td>
    </tr>
    <tr>
      <td><code>=</code></td>
      <td>Equals, returns <code>true</code> if the value is an exact match.  <br />A single wildcard <code>*</code> is also accepted for string values.</td>
      <td><code>field1="value1"</code><br /><code>field1="val*"</code></td>
    </tr>
    <tr>
      <td><code>!=</code></td>
      <td>Not Equals, returns <code>true</code> if the value does not match</td>
      <td><code>field3 != 456</code></td>
    </tr>
    <tr>
      <td><code>?=</code></td>
      <td>Contains, checks whether the string value contains the query</td>
      <td><code>field2 ?= "text2"</code></td>
    </tr>
    <tr>
      <td><code>&gt;</code></td>
      <td>Greater than, returns <code>true</code> if query comparison value is greater than event field value</td>
      <td><code>field3 > 100</code></td>
    </tr>
    <tr>
      <td><code>&lt;</code></td>
      <td>Less than, returns <code>true</code> if query comparison value is less than event field value</td>
      <td><code>field3 < 200</code></td>
    </tr>
    <tr>
      <td><code>&gt;=</code></td>
      <td>Greater than or equals, returns <code>true</code> if query comparison value is greater than or equals to the event field value</td>
      <td><code>field3 >= 123</code></td>
    </tr>
    <tr>
      <td><code>&lt;=</code></td>
      <td>Less than or equals, returns <code>true</code> if query comparison value is less than or equals to the event field value</td>
      <td><code>field3 <= 123</code></td>
    </tr>
  </tbody>
</table>