---
title: PDL Quick Reference
---

This is a reference guide for the Padas Domain Language (PDL). 

In order to understand how PADAS works, please review [Getting Started](/docs/get-started.html).

## Introduction
PDL is a domain-specific language designed for data processing, with features including querying, evaluation, filtering, renaming, and correlation of streaming event data.  A PDL expression consists of a combination of zero to many expressions and zero or one correlation statement separated by a pipe '`|`' character.  PDL syntax requires fields to be available in JSON object that it compares against and supports nested JSON objects/fields with dotted notation (e.g. `field.subfield.anothersubfield` etc.)

## Syntax
PDL can contain one or more expressions and zero or one correlation statement separated by a pipe `|` character.  Output from an expression or correlation statement becomes the input for the expression that comes after the pipe `|`.  Below grammar represents some generic grammar usage.
```
<expression> | <expression> | ...
<correlation> | <expression> | <expression> | ...
<expression> | ... | <correlation> | <expression> | ...
```

## Field Names and Field Values
For expressions and correlation statement field names (`<fieldName>`) represent the JSON field name and field value (`<fieldValue>`) can be a literal (number or string) or a field name.  Literal strings must be enclosed in double quotation marks.

Field names can not have spaces in them and currently following features are provided:

- Must begin with a letter (`[a-zA-Z]`) or underscore `_`
- Supports dotted notation for nested JSON fields.
- Does NOT support whitespace in field names.
- Accepts alphanumeric characters, minus/dash, underscore, and column (`[a-zA-Z0-9_-:]`)

---

## PDL Examples
--8<-- "pdl/pdl_examples.md"
