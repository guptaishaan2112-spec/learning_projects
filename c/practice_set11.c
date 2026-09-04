#include<stdio.h>
void reverse(int arr[],int size){
    int temp_arr[size];
    for (int i = 0; i<size;i++){
        temp_arr[i] = arr[size-i-1];
    }
    for (int i = 0;i<size;i++){
        arr[i] = temp_arr[i];
    }
}
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}
int main(){
    int arr[] = {1,2,3,4,5};
    reverse(arr,5);
    printArray(arr,5);
    return 0;
}