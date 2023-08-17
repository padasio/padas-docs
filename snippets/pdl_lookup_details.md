#### Description
The lookup expression is used to enrich event data. When an event is processed, the lookup expression is used to perform a match in the lookup table, based on a specified field. Once a match is found, relevant information from the lookup table is retrieved and added to the event data.

#### Syntax and Operators

```bash
... | lookup <lookup_id> <lookup_fieldName> OUTPUT <lookup_dest_fieldName>
```

_Arguments_

- `lookup_id`: It refers to the lookup name.
- `lookup_fieldName`: It refers to the field in the lookup table used for matching against the events.  
- `lookup_dest_fieldName`: Specifies a field in the lookup table that will be copied into the events.


_Operators_

- `AS`: This operator is used to define the new name of the field.


#### Lookup Examples
The following table provides examples of available functionality based on the following event data and lookup example:

Lookup Example:
```json
{
        "id": "windows_signatures_substatus",
        "content": [
            {
                "signature_id": 4625,
                "Sub_Status": "0xc0000064",
                "signature": "User name does not exist"
            },
            {
                "signature_id": 4625,
                "Sub_Status": "0xC0000064",
                "signature": "User name does not exist"
            },
            {
                "signature_id": 4625,
                "Sub_Status": "0xc000006a",
                "signature": "User name is correct but the password is wrong"
            }
        ]
    }
```

Event Data Example:
```json
{
  "EventTime": "2017/08/25 14:09:12",
  "Hostname": "CIVDCS-ADC1.changeme.com",
  "EventID": 4625,
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "Message": "An account failed to log on.",
  "Category": "Logon",
  "SubjectLogonId": "0x0",
  "TargetUserSid": "S-1-0-0",
  "TargetUserName": "MININT-UP26I95$",
  "TargetDomainName": "changeme",
  "Status": "0xc000006d",
  "FailureReason": "%%2313",
  "Sub_Status": "0xc000006a",
  "LogonType": "3",
  "IpAddress": "172.23.130.64"
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
          lookup windows_signatures_substatus Sub_Status OUTPUT signature
        ```
      </td>
      <td class="align-middle">
        ```json
				{
				  "EventTime": "2017/08/25 14:09:12",
				  "Hostname": "CIVDCS-ADC1.changeme.com",
				  "EventID": 4625,
				  "SourceName": "Microsoft-Windows-Security-Auditing",
				  "Message": "An account failed to log on.",
				  "Category": "Logon",
				  "SubjectLogonId": "0x0",
				  "TargetUserSid": "S-1-0-0",
				  "TargetUserName": "MININT-UP26I95$",
				  "TargetDomainName": "changeme",
				  "Status": "0xc000006d",
				  "FailureReason": "%%2313",
				  "Sub_Status": "0xc000006a",
				  "LogonType": "3",
				  "IpAddress": "172.23.130.64",
				  "signature": "User name is correct but the password is wrong"
				}
        ```
      </td>
    </tr>
  </tbody>
  </table>
