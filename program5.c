#include <stdio.h>
int main()
{
int a,b,temp;
a=50;
b=30;
printf("a=%d and b=%d",a,b);
temp=a;
a=b;
b=temp;
printf("a=%d and b=%d",a,b);
return 0;
}

