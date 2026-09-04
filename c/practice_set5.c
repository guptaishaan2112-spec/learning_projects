#include<stdio.h>
int main(){
    int a,b;
    printf("enter no. \n");
    scanf("%d",&a);
    printf("enter no. \n");
    scanf("%d",&b);
    int no_of_prime = 0;
    int isprime =0;
    for (int i=a+1; i<b; i++){
        if (i==2){
            isprime = 1;
        }
        else if(i==1){
            isprime = 0;
        }
        else{
            for (int j=2; j<=i/2 + 1; j++){
                if (i%j==0){
                    isprime=0;
                    break;
                } 
                else{
                    isprime=1;
                }
            }
        }
        if (isprime){
            no_of_prime+=1;
            printf("prime no. = %d\n",i);
        }
    }
    printf("no. of prime = %d",no_of_prime);
    return 0;
}