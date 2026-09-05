#include<iostream>
using namespace std;//we can either define it globally like this or in program too
// std → standard namespace
// It contains features of the C++ standard library
// Examples: std::cout, std::cin, std::string, std::vector, std::sort
int main(){
    cout << "Hello world!";//cout is compiler output so its like a print statement
    cout << endl;//endl is used for new line
    cout << "My name is Ishaan\n";//\n can also be used for new line 
    std::cout << "I am 17 years old";//defining namespace during the program (but since its a hassle witing it again and again like this we generally define it in the start globaly)
    
}