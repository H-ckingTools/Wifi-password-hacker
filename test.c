#include<stdio.h>
#include<string.h>
int main(){
    int i = 0;
    char *arr[100];
    char a[] = "mohamed (hathim) hunter sdf fg dfg dfg dfh dfh dhf dh dgh ghd ghd dgh ghd dgh dgh ghd gh gdh ghd dgh";
    char *b = strtok(a," ");
    while(b != NULL){
        arr[i++] = b;
        b = strtok(NULL," ");
    }

    for(int j = 0;j < i;j++){
        printf("%s\n",arr[j]);
    }
}
