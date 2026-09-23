pub trait Capitalize {
    fn capitalize(self) -> String;
}
impl<T: ToString> Capitalize for T {
    fn capitalize(self) -> String {
        let mut s = self
            .to_string()
            .as_str()
            .trim()
            .chars()
            .collect::<Box<[char]>>();
        let cap = s[0].to_uppercase().next().expect("no char");

        s[0] = cap;
        s.iter().collect::<String>()
    }
}
