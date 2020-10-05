/**
 * @file getline.c
 * @version 1.0
 * @author ????????
 *
 * @brief program that read lines from FILE (file or stdin).
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
size_t my_getline(char ** lineptr, size_t * n, FILE * stream)
{
    return 0;
}

int main()
{
    char * buffer;
    size_t bufsize = 32;
    size_t characters;

    buffer = (char *) malloc(bufsize * sizeof(char));
    if( buffer == NULL)
    {
        perror("Unable to allocate buffer");
        exit(1);
    }

    printf("Type something: ");
    characters = my_getline(&buffer, &bufsize, stdin);
    printf("%zu characters were read.\n", characters);
    printf("You typed: '%s'\n", buffer);

    return(0);
}