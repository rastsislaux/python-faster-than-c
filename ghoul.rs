fn main() {
    let mut number = 1000;
    while number > 0 {
        println!("{number} - 7 = {}", number - 7);
        number -= 7;
    }
    println!("I'm a ghoul");
}