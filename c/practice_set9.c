#include<stdio.h>
int main(){
    int a = 10;
    int* ptr = &a;
    printf("address of pointer = %u",ptr);
    ptr++;
    printf("value of ptr after increment = %u",ptr);
    return 0;
}
//ptr was incremented by 4 this means that the int value is stored in 4 bytes therefore after incrementing the address once it means storing another int after the one that was already stored and returning the new value of address(though no new int is stored inside the var it is just for understanding)

//if it was not an int but a char then each char is stored in one byte therefore the address would be incremented by only one

// so increment of pointer depends on the datatype its pointing to