#include <stdio.h>

int main() {
    int a, b;
    // char d = "weff"; this is wrong as char can have only one character in it 
    scanf("%d", &a);
    scanf("%d", &b);
    printf("product of the two no. is %d", a * b);
    return 0;//this is to indicate that the program ran successfully if main func is returning any other value that shows that something went wrong
    //we right return 0 by convention and the program will execute normally even without this statement 

    int i = 0;
    i=i+5;
    printf("i=%d\n",i);
    printf("i=%d\n",i++);// first print i then increment it by 1. similarly i-- is also there
    printf("i=%d\n",i);
    printf("i=%d\n",++i);// first increment i by 1 and then print it. similarly --i is also there
    printf("i=%d\n",i);
    i+=2;// same as writing i=i+2. similarly there are -=, *=, /=, %= etc
    return 0;
}
