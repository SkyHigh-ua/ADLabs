#include <fstream>
#include <vector>
#include <algorithm>
#include "generator.cpp"
class ENMSort
{
private:
    const char *initialfile;
    const char *file1;
    const char *file2;
    const char *file3;
    const char *file4;
    long ramsize;
public:
    ENMSort(const char *filename, const char *file1, const char *file2, const char *file3, const char *file4, long ramsize);
    void writenum(FILE* fileA, FILE* fileB, std::vector<long> nums, int runcount);
    std::vector<long> split_file();
    void mergeruns(std::vector<long> runs);
    void merge(FILE* file, FILE* fileA, FILE* fileB, long numA, long numB);
    std::vector<long> identifyrun(FILE* file);
};

ENMSort::ENMSort(const char *filename, const char *file1, const char *file2, const char *file3, const char *file4, long ramsize)
{
    this->ramsize = ramsize;
    this->initialfile = filename;
    this->file1 = file1;
    this->file2 = file2;
    this->file3 = file3;
    this->file4 = file4;
    this->mergeruns(this->split_file());
}

void ENMSort::writenum(FILE* fileA, FILE* fileB, std::vector<long> nums, int runcount){
    if (runcount%2 == 0)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            fprintf(fileB, "%ld\n", nums[i]);
        }
    }
    else
    {
        for (int i = 0; i < nums.size(); i++)
        {
            fprintf(fileA, "%ld\n", nums[i]);
        }
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
    std::vector<long> newruns;
    long num;
    bool swtch = true;
    while (runs.size() > 2)
    {
        newruns.clear();
        FILE* fileA = swtch ? fopen(this->file1, "r") : fopen(this->file3, "r");
        FILE* fileB = swtch ? fopen(this->file2, "r") : fopen(this->file4, "r");
        FILE* fileC = swtch ? fopen(this->file3, "w") : fopen(this->file1, "w");
        FILE* fileD = swtch ? fopen(this->file4, "w") : fopen(this->file2, "w");
        for (int i = 0; i < runs.size() - 1; i += 2)
        {
            if ((i/2+1)%2 == 0)
            {
                merge(fileD, fileA, fileB, runs[i], runs[i+1]);
            }
            else
            {
                merge(fileC, fileA, fileB, runs[i], runs[i+1]);
            }
            newruns.push_back(runs[i]+runs[i+1]);
        }
        if (runs.size()%2 == 1 && runs.size() != 3)
        {
            for (int i = 0; i < runs[runs.size() - 1]; i++)
            {
                fscanf(fileA, "%ld", &num);
                fprintf(newruns.size()%2 == 0 ? fileC : fileD, "%ld\n", num);
            }
            newruns.push_back(runs[runs.size() - 1]);
        }
        else if (runs.size() == 3){
            for (int i = 0; i < runs[runs.size() - 1]; i++)
            {
                fscanf(fileA, "%ld", &num);
                fprintf(fileD, "%ld\n", num);
            }
            newruns.push_back(runs[runs.size() - 1]);
        }
        runs = newruns;
        swtch = swtch ? false : true;
        fclose(fileA);
        fclose(fileB);
        fclose(fileC);
        fclose(fileD);
    }
    if (swtch)
    {
        merge(fopen(this->initialfile, "w"), fopen(this->file1, "r"), fopen(this->file2, "r"), runs[0], runs[1]);
    }
    else
    {
        merge(fopen(this->initialfile, "w"), fopen(this->file3, "r"), fopen(this->file4, "r"), runs[0], runs[1]);
    }
    
}

std::vector<long> ENMSort::split_file(){
    std::vector<long> runs, buffer;
    unsigned long sizeoflong = sizeof(long), sizeofvector = sizeof(std::vector<long>);
    runs.push_back(0);
    int index = runs.size()-1;
    long prev_num, num, prev_run_num=-1, ramsize = this->ramsize/32;
    bool readble = true, sorted;
    FILE* file = fopen(this->initialfile, "r");
    FILE* fileA = fopen(this->file1, "w");
    FILE* fileB = fopen(this->file2, "w");
    while (readble){
        sorted = true;
        buffer.clear();
        while (sizeofvector + (sizeoflong * buffer.size()) < ramsize && readble)
        {
            if (fscanf(file, "%ld", &num) == 1){
                if (buffer.size()>0){
                    if (buffer[buffer.size()-1]>num && sorted){
                        sorted = false;
                    }
                }
                buffer.push_back(num);
            }
            else {
                readble = false;
            }
        }
        if (!sorted){
            std::sort(buffer.begin(), buffer.end());
        }
        if (runs[index]>0)
        {
            if (prev_run_num <= buffer[0] && prev_run_num != -1){
                if (index == runs.size() - 2){
                    index = runs.size() - 1;
                }
                else{
                    index = runs.size() - 2;
                }
                runs[index] = buffer.size();
            }
            else {
                runs.push_back(buffer.size());
                index = runs.size() - 1;
            }
            prev_run_num = buffer[buffer.size()-1];
            writenum(fileA, fileB, buffer, index+1);
        }
        else
        {
            runs[index] = buffer.size();
            writenum(fileA, fileB, buffer, index+1);
            prev_run_num = buffer[buffer.size()-1];
        }
    }
    fclose(file);
    fclose(fileA);
    fclose(fileB);
    if(runs.size()==1){
        runs.push_back(0);
    }
    return runs;
}

int main()
{
    long ramsize = 524288000;
    generator(ramsize);
    std::cout << "file generated" << std::endl;
    ENMSort temp("./array.txt", "./temp/fileA.txt", "./temp/fileB.txt", "./temp/fileC.txt", "./temp/fileD.txt", ramsize);
    return 0;
}