#include<stdio.h>
int main(){
    FILE *ptr;//ptr is a pointer pointing to a file
    //fopen is used to open the file
    //modes of opening a file(similar to python file handling)
    // "r"   → Read mode; file must exist
    // "w"   → Write mode; creates it or overwrites existing content
    // "a"   → Append mode; creates it if it doesn't exist
    // "r+"  → Read + write
    // "w+"  → Write + read; creates or overwrites the file
    // "a+"  → Append + read; creates it if it doesn't exist
    // "rb"   → Read binary file
    // "wb"   → Write binary file; creates or overwrites
    // "ab"   → Append to binary file
    // "rb+"  → Read + write binary file
    // "wb+"  → Read + write binary; creates or overwrites
    // "ab+"  → Read + append binary file
    ptr = fopen("ishaan.txt","r");//ishaan.txt is the name of the file and r is the mode in which the file is opened
    if (ptr==NULL){//if a file does not exist then the value of ptr remains NULL 
        printf("the file does not exist");
    }
    else{
        int num;
        //fscanf is used to read the file 
        fscanf(ptr,"%d",&num);//after this num will have the value equal to the first int stored in the file
        printf("the num is %d\n",num);
        fscanf(ptr,"%d",&num);//after this num will have the value equal to the second int stored in the file
        //num was not equal to the first int because the ptr moves forward with every read
        printf("the num is %d\n",num);
    }
    fclose(ptr);//used to close the file
    return 0;
}