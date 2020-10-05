/**
 * @file fibonacci.c
 * @version 1.0
 * @author ????????
 *
 * @brief program that calculate the n'th number of fibonacci sequence.
 *
 * @section LICENSE
 * This program is part of the Black-Biss;
 * ANY USE OF THE PROGRAM OR THE SOURCE CODE WITHOUT THE BLACK-BISS AGREEMENT IS FORBIDDEN.
 *
 * @section DESCRIPTION
 * The system get number n as argument and find the n'th value in fibonacci sequence.
 * Input  : n - number
 * Output : print out the n'th value in fibonacci sequence.
 */


// ------------------------------ includes ------------------------------
#include <stdio.h>
#include <stdlib.h>

// ------------------------------ functions -----------------------------

unsigned int find_nth_fibonacci(int n)
{
    if (n==0 || n==1)
        return 1;
    return find_nth_fibonacci(n-2) + find_nth_fibonacci(n-1);
}

int main(int argc, char * argv[])
{
    // n
    int n = 0;
    // the n'th value in fibonacci sequence
    unsigned int num = 0;

    // you can add more initial checks
    if (argc < 2)
    {
        printf("missing number parameter.\n");
        return EXIT_FAILURE;
    }

    // parse the input into number
    n = atoi(argv[1]);

    num = find_nth_fibonacci(n);

    printf("The %d'th number of fibonacci sequence is %u.\n", n, num);

	return 0;
}
