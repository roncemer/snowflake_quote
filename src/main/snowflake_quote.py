# snowflake_quote
# A Python3 function to properly escape and quote string literals for Snowflake
#
# Copyright (c) 2022 Ronald B. Cemer
# Licensed under the MIT license.
#
# Project: https://github.com/roncemer/snowflake_quote

def snowflake_quote(s):
    if s is None:
        return "NULL"

    result = "'"
    for c in s:
        if (c == "'" or c == '"' or c == '\\'):
            result = result + '\\' + c
        elif (c == '\b'):
            result = result + '\\b'
        elif (c == '\f'):
            result = result + '\\f'
        elif (c == '\n'):
            result = result + '\\n'
        elif (c == '\r'):
            result = result + '\\r'
        elif (c == '\t'):
            result = result + '\\t'
        else:
            cc = ord(c)
            if ((cc >= 0x00 and cc <= 0x1f) or cc >= 0x7f):
                result = result + ("\\x%0.2x" % cc)
            else:
                result = result + c
    result = result + "'"
    return result
