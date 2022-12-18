
Description of fields can be found below.

| Field       | Description                                           | 
| -------     | ----------------------------------------------------- | 
| ID          | Unique identifier.  This ID is also used as a key when updating/deleting the entry. |
| Name        | A descriptive name.                                   |
| Description | Detailed description of the task functionality.       |
| Function    | One of the built-in functions for this task.        |
| Definition  | Function definition.  Each function has different definition parameters.  Please see below for details. |

##### `FILTER` Function Definition

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Type        | Must be `pdl` or `regex`.  Defines the type of filgering. | <img src="../assets/img/padas_ui_task_filter_example.png" class="img-fluid py-5 w-75"> {: rowspan=3} |
| Value       | Depending on the Type, this must be a PDL query or a Regular Expression to match the event.| &#8288 {: style="padding:0"} | 
| Action      | When the query/regex matches, this action processed on the event.  Must be `keep` or `drop`.| &#8288 {: style="padding:0"} |


##### `EXTRACT` Function Definition

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Regex       | Named group capturing Regular Expression to match the event.  Captured named groups will be JSON field names. | <img src="../assets/img/padas_ui_task_extract_example.png" class="img-fluid py-5 w-75"> {: rowspan=3} |
| Keep Raw    | Boolean to keep raw data in a separate field.  If set to `true` a field name should be provided.| &#8288 {: style="padding:0"} | 
| Raw Field Name | If raw data is to be kept, this will be the field to store it in. `_raw` is the default.| &#8288 {: style="padding:0"} |
