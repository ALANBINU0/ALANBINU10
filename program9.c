#include <stdio.h>
int main()
{
    int n,i,fact=1;
    printf("enter the number");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
       {
       fact=fact*i;
       }
     printf("the factorial is %d",fact);
   if (n<0)
   {
   printf("invalid");
   }
   
          return 0;
     }
