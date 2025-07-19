#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<arpa/inet.h>

void list_connected_wifi(const char *server_name){
    FILE *fp;
    char command[100];
    snprintf(command,sizeof(command),"iw dev %s station dump",server_name);
    fp = popen(command,"r");
    
    if(fp == NULL) printf("Command run failed\n");
    while (fgets())
    {
        
    }
    
}

int main(){
    list_connected_wifi("wlx98ba5fece6d3");
}