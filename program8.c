#include <stdio.h>
int main()
{
int num1,num2,sum,sub,mul,div,per;
char oper;
printf("enter number 1");
scanf("%d",&num1);
printf("enter number 2");
scanf("%d",&num2);
printf("enter the operation");
scanf(" %c",&oper);
switch(oper)
{ 
        case'+':
         sum=num1+num2;
         printf("the sum is:%d",sum);
         break;
          
         case'-':
         sub=num1-num2;
         printf("the sub is:%d",sub);
         break;
          
          
         case'*':
         mul=num1*num2;
         printf("the mult is:%d",mul);
         break;
          
          
         case'/':
         div=num1/num2;
         printf("the div is:%d",div);
         break;
         
         case'%':
         per=num1%num2;
         printf("the percentage is:%d",per);
         break;

         default:
         printf("invalid");
         break;
         }
return 0;
}   

