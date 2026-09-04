#include<stdio.h>
int main(){
    FILE *ptr;
    ptr = fopen("ishaan1.txt","w");
    int num = 780;
    fprintf(ptr,"%d\n",num);//fprintf is used to write in the file
    fprintf(ptr,"%d\n",num);
    fclose(ptr);
    ptr = fopen("ishaan1.txt","a");
    num = 830;
    fprintf(ptr,"%d",num);
    fclose(ptr);
    //writing a string 
    ptr = fopen("ishaan1.txt", "a+");
    if (ptr == NULL) {
        printf("File could not be opened\n");
        return 1;
    }
    //when we open a file in append mode the pointer does not always points to the starting char so while reading we should set it to the starting piont 
    rewind(ptr);//this function sets the pointer to the starting position in the file
    char c = fgetc(ptr); // reads one character
    printf("%c", c);
    fseek(ptr, 0, SEEK_END); // required when switching from reading to writing
    //Move the file pointer 0 positions from the end.
    //fseek(file_pointer, offset, position);
    //SEEK_END --> Start counting the offset from the end of the file.
    //0 --> stop at 0th position from the end of the file
    fputs("hello world", ptr); // writes a string
    fputc('a', ptr);           // writes a single character
    fclose(ptr);

    ptr = fopen("ishaan1.txt","r");
    int read;
    //fscanf only returns value 0 and 1 and eof so if it gets the desired char it return 1 and if it doesnt it returns 0 and if it fails to get input then eof
    while (fscanf(ptr,"%d",&read)==1){//since my file doesnt start with an integer the value of fscanf is 0 as it looks for an int but its not present (so i am changing my write statements to int only) 
        printf("%d\n",read);
    }
    char read1;
    while (fscanf(ptr,"%c",&read1)==1){//since my file doesnt start with an integer the value of fscanf is 0 as it looks for an int but its not present (so i am changing my write statements to int only) 
        printf("%c",read1);
    }
    // or
    rewind(ptr);
    while (1){
        char c2 = fgetc(ptr) ;
        if (c2 == EOF){
            break;
        }
        printf("%c",c2);
    }
    fclose(ptr);
    return 0;
}