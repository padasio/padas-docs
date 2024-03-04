---
title: About Padas Regular Expressions
layout: documentation
---

### About Padas Regular Expressions
Regular expressions, often shortened to regex, are powerful tools used to search, match, and manipulate text based on specific patterns. They are widely used in various fields, including programming, linguistics, and text processing. This page provides an introductory guide to regular expressions in Padas and some of the common information, drawing examples from the [Java Pattern](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/regex/Pattern.html) class.

Regular expressions in Padas are used within the following context:

- [EXTRACT](/stream-config/#extract-definition) Task definition
- [FILTER](/stream-config/#filter-definition) Task definition
- [rex](/pdl-expression/#rex) command within PPadas Domain Language (PDL)

#### Terminology
- **Pattern**: A sequence of characters representing the search criteria.
- **Match**: When the pattern successfully finds an occurrence in the text.
- **Group**: A portion of the pattern enclosed in parentheses, often used for capturing or manipulating specific parts of the matched text.
- **Quantifier**: A symbol specifying how many times a preceding character or group can appear in the match.

#### Syntax
Regular expressions use a combination of literal characters and special characters to define their patterns. Here are some common elements:

- **Literal characters**: Match themselves, e.g., "`a`", "`b`", "`1`".
- **Metacharacters**: Have special meanings, e.g., "`.`" (matches any single character), "`^`" (matches the beginning of the string), "`$`" (matches the end of the string).
- **Character classes**: Enclosed in square brackets `[]`, represent a set of characters that can match, e.g., `[abc]` matches any of "a", "b", or "c".
- **Escape sequences**: Used to represent literal versions of metacharacters, e.g., "." matches a literal period.


#### Character Types
- **`.`**: Matches any single character except newline.
- **`\d`**: Matches any digit (0-9).
- **`\w`**: Matches any word character (alphanumeric and underscore).
- **`\s`**: Matches any whitespace character (space, tab, newline, etc.).
- **`\D`**: Matches any non-digit character.
- **`\W`**: Matches any non-word character.
- **`^`** : Matches the beginning of the string.
- **`$`** : Matches the end of the string.


#### Group Quantifiers
- **`*`**: Matches the preceding character or group zero or more times.
- **`+`**: Matches the preceding character or group one or more times.
- **`?`**: Matches the preceding character or group zero or one time.
- **`{n}`**: Matches the preceding character or group exactly n times.
- **`{n,m}`**: Matches the preceding character or group at least n but no more than m times.


#### Capturing Groups
Enclosing a part of the pattern in parentheses () creates a capturing group. This allows capturing the matched text for later use. The captured text can be accessed using special methods provided by the programming language or tool.

**_IMPORTANT NOTE_**: Named Capturing Group names MUST contain alphanumeric characters only (special characters such as underscore `_` or period `.` are not supported).  If you need to use these characters in the field name try utilizing [eval](/pdl-expression/#eval) or [rename](/pdl-expression/#rename) commands after field extraction.

#### Examples

**Matching a phone number** (e.g. to be used with [FILTER](/stream-config/#filter-definition) task)

- Regular Expression Pattern: `\d{3}-\d{3}-\d{4}`
- Description: This pattern matches phone numbers in the format ###-###-####, where `\d` represents any digit.


**Extracting first name from a string** (e.g. to be lused with [EXTRACT](/stream-config/#extract-definition) task or [rex](/pdl-expression/#rex) PDL command):

- Regular Expression Pattern: `(?<firstname>.+?)\s+.+)`
- Description: This example demonstrates capturing the first word (assumed to be the first name) using a capturing group as a new field named `firstname`.  For example, if the input string is `"John Doe"`, the new field will have the value `"John"`.
```json
{
  ...
  "firstname": "John"
  ...
}
```

These are just a few examples to illustrate basic concepts. Remember that regular expressions can be complex and require practice to master. Refer to the [Java Pattern](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/regex/Pattern.html) class for more detailed information and advanced features.