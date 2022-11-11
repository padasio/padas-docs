<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Event <code>jsondata</code> value</th>
      <th scope="col">PDL Query</th>
      <th scope="col">Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <pre>
        {
          "field1":{
            "subfield1":"subvalue1",
            "subfield2":"sub value2"
          },
          "field2":"value2",
          "field3":123
        }
        </pre>
      </td>
      <td><code>field1.subfield2 ?= "value2"</code></td>
      <td><code>true</code></td>
    </tr>
    <tr>
      <td>
        <pre>
        {
          "field1":"value1",
          "field2":"value2 text2 value2",
          "field3":123,
          "field4":"value4",
          "field_5":5,
          "field-6":6,
          "field:7":7
        }
        </pre
      ></td>
      <td><code>field1="va*e1"</code></td>
      <td><code>true</code></td>
    </tr>
    <tr>
      <td>
        <pre>
          {
            "field1":{
              "subfield1":"subvalue1",
              "subfield2":"sub value2"
            },
            "field2":"value2",
            "field3":123
          }
        </pre>
      </td>
      <td><code>(field1.subfield2 = "value2" AND field3=123)</code></td>
      <td><code>false</code></td>
    </tr>
  </tbody>
</table>