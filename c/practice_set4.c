#include<stdio.h>
int main(){
    int i = 0;
    while (i<5){ 
        printf("while loop iter %d\n",i);
        i+=1;
    }// a while loop checks the condition and then executes the code
    i=0;
    do{    
        printf("do - while loop iter %d\n",i);    
        i+=1;
    }while (i<5);// this is called a do - while loop it executes the code first and then checks the condition. it executes atleast once whereas while loop may or may not run atleast once
    i=0;
    for (i;i<5;i+=1){//for (initialize; condition test; increment or decrement){/*code*/}
        printf("for increment loop iter %d\n",i);
    }
    i=5;
    for (i;i;i-=1){//for (initialize; condition test; increment or decrement){/*code*/}
        //printf("for decrement loop iter %d\n",i);
        if (i==3){
            printf("since i = 3 break the loop");
            break;//exit the loop
        }
        // else if(i==4){
        //     continue;//skip the iteration see iter with i = 4 is not printed in the output
        // }
        printf("for decrement loop iter %d\n",i);     
    }// here in condition i is used as when i value reaches 0 c interprets it as a false condition and hence the loop terminates
    return 0;
}