use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::str::FromStr;

fn main() {
    let lines = read_lines("../input2.txt").unwrap();
    let result = calculate_result(lines);
    println!("Result: {}", result);
}

fn calculate_result<R: BufRead>(lines: io::Lines<R>) -> u32 {
    let mut horizontal: u32 = 0;
    let mut depth: u32 = 0;

    for line_result in lines {
        if let Ok(line) = line_result {
	    match parse_line(&line) {
		Action::FORWARD(value) => horizontal += value,
		Action::DOWN(value) => depth += value,
		Action::UP(value) => depth -= value,
	    }
            //println!("{}", ip);
        }
    }
    println!("Final position: <{}, {}>", horizontal, depth);
    horizontal * depth
}

enum Action {
    FORWARD(u32),
    DOWN(u32),
    UP(u32),
}

fn parse_line(line: &str) -> Action {
    let parts: Vec<&str> = line.split(' ').collect();
    let command: &str = parts[0];
    let value = u32::from_str(&parts[1]).unwrap();
    if command == "forward" {
	return Action::FORWARD(value);
    } else if command == "down" {
	return Action::DOWN(u32::from_str(&parts[1]).unwrap());
    } else if command == "up" {
	return Action::UP(value);
    }
    panic!("Unrecognized command: {}", command);
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::Cursor;

    #[test]
    fn test_calculation() {
	let test_input = b"forward 5
down 5
forward 8
up 3
down 8
forward 2";
	let reader = Cursor::new(test_input);
	let result = calculate_result(reader.lines());
        assert_eq!(result, 150);
    }
}
