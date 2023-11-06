
<table>
  <thead>
    <tr>
      <th style="text-align: center;" scope="col">#</th>
      <th style="text-align: center;" scope="col">Simple Rule</th>
      <th style="text-align: center;" scope="col">PDL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        1
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file: 'example.exe'
            condition: selection
        ```
      </td>
      <td class="align-middle">
        ```json
        file="example.exe"
        ```
      </td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        2
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file: 'example.exe'
                eventId: 4769
            condition: selection
        ```
      </td>
      <td class="align-middle">
        ```json
        file="example.exe" AND eventId=4769
        ```
      </td>
    </tr>
  </tbody>
   <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        3
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file: 
                    - 'example.exe'
                    - 'example2.exe'
                eventId: 4769
            filter:
                user: 'someuser'
            condition: selection and not filter
        ```
      </td>
      <td class="align-middle">
        ```json
        ((file="example.exe" OR file="example2.exe") AND eventId=4769) AND NOT (user="someuser")
        ```
      </td>
    </tr>
  </tbody>   
   <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        4
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file: 
                    - 'example.exe'
                    - 'example2.exe'
                eventId: 4769
            filter:
                user: 'someuser'
                password: null
            condition: selection and not filter
        ```
      </td>
      <td class="align-middle">
        ```json
        ((file="example.exe" OR file="example2.exe") AND eventId=4769) AND NOT (user="someuser" AND password!="*")
        ```
      </td>
    </tr>
  </tbody>   
   <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        5
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file|endswith: 
                    - '\\example.exe'
                    - '\\example2.exe'
                eventId|gte: 4769
            filter:
                user|contains: 'someuser'
                password: null
            condition: selection and not filter
        ```
      </td>
      <td class="align-middle">
        ```json
        ((file="*\\example.exe" OR file="*\\example2.exe") AND eventId>=4769) AND NOT (user?="someuser" AND password!="*")
        ```
      </td>
    </tr>
  </tbody>   
   <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        6
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file|endswith: 
                    - '\\example.exe'
            selection2:
                file|endswith: 
                    - '\\example2.exe'
                eventId|gte: 4769
            filter:
                user|contains: 'someuser'
                password: null
            condition: 1 of selection* and not filter
        ```
      </td>
      <td class="align-middle">
        ```json
        ((file="*\\example.exe") OR (file="*\\example2.exe" AND eventId>=4769)) AND NOT (user?="someuser" AND password!="*")
        ```
      </td>
    </tr>
  </tbody>  
   <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        7
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file|endswith: 
                    - '\\example.exe'
            selection2:
                file|endswith: 
                    - '\\example2.exe'
                eventId|gte: 4769
            filter:
                user|contains: 'someuser'
                password: null
            condition: all of selection* and not filter
        ```
      </td>
      <td class="align-middle">
        ```json
        ((file="*\\example.exe") AND (file="*\\example2.exe" AND eventId>=4769)) AND NOT (user?="someuser" AND password!="*")
        ```
      </td>
    </tr>
  </tbody>
   <tbody>
    <tr>
      <td class="align-middle" style="text-align: center;">
        8
      </td>
      <td class="align-middle">
        ```yaml
        detection:
            selection:
                file|endswith|all: 
                    - '\\example.exe'
                    - '\\example2.exe'
                eventId|gte: 4769
            filter:
                user|contains: 'someuser'
                password: null
            condition: selection and not filter
        ```
      </td>
      <td class="align-middle">
        ```json
        ((file="*\\example.exe" AND file="*\\example2.exe") AND eventId>=4769) AND NOT (user?="someuser" AND password!="*")
        ```
      </td>
    </tr>
  </tbody>     
</table>