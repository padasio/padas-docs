<table>
  <thead>
    <tr>
      <th scope="col">JSON Event Data</th>
      <th scope="col">PDL Expression</th>
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
      ```js
        null
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
              "field3":123,
              "field4": [5, 6, 7]
            }

        ```
      </td>
      <td class="align-middle">
      ```bash
        (field1.subfield2 ?= "value2" AND field3=123) 
        | eval newField=field3+100
        | eval anotherField=if(newField > 300, "above 300", "below 300")
      ```
      </td>
      <td class="align-middle">
      ```json
        {
          "field1": {
            "subfield1": "subvalue1",
            "subfield2": "sub value2"
          },
          "field2": "value2",
          "field3": 123,
          "field4": [
            5,
            6,
            7
          ],
          "newField": 223,
          "anotherField": "below 300"
        }
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
              "field3":123,
              "field4": [5, 6, 7]
            }

        ```
      </td>
      <td class="align-middle">
      ```bash
        field2 IN ["value1", "value2"] AND field4 ?= 6
        | eval newField=field3+100
        | fields keep field1, newField
        | rename field1.subfield1 AS myField
      ```
      </td>
      <td class="align-middle">
      ```json
        {
          "field1": {
            "subfield2": "sub value2"
          },
          "newField": 223,
          "myField": "subvalue1"
        }
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
              "field3":123,
              "field4": [5, 6, 7]
            }

        ```
      </td>
      <td class="align-middle">
      ```bash
        field2 ?= "value"
        | fields remove field2
        | flatten
      ```
      </td>
      <td class="align-middle">
      ```json
        {
          "field1_subfield1": "subvalue1",
          "field1_subfield2": "sub value2",
          "field3": 123,
          "field4_0": 5,
          "field4_1": 6,
          "field4_2": 7
        }
      ```
      </td>
    </tr>
  </tbody>
</table>