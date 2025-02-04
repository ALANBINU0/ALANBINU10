#include <stdio.h>
int main()
{
int roll_no,age;
float height;
char grade;
printf("enter the roll no");
scanf("%d",&roll_no);
printf("enter the age");
scanf("%d",&age);
printf("enter the height");
scanf("%f",&height);
printf("enter the grade");
scanf(" %c",&grade);
printf("the roll no is %d\n",roll_no);
printf("the age is %d\n",age);
printf("the height is %f\n",height);
printf("the grade is %c",grade);
return 0;
}

