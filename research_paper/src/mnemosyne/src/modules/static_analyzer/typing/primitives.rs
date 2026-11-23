/* Signed integers */
/// Standard 8-bit integer.
const CHAR: &str = "i8";
/// Standard 16 bit integer.
/// Also accounts for `short int`.
const INT: &str = "i16";
/// Standard 32-bit integer.
const LONG_INT: &str = "i32";
/// Standard 64-bit integer.
const LONG_LONG_INT: &str = "i64";

/* Unsigned integers */
const UCHAR: &str = "u8";
/// Standard 16 bit integer.
/// Also accounts for `short int`.
const UINT: &str = "u16";
/// Standard 32-bit integer.
const ULONG_INT: &str = "u32";
/// Standard 64-bit integer.
const ULONG_LONG_INT: &str = "u64";

/* floats */
const FLOAT: &str = "f32";
const DOUBLE: &str = "f64";

pub enum Numeric<'a> {
    Char(&'a str),
    Int(&'a str),
    LongInt(&'a str),
    LongLongInt(&'a str),
    Float(&'a str),
}
