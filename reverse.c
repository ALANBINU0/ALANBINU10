#include <stdio.h>
int main()
{
 char str[50],temp;
 int len,i,j;
 printf("enter the string");
 scanf("%[^\n]",str);
 for(len=0;str[len]!='\0';len++);
 i=len-1;
 for(j=0;j<len/2;j++,i--)
 {
 temp=str[i];
 str[i]=str[j];
 str[j]=temp;
 }
printf("The reversed string is %s",str);
return 0;
}
