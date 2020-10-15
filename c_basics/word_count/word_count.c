/**
 * @file word_count.c
 * @version 1.0
 * @author Daniel Cohen Hillel, ID: 212553804
 *
 * @brief program that print how many words are in a given file.
 *
 * @section LICENSE
 * This program is part of the Black-Biss;
 * ANY USE OF THE PROGRAM OR THE SOURCE CODE WITHOUT THE BLACK-BISS AGREEMENT IS FORBIDDEN.
 *
 * @section DESCRIPTION
 * The system get file path as argument. Open it and count the word's in it.
 * Input  : file_path
 * Output : print out the amount of words.
 */


// ------------------------------ includes ------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <regex.h>

// ------------------------------ functions -----------------------------
int main(int argc, char * argv[])
{
    size_t word_count = 0;
    // you can add more initial checks
    if (argc < 2)
    {
        printf("missing file_path parameter.\n");
        return EXIT_FAILURE;
    }

    // open the file
    char buff[255];
    FILE *fp;
    fp = fopen(argv[1], "r");

    // loop over all the words
    while (fscanf(fp, "%s", buff)==1)
        word_count++;

    fclose(fp);

    printf("The file %s contains \33[35m%zu\33[0m words.\n", argv[1], word_count);

	return 0;
}
