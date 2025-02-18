#include<stdio.h>
int main()
{
int row1,col1,row2,col2,i,j,a[10][10],b[10][10],c[10][10];
printf("enter the no of rows and columns of first matrix");
scanf("%d%d",&row1,&col1);
printf("enter the no of rows and columns of second matrix");
scanf("%d%d",&row2,&col2);
if (row1!=row2 && col1!=col2)
{ 
printf("matrix cannot be added");
return 0;
}
else 
{
printf("enter the elements in first matrix");
for(i=0;i<row1;i++)
{
  for(j=0;j<col1;j++)
  {
   scanf("%d",&a[i][j]);
  }
}
printf("enter the elements in second matrix");
for(i=0;i<row2;i++)
{
  for(j=0;j<col2;j++)
  {
   scanf("%d",&b[i][j]);
  }
}
for(i=0;i<row1;i++)
{
  for(j=0;j<col1;j++)
  {
    c[i][j]=a[i][j]+b[i][j];
  }
}
printf("sum of 2 matrices is \n");
for(i=0;i<row1;i++)
{
  for(j=0;j<col1;j++)
  { 
    printf("%d  ",c[i][j]);
  }
printf("\n");
}
}
return 0;
}

