<table class="table table-bordered">
  <thead>
    <tr>
      <th scope="col">JSON Event Data</th>
      <th scope="col">PDL Query</th>
      <th scope="col">Expected Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        ```json
        {
          "field1":{
            "subfield1":"subvalue1",
            "subfield2":"sub value2"
          },
          "field2":"value2",
          "field3":123
        }
        ```
      </td>
      <td class="align-middle">
      ```bash
      field1.subfield2 ?= "value2"
      ```
      </td>
      <td class="align-middle">
      ```python
      true
      ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```json
        {
          "field1":"value1",
          "field2":"value2 text2 value2",
          "field3":123,
          "field4":"value4",
          "field_5":5,
          "field-6":6,
          "field:7":7
        }
        ```
      </td>
      <td class="align-middle">
      ```bash
      field1="va*e1"
      ```
      </td>
      <td class="align-middle">
      ```
      true
      ```
      </td>
    </tr>
    <tr>
      <td class="align-middle">
        ```json
          {
            "field1":{
              "subfield1":"subvalue1",
              "subfield2":"sub value2"
            },
            "field2":"value2",
            "field3":123
          }
        ```
      </td>
      <td class="align-middle">
      ```bash
      (field1.subfield2 = "value2" AND field3=123)
      ```
      </td>
      <td class="align-middle">
      ```
      false
      ```
      </td>
    </tr>
  </tbody>
</table>