#include <stdio.h>
int fact(int);
int main()
{
     int x;
     printf("enter the number");
     scanf("%d",&x);
     printf("the factorial of %d is %d",x,fact(x));
     return 0;
}
int fact(int a)
{
      int factorial=1,i;
      for(i=1;i<=a;i++)
      {
         factorial*=i;
         }
      return factorial;
}

