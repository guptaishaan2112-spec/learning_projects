#include<stdio.h>

//giving array as an argument to a function

void printArray(int arr[], int size) {// or --> void printArray(int *arr, int size)
    //here if we change anything in the array it will also be in the original array as we are providing the address the of the elements and not the value

    //When an array is passed to a function, the array name is converted to a pointer to its first element, so the function receives the address of the first element rather than a copy of the entire array. Since the elements are stored consecutively in memory, pointer arithmetic allows the function to move from one element to the next (arr + 1, arr + 2, etc.), with the movement based on the size of the data type. Therefore, arr[i] is essentially equivalent to *(arr + i), allowing the function to access and modify the original array.
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}

int main(){
    int marks[90];//it tells the compiler to make space or an array for 90 integer values indexing from 0 to 89
    printf("enter marks 2\n");
    scanf("%d",&marks[2]);
    marks[0]=30;//assign the 0th index value 30
    marks[1]=50;
    printf("marks 0 is %d and marks 1 is %d and marks 2 is %d\n", marks[0],marks[1],marks[2]);
    printf("marks 10 is %d\n",marks[10]);//by default all the other values in the array are zero when they are not assigned any value
    int a[] = {10,20,30};
    int* ptr = a;// this line means --> int* ptr = &a[0];
    //accessing array with the help of indexes
    for (int i=0;i<3;i++){
        printf("value of %d place is %d\n",i,a[i]);
        printf("value of %d place is %d\n",i,&a[i]);
        //every address has a 4 unit gap this indicates each int stored in the array takes up 4 bytes and each int is stored in contiguous blocks and not at random places in the memory
    }
    //accessing array with the help of a pointer
    for (int i = 0;i<3;i++){
        printf("value of %d place is %d\n",i,*ptr);
        ptr++;
    }
    // function call in arrays
    int numbers[] = {10, 20, 30, 40, 50};
    printArray(numbers, 5);

    //multidimensional arrays
    int arr[3][2] = {{1,2},{3,4},{5,6}};//2 dim array with 3 rows and 2 columns if we relate it to python ml
    //they are also stored contiguously first [0][0] ie 1 then [0][1] ie 2 then [1][2] ie 3 and so on
    ptr = &arr[0][0];// it will take the address of first element ie [0][0]
    for (int i = 0; i<6;i++){
        printf("value of %d place is %d\n",i,*ptr);
        ptr++;
    }
    return 0;
}


