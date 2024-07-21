#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <dos.h>
#include <conio.h>
#include <windows.h>
#include"color.c"
int main()
{
    int in, se, o;
    static int points = 0, pc = 0;
    int a[13];
    printf(WHITEBACKGROUND);
    printf(BLUE);
    printf("hey user\n enter your gaming name of maximum 12 characters :\n");
    scanf("%s", &a);
    printf("welcome %s into rock , paper & scissor game\n", a);
again:
    printf(WHITEBACKGROUND);
    printf(BLUE);
    int i = 0;
    while (i < 3)
    {
        printf(BLUE);
        i++;
        printf("%s select\n 0. for rock\n 1. for paper\n 2.for scissors\n", a);
        scanf("%d", &in);
        printf(GREEN);
        switch (in)
        {
        case 0:
            char b[9] = "rock";
            printf("%s\n\n", b);
            break;
        case 1:
            char c[9] = "paper";
            printf("%s\n\n", c);
            break;
        case 2:
            char d[9] = "scissors";
            printf("%s\n\n", d);
            break;

        default:
            printf("invalid inpur:\n");
            break;
        }
        srand(time(NULL));
        se = (rand() % 3);
        printf(RED);
        switch (se)
        {
        case 0:
            char b[9] = "rock";
            printf("%s\n\n", b);
            break;
        case 1:
            char c[9] = "paper";
            printf("%s\n\n", c);
            break;
        case 2:
            char d[9] = "scissors";
            printf("%s\n\n", d);
            break;

        default:
            printf("invalid inpur:\n");
            break;
        }
        printf(BLUE);
        if (in == se)
        {
            printf("tie\n");
            continue;
        }
        else if (in == 0 && se == 1)
        {
            printf(RED);
            printf("computer wins:\n");
            pc++;
            continue;
        }
        else if (in == 0 && se == 2)
        {
            printf(GREEN);
            printf("%s wins\n", a);
            points++;
            continue;
        }
        else if (in == 1 && se == 0)
        {
            printf(GREEN);
            printf("%s wins\n", a);
            points++;
            continue;
        }
        else if (in == 1 && se == 2)
        {
            printf(RED);
            printf("computer wins\n");
            pc++;
            continue;
        }
        else if (in == 2 && se == 0)
        {
            printf(RED);
            printf("computer wins\n");
            pc++;
            continue;
        }
        else if (in == 2 && se == 1)
        {
            printf(GREEN);
            printf("%s wins\n", a);
            points++;
            continue;
        }
    }
    printf(MAGENTA);
    if (points == pc)
    {
        printf("\nmatch tie\n");
        printf("points are %d-%d\n", points, pc);
    }
    else if (points < pc)
    {
        printf("\ncomuter wins\n");
        printf("points of computer are %d\n", pc);
        printf("points of %s are %d\n", a, points);
    }
    else
    {
        printf("\n%s wins\n", a);
        printf("points of %s are %d\n", a, points);
        printf("points of computer are %d\n", pc);
    }
    printf(SIMPLE);
    printf("for play once again type 1\nfor exit type 0\n");
    scanf("%d", &o);
    if (o == 1)
    {
        goto again;
    }
    if (o == 0)
    {
        goto end;
    }
    else
    {
        printf("invalid input:\n");
        goto end;
    }

end:
    printf("we hope you enjoy playing this game :\nhave a nice day\n.");

    return 0;
}