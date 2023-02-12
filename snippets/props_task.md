
Description of fields can be found below.

| Field       | Description                                           | 
| -------     | ----------------------------------------------------- | 
| ID          | Unique identifier.  This ID is also used as a key when updating/deleting the entry. |
| Name        | A descriptive name.                                   |
| Description | Detailed description of the task functionality.       |
| Function    | One of the built-in functions for this task.        |
| Definition  | Function definition.  Each function has different definition parameters.  Please see below for details. |

##### `FILTER` Definition
This function allows filtering (keep or drop) an event if it matches the specified regular expression (`regex`) or PDL query (`pdl`).  Event is not transformed and kept the same.

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Type        | Must be `pdl` or `regex`.  Defines the type of filgering. | <img src="../assets/img/padas_ui_task_filter_example.png" class="img-fluid py-5 w-75"> {: rowspan=3} |
| Value       | Depending on the Type, this must be a PDL query or a Regular Expression to match the event.| &#8288 {: style="padding:0"} | 
| Action      | When the query/regex matches, this action processed on the event.  Must be `keep` or `drop`.| &#8288 {: style="padding:0"} |


##### `EXTRACT` Definition
This function allows usage of named capturing groups in regular expression to extract fields from event data.  The output is in `JSON` formatted event with named groups as fields.

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Regex       | Named group capturing Regular Expression to match the event.  Captured named groups will be JSON field names. | <img src="../assets/img/padas_ui_task_extract_example.png" class="img-fluid py-5 w-75"> {: rowspan=3} |
| Keep Raw    | Boolean to keep raw data in a separate field.  If set to `true` a field name should be provided.| &#8288 {: style="padding:0"} | 
| Raw Field Name | If raw data is to be kept, this will be the field to store it in. `_raw` is the default.| &#8288 {: style="padding:0"} |


##### `PARSE_CSV` Definition
This function allows parsing CSV formatted data with any delimiter.  The output is `JSON` formatted event with specified field names.

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Field Names | Comma separated list of field names for the CSV data. | <img src="../assets/img/padas_ui_task_parsecsv_example.png" class="img-fluid py-5 w-75"> {: rowspan=4} |
| Delimiter   | Field separator for the CSV items.  Default is comma `,`. | &#8288 {: style="padding:0"} | 
| Keep Raw    | Boolean to keep raw data in a separate field.  If set to `true` a field name should be provided.| &#8288 {: style="padding:0"} | 
| Raw Field Name | If raw data is to be kept, this will be the field to store it in. `_raw` is the default.| &#8288 {: style="padding:0"} |


##### `PARSE_KV` Definition
This function allows parsing key-value pairs within event data with any delimiter.  Left side of the delimiter becomes the field name and right side becomes the field value.  The output is `JSON` formatted event.

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Delimiter   | Field separator for the Key-Value items.  Default is comma `=`. | <img src="../assets/img/padas_ui_task_parsekv_example.png" class="img-fluid py-5 w-75"> {: rowspan=3}  | 
| Keep Raw    | Boolean to keep raw data in a separate field.  If set to `true` a field name should be provided.| &#8288 {: style="padding:0"} | 
| Raw Field Name | If raw data is to be kept, this will be the field to store it in. `_raw` is the default.| &#8288 {: style="padding:0"} |


##### `TIMESTAMP` Definition
This function extracts event timestamp from the given field with the provided format. The output is time in milliseconds in a new field (if specified).  The timestamp information is utilized by stream processing.

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Field       | JSON data field name that holds the timestamp value to be parsed. | <img src="../assets/img/padas_ui_task_timestamp_example.png" class="img-fluid py-5 w-75"> {: rowspan=4}  | 
| Format      | Pattern to extract field data timestamp information based on [Java SE Patterns for Formatting and Parsing](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html). Default pattern is `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.| &#8288 {: style="padding:0"} | 
| Add New Field | Boolean to add a new field for extracted timestamp, represented in milliseconds.  Default is `true`.| &#8288 {: style="padding:0"} | 
| Time Field Name | Field name to add if the above is set to `true`. Default is `_time`.| &#8288 {: style="padding:0"} | 


##### `EVAL` Definition
This function allows data enrichment via various additional mini-functionality.  Input must be `JSON` since fields and conditions require this in order to process event data.

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Condition   | Matching PDL query in order to execute the EVAL action specified. Empty or null query matches all events. | <img src="../assets/img/padas_ui_task_eval_example.png" class="img-fluid py-5 w-75"> {: rowspan=4}  | 
| Action      | Must be on of `add`, `alias`, `regex`, `remove`, `rename`.| &#8288 {: style="padding:0"} | 
| Field | Field name to implement the action.<br/>`add`: new field name<br/>`alias`: existing field name to create an alias for<br/>`regex`: existing field to apply regular expression.<br/>`remove`: existing field to remove<br/>`rename`: existing field to rename| &#8288 {: style="padding:0"} | 
| Value | Each action represents different value. <br/>`add`: new field value<br/>`alias`: new alias field name<br/>`regex`: named capturing regular expression where matched fields are added.<br/>`remove`: N/A<br/>`rename`: new field name| &#8288 {: style="padding:0"} | 


##### `APPY_RULES` Definition
This function applies pre-defined rules (PDL queries) in order to generate event alerts that match them.  The output is enriched with `padas_rules` object array that contain matching rule information as well as the event data.

| Field       | Description                                           | Example |
| -------     | ----------------------------------------------------- | :---: |
| Condition   | Matching PDL query in order to associate the event with the Data model, so that matching rules can be evaluated. | <img src="../assets/img/padas_ui_task_rules_example.png" class="img-fluid py-5 w-75"> {: rowspan=4}  | 
| Data model  | Rules with this matching data model will be evaluated against the event. | &#8288 {: style="padding:0"} | 
| Match All   | If set to `true`, all rules for this data model are evaluated.  If set to `false`, first match wins and evaluation stops. | &#8288 {: style="padding:0"} | 
