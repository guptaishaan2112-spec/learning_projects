#include<stdio.h>
int sum1(int, int);// value based function call --> this type of function call cant change the value stored in the original variable that are passed to it like in sum1(x,y) only the value of its copy inside the function will be changed to 5 and the value of original(in python like global x) will remain 3 only it wont change by this type of function call
int sum1(int a, int b){
    a = 5;
    return a + b;
}

int sum2(int *,int *);//reference based function call --> this type of function call can change the value stored in the original variable as it takes in memory address as the input and can change the value directly from the memory
int sum2(int *a, int *b){
    *a = 5;//value stored at the address stored by a = 5 so it changes the value from location at which it is stored and hence can make changes in the global variable
    return *a + *b;//value stored at the address stored by a plus that of b
} 

int main(){
    int x = 3, y = 4;
    int* x_address = &x;
    int* y_address = &y;
    printf("for sum1 sum is %d\n", sum1(x,y));
    printf("value of x after sum1= %d\n",x);
    printf("from sum2 sum is %d\n", sum2(x_address,y_address));
    printf("value of x after sum2= %d\n",x);
    return 0;
}