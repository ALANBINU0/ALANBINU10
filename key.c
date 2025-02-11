#include<stdio.h>
int main() 
{
int a[20],i,flag=0,p=0,key,n;
printf("enter array size");
scanf("%d",&n);
printf("enter a element");
for (i=0;i<n;i++)
{  
   scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
printf("%d\t",a[i]);
}
printf("enter key");
scanf("%d",&key);
for(i=0;i<n;i++)
{
   if (a[i]==key) 
   {
   flag=1;
   p=i;
   break;
   }
  }
  if (flag==0)
  {
  printf("element not found");
  }
  else
  {
  printf("element %d is found at %d\n",key,p);
}   
return 0;
}
