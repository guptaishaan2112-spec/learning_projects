#include<stdio.h>
int main(){
    int a=4;
    //using curly brackets in if else is a good practice however the code written below also works the same way
    if (a=10)//since if has an assignment and not a condition eg a=10 or a='b' or just 5, therefore is takes it as a true value ie 1 and hence the if statement 
    printf("a is 10 %d");
    else if (0) //here if clause has a value 0 explicitly mentioned therefore else clause will execute
    printf("ans is o");
    else
    printf("a is 4");
}
