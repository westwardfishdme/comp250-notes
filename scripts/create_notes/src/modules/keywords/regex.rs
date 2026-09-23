use std::{collections::HashSet, error::Error, fs, path::PathBuf};

use regex::Regex;

const REGEX_STR: &str = "^(\\*\\*Keywords:\\*\\*)";
trait Capitalize {
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

pub fn find_keywords(
    file: PathBuf,
    exclude: &Option<Vec<String>>,
) -> Result<Option<HashSet<String>>, Box<dyn Error>> {
    //! returns a list of all keywords.
    //! if exclude is set to `true`-- any keywords in files containing
    //! what is stored at compile time will be ignored.

    let mut keywords: HashSet<String> = HashSet::new();
    // regex we use to find keywords.
    let re = Regex::new(REGEX_STR)?;
    let fcontent = fs::read_to_string(&file)?;

    for (line, text) in fcontent.lines().enumerate() {
        // read the lines until we find a match and once found,
        // append the next line to keywords
        if re.is_match(text) {
            let next_line = line + 1;

            match &fcontent.lines().nth(next_line) {
                Some(v) => {
                    if v.trim().is_empty() {
                        return Ok(None);
                    }

                    v.split(',').for_each(|k| {
                        keywords.insert(k.capitalize());
                    })
                }
                None => return Err("File ended at 'keywords'".into()),
            };
            // if we have an exclusion list...
            if let Some(exclude) = exclude {
                for word in exclude {
                    if !word.is_empty() {
                        let word = word.as_str().trim().to_string().to_lowercase();
                        keywords.remove(&word.capitalize());
                    }
                }
            };

            return Ok(Some(keywords));
        }
    }
    // we couldn't find a match
    Ok(None)
}
