use clap::Parser;

#[derive(Debug, Clone, Parser)]
pub struct NoteArgs {
    #[command(subcommand)]
    pub commands: Commands,
    /// Open in the a text editor.
    /// if not set, it will default to using
    /// notepad on windows, and vim on linux.
    #[arg(short, long)]
    pub edit: bool,
}
#[derive(Debug, Clone, Parser)]
pub enum Commands {
    /// Creates a new note.
    New(NewArgs),
}
#[derive(Debug, Clone, Parser)]
pub struct NewArgs {
    /// Name of the file.
    pub filename: String,
    #[arg(long, short, value_delimiter = ',')]
    /// Appends the Keywords to the file;
    /// Separated by commas.
    pub keywords: Vec<String>,
    #[arg(long, short)]
    /// When provided this will title the note
    /// the following name. Otherwise, it uses
    /// the file name as the file name.
    pub title: Option<String>,
}
