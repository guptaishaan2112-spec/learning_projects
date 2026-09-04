#include<stdio.h>
#include<string.h>// this statement is used whenever we use string methods like strlen, strcpy, strcat etc
int main(){
    //string definition by array
    char str[] = {'i','s','h','a','a','n','\0'};// \0 is for null char it marks the ending of a string
    char* ptr = str;
    // printf("char is %c\n",*str);
    for (int i = 0; i <=6;i++){
        printf("char is %c\n",*ptr);
        ptr++;
    }

    char str1[50] = "hello";
    printf("%s %s",str1,str);

    char str2[50];
    scanf("%49s",str2);
    // & is not written as string already gives an address and it automatically adds a null char when we use enter so we dont have to put it
    //The string should be short enough to fit into the array.
    //scanf cannot be used to input multi word string with spaces 
    printf("%s",str2);

    //gets() func
    char str3[50];
    fgets(str3,sizeof(str3), stdin);
    // gets() was used to read a multi-word string, but it is unsafe and was
    // removed from the C standard. Use fgets() instead.
    //
    // fgets(str3, sizeof(str3), stdin);
    // reads a string including spaces while limiting input to the size of the array.
    
    //puts() func
    puts(str3); // Prints the string & places the cursor on the next line

   //string definition using pointer
   char *str4 = "hello";

   // Array: the array itself cannot be reassigned to another string using =,
    //        but its contents can be changed and the same array can be reused.
    //
    // Pointer: the pointer can be reassigned to point to a different string,
    //          so it can easily be made to refer to another string.

    printf("legth of str4 is %d",strlen(str4));//strlen() Counts the number of characters in a string,excluding the null ('\0') character

    strcpy(str1,"Changed string");
    puts(str1);
    //str1 is now assigned the value Changed string even though it was declared using array 
    // strcpy() copies the contents of one string into a character array.
    // Since an array cannot be reassigned using =, strcpy() lets us reuse the same
    // array variable by replacing its existing string with a new one.
    // Syntax: strcpy(destination, source);

    strcat(str3,str4);
    puts(str3);
    // strcat(destination, source) appends the source string to the end of the destination string.
    // It modifies the destination and leaves the source unchanged.
    // The destination must be writable and have enough space for both strings + '\0'.
    //
    // With an array:
    // char str[20] = "Hello";
    // strcat(str, " World");        // ✅ works
    // The array has its own writable storage, so strcat() can modify its contents.
    //
    // With a pointer:
    // char *ptr = "Hello";
    // strcat(ptr, " World");        // ❌ unsafe
    // This fails because ptr points to a string literal ("Hello"), which should not be modified.
    // Also, the string literal does not guarantee extra space after "Hello" for the appended string.
    //
    // A pointer CAN be used with strcat() if it points to a writable array:
    // char str[20] = "Hello";
    // char *ptr = str;
    // strcat(ptr, " World");        // ✅ works
    // Here ptr points to the writable 20-character array, so strcat() can modify it.
    //
    // Syntax: strcat(destination, source);

    printf("output of strcmp func %d",strcmp(str3,str4));
    // strcmp(string1, string2) compares two strings character by character.
    // It returns:
    //     0  → both strings are equal
    //    <0  → string1 comes before string2
    //    >0  → string1 comes after string2
    //
    // Use strcmp() to compare the CONTENTS of strings; don't use == for string comparison.
    // == compares addresses when used with arrays/pointers, not the actual characters.
    //
    // The comparison is case-sensitive and stops at the first different character.
    // strcmp() does not modify either string.
    //
    // Syntax:
    // strcmp(string1, string2);
    return 0;
}