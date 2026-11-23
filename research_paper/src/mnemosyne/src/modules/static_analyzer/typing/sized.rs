use super::primitives::Numeric;

pub enum TypeAlloc {
    Heap,
}

pub struct Sized<'a> {
    resizeable: bool,
    ret_type: Numeric<'a>,
}

impl Sized {
    pub fn new() {
        //! create a new stored value for detecting sized types.
    }
}
