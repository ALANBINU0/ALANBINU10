#include<stdio.h>
void palindrome(int);
int main()
{
int x;
printf("enter the number");
scanf("%d",&x);
palindrome(x);
return 0;
}
void palindrome(int a)
{
int rev=0,rem,num;
num=a;
while (a>0)
{
rem=a%10;
rev=rev*10+rem;
a=a/10;
}
if(num==rev)
{
printf("the given no is palindrome");
} 
else
{
printf("the given no is not a palindrome");
}
}

