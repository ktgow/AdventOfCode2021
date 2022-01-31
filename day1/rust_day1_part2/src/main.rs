use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::str::FromStr;

fn main() {
    // File hosts must exist in current path before this produces output
    if let Ok(mut lines) = read_lines("../input2.txt") {
	let mut window: Vec<i32> = Vec::new();
	for _i in 1..4 {
	    let line = lines.next().unwrap().unwrap();
	    let value = i32::from_str(&line).unwrap();
	    window.push(value);
	}
	assert_eq!(window.len(), 3);

	let mut num_increases = 0;

        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
		let value = i32::from_str(&ip).unwrap();

		let mut new_window: Vec<i32> = Vec::new();
		new_window.resize(2, 0);
		new_window.copy_from_slice(&window[1..]);
		new_window.push(value);
		assert_eq!(new_window.len(), 3);

		if window_average(&new_window) > window_average(&window) {
		    num_increases += 1;
		}
		window = new_window;
            }
        }
	println!("Num increases: {}", num_increases);
    }
}

fn window_average(window: &Vec<i32>) -> f32 {
    let mut sum: f32 = 0.0;
    for value in window {
	sum += *value as f32;
    }
    return sum / window.len() as f32;
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
