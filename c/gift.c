#include<stdio.h>


int main(int argc, char const *argv[])
{
    int a,b,c,d;
    printf("what are your marks in maths\n",a);
    scanf("%d",&a);
    printf("what are your marks in science\n",b);
    scanf("%d",&b);
    c = a+b;
    d = c/2;
    printf("your total number is = %d\n",c);
    printf("your average is = %d\n",d);
    if (a>=60)
    {   if (b>=60)
    {
        printf("you are pass in both exams\n you get a reward of RS45");
    }
        else{
        printf("you are pass in maths\n you get a reward of RS15");
        }
        }
    else{
        if (b>=60)
        {
            printf("you are pass in science\n you get a reward of RS15");
        }
        else{
            printf("you are fail\n you need to work hard");
        }
    }
    
    return 0;
}
