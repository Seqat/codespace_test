

//My first code in Rust :D

use std::io;


fn main() {

    //print "Hello, world!" with my style :D
    println!("Hello, world! This is my first code in Rust!");

    // Task-1 : Create a variable called "x" and assign it the value of 5. 
    // Then, print the value of x.     
    
    let mut x:i32 = 5;

    println!("TASK-1 \n {} is my Lucky number",x);
    
    x=10;
    println!("Now, {} is my Lucky number",x);

    // Task-2 : Create a String variable called "input" and take input from the user.
    // Then, print the value of input.
    
    let mut input = String::new();

    println!("TASK-2 \n Oh my! What's your number: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");



    println!("{} is the number came from our ancestors :D",input);



}
