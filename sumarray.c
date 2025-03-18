#include<stdio.h>
int arrsum(int arr[],int);
int main()
{
int n,i,result;
printf("enter te number of elements");
scanf("%d",&n);
int a[n];
printf("\n enter the elements");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
result=arrsum(a,n);
printf("the sum of elements in array:%d",result);
return 0;
}
int arrsum(int arr[],int a )
{
int sum=0;
for(int i=0;i<a;i++)
{
sum=sum+arr[i];
}
return sum;
}
