#include<stdio.h>
#define PI 3.142
#define area_of_circle(r) (PI*r*r)
#define surface_area_cylinder(r,h) (2*PI*r*(r+h))
int main()
{
float r,h,area,surface_area;
printf("enter the radius ");
scanf("%f",&r);
printf("enter the height of cylinder");
scanf("%f",&h);
area=area_of_circle(r);
surface_area=surface_area_cylinder(r,h);
printf("the area of circle is %f\n",area);
printf("the surface area of cylinder is %f",surface_area);
return 0;
}
