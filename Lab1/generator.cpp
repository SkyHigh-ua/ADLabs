#pragma once
#include <iostream>
#include <fstream>
#include <random>

void generator(long ramsize)
{
    FILE *file = fopen("array.txt", "w");
    long size = 0, num;
    while (size < ramsize*2){
        num = rand();
        fprintf(file, "%ld\n", num);
        size += sizeof(num);
    }
    fclose(file);
}
