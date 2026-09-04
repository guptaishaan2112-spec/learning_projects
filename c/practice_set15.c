#include<stdio.h>
#include<string.h>
//struct is a datatype like dictionary in python, it is used in a very similar way to class variable in python
struct emp{
    int id;
    char name[50];
    int salary;
};
typedef struct emp1{
    int id;
    char name[50];
    int salary;
}EMPLOYEE;
struct emp new_emp_salary_plus_id(struct emp emp1,struct emp emp2){
    struct emp new_emp;
    new_emp.id = emp1.id + emp2.id;
    new_emp.salary = emp1.salary + emp2.salary;
    return new_emp;
}
EMPLOYEE new_emp_2(EMPLOYEE emp1,EMPLOYEE emp2){
    EMPLOYEE new_emp;
    new_emp.id = emp1.id + emp2.id;
    new_emp.salary = emp1.salary + emp2.salary;
    return new_emp;
}

int main(){ 
    struct emp apple[100];//an array of structures
    apple[0].id = 1;
    apple[0].salary = 1000;
    strcpy(apple[0].name,"Ishaan");

    struct emp ishaan = {2,"ishaan1",1000};
    printf("%d %s %d\n", ishaan.id,ishaan.name,ishaan.salary);
    struct emp aryan = {0};//all values set to 0
    
    //pointer to structures
    struct emp e1;
    e1.id = 3;
    e1.salary = 1000;
    struct emp *ptr;//ptr points to a strcture named emp
    ptr = &e1;//ptr stores the address of structure named emp with name e1
    printf("%d\n",(*ptr).id);//Go to the structure that ptr points to, then access its id.
    //or we can use arrow operator ie
    printf("%d\n",ptr->id);
    
    //using typedef
    EMPLOYEE emp1;
    emp1.id = 4;
    
    //we can also use typedef here if you dont wanna do it while defining the struct
    typedef struct emp EMP;
    EMP emp2;
    emp2.id = 5;
    
    EMP emp3 = {2,"ishaan1",1000};
    EMP *ptr1 = &emp3;
    printf("%d %s %d\n", ptr1->id,ptr1->name,ptr1->salary);

    // IMPORTANT: A structure can be initialized using {} only when it is declared.
    //
    // ✅ Valid:
    // EMP emp3 = {2, "ishaan1", 1000};
    //
    // ❌ Invalid after declaration:
    // EMP emp3;
    // emp3 = {2, "ishaan1", 1000};
    //
    // After declaration, assign members individually:
    // emp3.id = 2;
    // strcpy(emp3.name, "ishaan1");
    // emp3.salary = 1000;
    // 
    // OR assign another structure of the same type:
    // EMP temp = {2, "ishaan1", 1000};
    // emp3 = temp;   // ✅ valid
    //
    // So remember:
    // Initialization → EMP emp3 = {...};  ✅
    // Structure assignment → emp3 = temp;  ✅
    // Brace assignment → emp3 = {...};    ❌
    struct emp new_emp = new_emp_salary_plus_id(e1 ,ishaan);
    printf("new emp %d %d",new_emp.id,new_emp.salary);
    return 0;
}