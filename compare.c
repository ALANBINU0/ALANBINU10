#include<stdio.h>
#include<string.h>
int main()
{
char str1[30],str2[60];
printf("enter first string");
scanf("%s",str1);
printf("enter second string");
scanf("%s",str2);
if (strcmp(str1,str2)==0)
{
 printf("the strings are equal\n");
 }
else
{
printf("the strings are not equal\n");
}
return 0;
}
