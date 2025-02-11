#include<stdio.h>
int main() 
{
int i,max=0,min=0,p1=0,p2=0,n;
printf("enter array size");
scanf("%d",&n);
int a[n];
printf("enter the elements");
for (i=0;i<n;i++)
{  
   scanf("%d",&a[i]);
}
max=min=a[0];
for (i=1;i<n;i++)
{
  if (a[i]>max)
  {
    max=a[i];
    p1=i;
   }
  if (a[i]<min)
  { 
     min=a[i];
     p2=i;
  }
}
printf("max is %d is at position %d\n",max,p1);
printf("min is %d is at position %d\n",min,p2);
return 0;
}
  
