
Description of fields can be found below.

| Field       | Description                                           | 
| -------     | ----------------------------------------------------- | 
| ID          | Unique identifier.  This ID is also used as a key when updating/deleting the entry. |
| Name        | A descriptive name.                                   |
| Description | Detailed description of the rule functionality.       |
| Data model  | Data model name where this rule is applicable to.  This is specified in a Task with `APPLY_RULES` function.<br/>Any arbitrary data model can be specified.  Please refer to [Datamodel Reference](datamodel-reference.md) for more generic types and conventions. |
| PDL         | PDL query to match the streaming data.  Please refer to [PDL Reference](../pdl-reference.md) for details.<br/>Sample rules can also be found as [PadasRules_sample.json](../assets/config/PadasRules_sample.json) |
| Annotations | List of applicable annotations for this rule.<br/>For example, a common usage would be adding MITRE ATT&CK Technique IDs. |
| Enabled     | Set to `true` when enabled, `false` otherwise.        |
