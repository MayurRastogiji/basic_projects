#include<stdio.h>
#include<complex.h>
#include<math.h>
int a,b,c,d,dis;
float root1,root2,imag;
int calculator()
{
    printf("enter digits you want to do mathematical operation on:\n");
    scanf("%d%d",&a,&b);
    switch (d)
    {
    case 1:
        d=a+b;
        printf("addition of %d and %d is : %d",a,b,d);
        break;
    case 2:
        d=a*b;
        printf("multiplication of %d and %d is : %d",a,b,d);
        break;
    case 3:
        d=a/b;
        printf("division of %d and %d is: %d",a,b,d);
        break;
    case 4:
        d=a-b;
        printf("subtraction of %d and %d is : %d",a,b,d);
        break;
    default:
        printf("wrong input");
        break;
    }
    return 0;
}
int equation()
{
    printf("enter value of a,b,c in eq : ax^2+bx+c \n");
    scanf("%d%d%d",&a,&b,&c);
    dis=(b*b)-4*a*c;
    root1= (-b+csqrt(dis))/2*a;
    root2= (-b-csqrt(dis))/2*a;
    imag= (dis)/2*a;
    printf("discriminant is : %d\n",dis);
    if (dis > 0)
    {
        printf("roots are real and distinct\n");
        printf("the root1 = %f and root2 = %f",creal(root1),creal(root2));
    }
    else
    {
        if(dis < 0)
        {
            printf("roots are imaginary and distinct\n");
            printf("the root1 = %f +i%f \n root2 = %f + i%f",creal(root1),imag,creal(root2),imag);
        }
        else
        {
            printf("roots are real and same \n");
            printf("root1 = %f \n root2 = %f",creal(root1),creal(root2));
        }
    }
    return 0;
}
int main()
{
    printf("enter \n 1 for addition:\n 2 for multiplication: \n 3 for division: \n 4 for subtraction: \n 5 for finding roots of qadratic eqiation:\n");
    scanf("%d",&d);
    if (d<=4)
    {
        calculator();
    }
    else
    {
        equation();
    }
    printf("\nJAI SHRI RAM \n");
    return 0;
}
