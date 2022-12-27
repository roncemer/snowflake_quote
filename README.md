# snowflake_quote
Python3 and JavaScript functions to properly escape and quote string literals for Snowflake

Copyright (c) 2022 Ronald B. Cemer.

Licensed under the MIT license.

# MANDATORY USAGE

If you are quoting string literals in Python3 or JavaScript for the purpose of building SQL statements for Snowflake, you *MUST* use this library, or a functionally identical equivalent, in order to avoid creating SQL injection vectors which can be easily exploited by malicious actors.

# Running the tests

To run the tests:

```sh
python3 src/test/test_snowflake_quote.py
node src/test/test_snowflake_quote.js
```
