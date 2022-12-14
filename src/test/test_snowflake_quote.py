# snowflake_quote
# A Python3 function to properly escape and quote string literals for Snowflake
#
# Copyright (c) 2022 Ronald B. Cemer
# Licensed under the MIT license.
#
# Project: https://github.com/roncemer/snowflake_quote

import os
import sys

os.sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from main.snowflake_quote import snowflake_quote

expected_results = [
    """'\\x00'""", """'\\x01'""", """'\\x02'""", """'\\x03'""", """'\\x04'""", """'\\x05'""", """'\\x06'""", """'\\x07'""",
    """'\\b'""", """'\\t'""", """'\\n'""", """'\\x0b'""", """'\\f'""", """'\\r'""", """'\\x0e'""", """'\\x0f'""", """'\\x10'""",
    """'\\x11'""", """'\\x12'""", """'\\x13'""", """'\\x14'""", """'\\x15'""", """'\\x16'""", """'\\x17'""", """'\\x18'""",
    """'\\x19'""", """'\\x1a'""", """'\\x1b'""", """'\\x1c'""", """'\\x1d'""", """'\\x1e'""", """'\\x1f'""",
    """' '""", """'!'""", """'\\"'""", """'#'""", """'$'""", """'%'""", """'&'""", """'\\''""",
    """'('""", """')'""", """'*'""", """'+'""", """','""", """'-'""", """'.'""", """'/'""",
    """'0'""", """'1'""", """'2'""", """'3'""", """'4'""", """'5'""", """'6'""", """'7'""",
    """'8'""", """'9'""", """':'""", """';'""", """'<'""", """'='""", """'>'""", """'?'""",
    """'@'""", """'A'""", """'B'""", """'C'""", """'D'""", """'E'""", """'F'""", """'G'""",
    """'H'""", """'I'""", """'J'""", """'K'""", """'L'""", """'M'""", """'N'""", """'O'""",
    """'P'""", """'Q'""", """'R'""", """'S'""", """'T'""", """'U'""", """'V'""", """'W'""",
    """'X'""", """'Y'""", """'Z'""", """'['""", """'\\\\'""", """']'""", """'^'""", """'_'""",
    """'`'""", """'a'""", """'b'""", """'c'""", """'d'""", """'e'""", """'f'""", """'g'""",
    """'h'""", """'i'""", """'j'""", """'k'""", """'l'""", """'m'""", """'n'""", """'o'""",
    """'p'""", """'q'""", """'r'""", """'s'""", """'t'""", """'u'""", """'v'""", """'w'""",
    """'x'""", """'y'""", """'z'""", """'{'""", """'|'""", """'}'""", """'~'""", """'\\x7f'""",
    """'\\x80'""", """'\\x81'""", """'\\x82'""", """'\\x83'""", """'\\x84'""", """'\\x85'""", """'\\x86'""", """'\\x87'""",
    """'\\x88'""", """'\\x89'""", """'\\x8a'""", """'\\x8b'""", """'\\x8c'""", """'\\x8d'""", """'\\x8e'""", """'\\x8f'""",
    """'\\x90'""", """'\\x91'""", """'\\x92'""", """'\\x93'""", """'\\x94'""", """'\\x95'""", """'\\x96'""", """'\\x97'""",
    """'\\x98'""", """'\\x99'""", """'\\x9a'""", """'\\x9b'""", """'\\x9c'""", """'\\x9d'""", """'\\x9e'""", """'\\x9f'""",
    """'\\xa0'""", """'\\xa1'""", """'\\xa2'""", """'\\xa3'""", """'\\xa4'""", """'\\xa5'""", """'\\xa6'""", """'\\xa7'""",
    """'\\xa8'""", """'\\xa9'""", """'\\xaa'""", """'\\xab'""", """'\\xac'""", """'\\xad'""", """'\\xae'""", """'\\xaf'""",
    """'\\xb0'""", """'\\xb1'""", """'\\xb2'""", """'\\xb3'""", """'\\xb4'""", """'\\xb5'""", """'\\xb6'""", """'\\xb7'""",
    """'\\xb8'""", """'\\xb9'""", """'\\xba'""", """'\\xbb'""", """'\\xbc'""", """'\\xbd'""", """'\\xbe'""", """'\\xbf'""",
    """'\\xc0'""", """'\\xc1'""", """'\\xc2'""", """'\\xc3'""", """'\\xc4'""", """'\\xc5'""", """'\\xc6'""", """'\\xc7'""",
    """'\\xc8'""", """'\\xc9'""", """'\\xca'""", """'\\xcb'""", """'\\xcc'""", """'\\xcd'""", """'\\xce'""", """'\\xcf'""",
    """'\\xd0'""", """'\\xd1'""", """'\\xd2'""", """'\\xd3'""", """'\\xd4'""", """'\\xd5'""", """'\\xd6'""", """'\\xd7'""",
    """'\\xd8'""", """'\\xd9'""", """'\\xda'""", """'\\xdb'""", """'\\xdc'""", """'\\xdd'""", """'\\xde'""", """'\\xdf'""",
    """'\\xe0'""", """'\\xe1'""", """'\\xe2'""", """'\\xe3'""", """'\\xe4'""", """'\\xe5'""", """'\\xe6'""", """'\\xe7'""",
    """'\\xe8'""", """'\\xe9'""", """'\\xea'""", """'\\xeb'""", """'\\xec'""", """'\\xed'""", """'\\xee'""", """'\\xef'""",
    """'\\xf0'""", """'\\xf1'""", """'\\xf2'""", """'\\xf3'""", """'\\xf4'""", """'\\xf5'""", """'\\xf6'""", """'\\xf7'""",
    """'\\xf8'""", """'\\xf9'""", """'\\xfa'""", """'\\xfb'""", """'\\xfc'""", """'\\xfd'""", """'\\xfe'""", """'\\xff'""",
]

num_errors = 0
for cc in range(0, 256):
    expected = expected_results[cc]
    res = snowflake_quote(chr(cc))
    error = ""
    if res != expected:
        error = " *** ERRROR ***"
        num_errors = num_errors + 1
    print("Hex value: %0.2x, quoted string: %s, expected: %s%s" % (cc, res, expected, error))

expected = "NULL"
error = ""
res = snowflake_quote(None)
if res != expected:
    error = " *** ERRROR ***"
    num_errors = num_errors + 1
print("None type, quoted string: %s, expected: %s%s" % (res, expected, error))

if num_errors > 0:
    print("%d ERRORS!" % (num_errors), file=sys.stderr)
    sys.exit(10)

print("SUCCESS!")
sys.exit(0)
