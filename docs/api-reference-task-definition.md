---
title: Task Definition REST API
---

--8<-- "description_task.md"

## Important Notes

- This section describes the function definition of a task, for generic API call, please refer to [Tasks REST API](api-reference.md#_tasks).  
- Padas Engine verifies requests against the JSON schema defined as [Padas Task Schema](/assets/config/PadasTaskSchema.json).
- For description of each definition field and default values please refer to [Stream Configuration](stream-config.md#tasks)

## Task Definition Examples

### FILTER Definition Example

```json
{
  "id": 1,
  "name": "MyTask Name",
  "description": "MyTask description goes here.",
  "function": "FILTER",
  "definition": {
    "type": "regex",
    "action": "drop",
    "value": "regex goes here"
  }
}
```

### EXTRACT Definition Example

```json
{
  "id": 1,
  "name": "MyTask Name",
  "description": "MyTask description goes here.",
  "function": "EXTRACT",
  "definition": {
    "field": "somefield",
    "regex": "someregex text here",
    "keepRaw": false
  }
}
```

### PARSE_CSV Definition Example

```json
{
  "id": 1,
  "name": "MyTask Name",
  "description": "MyTask description goes here.",
  "function": "PARSE_CSV",
  "definition": {
    "fieldNames": "field1,field2,field3",
    "delimeter":"|"
  }
}
```

### PARSE_KV Definition Example

```json
{
  "id": 1,
  "name": "MyTask Name",
  "description": "MyTask description goes here.",
  "function": "PARSE_KV",
  "definition": {
    "delimeter":":"
  }
}
```

### TIMESTAMP Definition Example

```json
{
  "id": 1,
  "name": "MyTask Name",
  "description": "MyTask description goes here.",
  "function": "TIMESTAMP",
  "definition": {
    "field": "somefield",
    "format": "%H%M%S"
  }
}
```

### PDL_EXPRESSION Definition Example

```json
{
  "id": 1,
  "name": "MyTask Name",
  "description": "MyTask description goes here.",
  "function": "PDL_EXPRESSION",
  "definition": {
    "pdl" : "field1=\"value1\" AND field2 > 100 | eval field3=if(field2 < 400, 0, 1)"
  }
}
```

### APPLY_RULES Definition Example

```json
{
  "id": 1,
  "name": "MyTask Name",
  "description": "MyTask description goes here.",
  "function": "APPLY_RULES",
  "definition": {
    "rules": [
      "rule1",
      "rule2"
      ],
    "matchAll": false
  }
}
```