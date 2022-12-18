A task is the single unit of work performed on event data.  Each task has the following built-in functions that can perform processing on an event:

- `FILTER`: Filter an event (keep or drop) based on [PDL](/pdl-reference) or regex definition.  For PDL, the input must be `JSON`.
- `EXTRACT`: Extract any event input with provided Regular Expression defition (named groups). The output is `JSON`.
- `PARSE_CSV`: Parse input `CSV` event into `JSON`.
- `PARSE_KV`: Parse input key-value pairs event into `JSON`.
- `EVAL`: Add, remove or rename fields within `JSON` data.  Both input and output are `JSON`.
- `TIMESTAMP`: Define a field from within the event data (`JSON` formatted) to use as the timestamp.
- `APPLY_RULES`: Apply predefined rules that are tagged with specific data models to events.  It's possible to provide a PDL condition for events to match certain datamodels.


