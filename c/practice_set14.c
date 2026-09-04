#include<stdio.h>
int main(){
    typedef int ishaan;
    //typedef allows us to create our own datatype
    //it is majorly used for structure though it can be used for any datatype
    ishaan a = 90;
    printf("using typedef %d",a);
    //even after using typedef we are still able to use the previous datatype
    printf("using int %d",a);
    return 0;
}