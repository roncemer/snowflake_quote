module.exports.snowflake_quote = function(s) {
    if (s === null) return 'NULL';

    let result = "'"
    for (let i = 0, n = s.length; i < n; i++) {
        let c = s[i];
        if (c == "'" || c == '"' | c == '\\') {
            result = result + '\\' + c;
        } else if (c == '\b') {
            result = result + '\\b';
        } else if (c == '\f') {
            result = result + '\\f';
        } else if (c == '\n') {
            result = result + '\\n';
        } else if (c == '\r') {
            result = result + '\\r';
        } else if (c == '\t') {
            result = result + '\\t';
        } else {
            let cc = c.charCodeAt(0);
            if ((cc >= 0x00 && cc <= 0x1f) || cc >= 0x7f) {
                cc = cc.toString(16);
                if (cc.length < 2) cc = "0" + cc;
                result = result + "\\x" + cc;
            } else {
                result = result + c;
            }
        }
    }
    result = result + "'"
    return result
}
