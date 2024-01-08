
Description of fields can be found below.

| Field       | Description                                           | 
| -------     | ----------------------------------------------------- | 
| ID          | Unique identifier.  This ID is also used as a key when updating/deleting the entry. |
| Name        | A descriptive name.                                   |
| Description | Detailed description of topology functionality.       |
| Group       | Consumer group associated with this topology.         | 
| Input       | Input topic to consume and apply configured pipeline(s). |
| Output      | One or more output topics to send transformed data to.|
| Enabled     | Set to `true` when enabled, `false` otherwise.        |
| Pipelines   | An ordered list of Pipelines to execute when streaming data from specified Input.<br/>When multiple Pipelines are specified, output from a Pipeline becomes an input for the next Pipeline. |
