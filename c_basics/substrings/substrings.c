/**
 * @file substrings.c
 * @version 1.0
 * @author Daniel Cohen Hillel, ID: 212553804
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
#include <string.h>

// ------------------------------ functions -----------------------------
char * my_strstr(const char * a, const char * b)
{
   for (int i=0; i < strlen(a); i++)
      for (int j=0; a[i+j]==b[j]; j++)
         if (j==strlen(b)-1)
            return (unsigned char *)a+i;
   return NULL;
}

int main(int argc, char * argv[])
{
   char s1[] = "AAAAAAACCCAAAAAAAA";
   char s2[] = "CCC";


   char * ret = my_strstr(s1, s2);

   printf("\33[1mThe substring is:\33[0m\33[35m %s\n\33[0m", ret);

   return 0;
}
