/**
 * @file substrings.c
 * @version 1.0
 * @author ????????
 *
 * @brief program that check if one string is substring of the other and return pointer
 * to the start of the substring in the string.
 *
 * @section LICENSE
 * This program is part of the Black-Biss;
 * ANY USE OF THE PROGRAM OR THE SOURCE CODE WITHOUT THE BLACK-BISS AGREEMENT IS FORBIDDEN.
 *
 */

// ------------------------------ includes ------------------------------
#include <stdio.h>
#include <stdlib.h>

// ------------------------------ functions -----------------------------
char * my_strstr(const char * a, const char * b)
{
    return NULL;
}

int main(int argc, char * argv[])
{
   char s1[] = "AAAAAAACCCAAAAAAAA";
   char s2[] = "CCC";

   char * ret = my_strstr(s1, s2);

   printf("The substring is: %s\n", ret);

	return 0;
}