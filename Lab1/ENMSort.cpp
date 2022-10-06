#include <fstream>
#include <vector>
#include "generator.cpp"
class ENMSort
{
private:
    const char *initialfile;
    const char *file1;
    const char *file2;
public:
    ENMSort(const char *filename, const char *file1, const char *file2);
    void writenum(FILE* fileA, FILE* fileB, long num, int runcount);
    std::vector<long> split_file();
    void mergeruns(std::vector<long> runs);
    void merge(FILE* file, FILE* fileA, FILE* fileB, long numA, long numB);
    std::vector<long> identifyrun(FILE* file);
};

ENMSort::ENMSort(const char *filename, const char *file1, const char *file2)
{
    this->initialfile = filename;
    this->file1 = file1;
    this->file2 = file2;
    this->mergeruns(this->split_file());
}

void ENMSort::writenum(FILE* fileA, FILE* fileB, long num, int runcount){
    if (runcount%2 == 0)
    {
        fprintf(fileB, "%ld\n", num);
    }
    else
    {
        fprintf(fileA, "%ld\n", num);
    }
}

void ENMSort::merge(FILE* file, FILE* fileA, FILE* fileB, long numA, long numB){
    long num1, num2;
    fscanf(fileA, "%ld", &num1);
    fscanf(fileB, "%ld", &num2);
    int i = 1, j = 1;
    while (i <= numA && j<=numB)
    {
        if (num1 < num2){
            fprintf(file, "%ld\n", num1);
            if (i < numA)
            {
                fscanf(fileA, "%ld", &num1);
            }
            i++;
        }
        else if (num1 == num2){
            fprintf(file, "%ld\n", num1);
            fprintf(file, "%ld\n", num2);
            if (i < numA)
            {
                fscanf(fileA, "%ld", &num1);
            }
            if (j < numB)
            {
                fscanf(fileB, "%ld", &num2);
            }
            i++;
            j++;
        }
        else{
            fprintf(file, "%ld\n", num2);
            if (j < numB)
            {
                fscanf(fileB, "%ld", &num2);
            }
            j++;
        }
    }
    while (i <= numA)
    {
        fprintf(file, "%ld\n", num1);
        if (i < numA)
        {
            fscanf(fileA, "%ld", &num1);
        }
        i++;
    }
    while (j <= numB)
    {
        fprintf(file, "%ld\n", num2);
        if (j < numB)
        {
            fscanf(fileB, "%ld", &num2);
        }
        j++;
    }
}

void ENMSort::mergeruns(std::vector<long> runs){
    long num;
    while (runs.size() > 1)
    {
        FILE* file = fopen(this->initialfile, "w");
        FILE* fileA = fopen(this->file1, "r");
        FILE* fileB = fopen(this->file2, "r");
        for (int i = 0; i < runs.size() - 1; i += 2)
        {
            merge(file, fileA, fileB, runs[i], runs[i + 1]);
        }
        if (runs.size()%2 == 1)
        {
            for (int i = 0; i < runs[runs.size() - 1]; i++)
            {
                fscanf(fileA, "%ld", &num);
                fprintf(file, "%ld\n", num);
            }
        }
        fclose(file);
        fclose(fileA);
        fclose(fileB);
        runs = split_file();
    }
}

std::vector<long> ENMSort::split_file(){
    std::vector<long> runs;
    runs.push_back(0);
    int index = runs.size()-1;
    long prev_num, num, prev_run_num=-1;
    FILE* file = fopen(this->initialfile, "r");
    FILE* fileA = fopen(this->file1, "w");
    FILE* fileB = fopen(this->file2, "w");
    while (fscanf(file, "%ld", &num) == 1){
        if (runs[index]>0)
        {
            if (prev_num <= num)
            {
                runs[index]++;
                writenum(fileA, fileB, num, index+1);
                prev_num = num;
            }
            else
            {
                if (prev_run_num <= num && prev_run_num != -1){
                    if (index == runs.size() - 2){
                        index = runs.size() - 1;
                    }
                    else{
                        index = runs.size() - 2;
                    }
                    runs[index]++;
                    prev_run_num = prev_num;
                }
                else {
                    runs.push_back(1);
                    index = runs.size() - 1;
                    prev_run_num = prev_num;
                }
                writenum(fileA, fileB, num, index+1);
                prev_num = num;
            }
        }
        else
        {
            runs[index]++;
            writenum(fileA, fileB, num, index+1);
            prev_num = num;
        }
    }
    fclose(file);
    fclose(fileA);
    fclose(fileB);
    return runs;
}

int main()
{
    long ramsize = 524288000/64;
    generator(ramsize);
    printf("Time taken: file generated\n");
    clock_t tStart = clock();
    ENMSort temp("./array.txt", "./temp/fileA.txt", "./temp/fileB.txt");
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}