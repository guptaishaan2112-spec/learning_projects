#include<stdio.h>
#include<stdlib.h>

int main(){

    //Dynamic memory allocation → memory is allocated during runtime
    //It is useful when we don't know the required memory size beforehand.

    //malloc() → allocates a block of memory of the given size
    int *ptr = malloc(5 * sizeof(int));

    //int *ptr → ptr is a pointer to int which stores the address of allocated memory
    //malloc() → allocates memory from the heap and returns its starting address
    //5 → number of int elements we want memory for
    //sizeof(int) → gives the size of one int in bytes
    //5 * sizeof(int) → total number of bytes required for 5 integers

    //malloc() returns NULL if memory allocation fails
    if(ptr == NULL){
        printf("Memory allocation failed");
        return 1;
    }

    //malloc() does not initialize the allocated memory
    //so the allocated memory initially contains indeterminate/garbage values

    //we can use dynamically allocated memory like an array
    for(int i = 0; i < 5; i++){
        ptr[i] = i + 1;
    }

    for(int i = 0; i < 5; i++){
        printf("%d ", ptr[i]);
    }

    //free() → releases the dynamically allocated memory
    free(ptr);


    //calloc() → allocates memory for multiple elements
    int *ptr2 = calloc(5, sizeof(int));

    //5 → number of elements we want
    //sizeof(int) → size of each element
    //calloc(5, sizeof(int)) → allocates memory for 5 integers
    //calloc() initializes all allocated memory to 0

    if(ptr2 == NULL){
        printf("Memory allocation failed");
        return 1;
    }

    for(int i = 0; i < 5; i++){
        printf("%d ", ptr2[i]);
    }

    free(ptr2);


    //realloc() → changes the size of previously allocated memory
    ptr = malloc(3 * sizeof(int));

    ptr[0] = 10;
    ptr[1] = 20;
    ptr[2] = 30;

    //realloc(pointer, new_size)
    ptr = realloc(ptr, 5 * sizeof(int));

    //ptr → pointer to the memory whose size we want to change
    //5 * sizeof(int) → new total size required for 5 integers
    //realloc() may move the memory to a new location if required

    ptr[3] = 40;
    ptr[4] = 50;

    for(int i = 0; i < 5; i++){
        printf("%d ", ptr[i]);
    }

    free(ptr);
    // free(ptr) → releases the dynamically allocated memory
    // It should be used after we are finished using memory allocated by malloc(), calloc() or realloc()
    // After free(ptr), we should not access the memory through ptr
    return 0;
}