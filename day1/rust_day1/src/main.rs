use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::str::FromStr;

fn main() {
    // File hosts must exist in current path before this produces output
    if let Ok(mut lines) = read_lines("../input.txt") {
	let first_line = lines.next().unwrap().unwrap();
	let mut last_value = i32::from_str(&first_line).unwrap();
	let mut num_increases = 0;

        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
		let value = i32::from_str(&ip).unwrap();

		if value > last_value {
		    num_increases += 1;
		}
		last_value = value;
                //println!("{}", ip);
            }
        }
	println!("Num increases: {}", num_increases);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
