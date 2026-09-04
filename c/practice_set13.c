#include<stdio.h>
int main(){
    int a = 0;
    int m = 1;
    int n = 7;
    char str2[50];
    char str[] = "Ishaan Gupta";
    for (int i = m; i<=n; i++){
        str2[a] = str[m];
        m++;
        a++;
    }
    printf("%s",str2);
    return 0;
}