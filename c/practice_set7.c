#include<stdio.h>
int main(){
    int a = 5;
    int* b;//b is a variable that stores the address of an int.
    b = &a;
    int** c = &b;//c is a pointer to pointer ie it stores a value that is a pointer to another variable. so here c is the variable that stores the address of a pointer variable that stores the address of another variable which is storing an int value.
    printf("%p\n",&a);//print address of a 
    printf("%p\n",*&b);//print value stored at address of b ie print value of a
    printf("%p\n",*&a);//print the value stored at the address of a 
    printf("%p\n",c);//print address of b
    printf("%p\n",*c);//print value stored in address of b ie address of a 
    printf("%p\n",**c);// ** fetches the value stored in the pointer to pointer variable that the variable that the pointer variable is pointing to. ie print the value stored in the address of a 
    printf("%p\n",**&b);
    return 0;
}
// by using * during decaration of a variable we let the compiler know that this variable stores an address ie this is a pointer variable and when we use * in printf we are telling the compiler to fetch the value from the given address
// b    → address of a
// *b   → 5(value stored at address stored by the a)
// &b   → address of b
//*&a   → 5(value stored at address of a )
//%p is used for pointers in printf like statements
//%u can also be used but %p is explicitly for pointers so its a good practice to use %p 
//%p gives hexadecimal value
//%u gives decimal values