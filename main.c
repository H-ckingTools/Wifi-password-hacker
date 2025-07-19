#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<arpa/inet.h>

int find_index(const char *src,int time){
    int temp;
    int len = strlen(src);
    for(int pos = 0;pos <= len;pos++){
        if(src[pos] == ' '){
            temp++;
            if(temp == time) return pos;
        }
    }
}

void list_connected_wifi(const char *server_name){
    FILE *fp;
    char buff[3000];
    char command[100];
    char response[4000];
    snprintf(command,sizeof(command),"iw dev %s station dump",server_name);
    fp = popen(command,"r");
    
    if(fp == NULL) printf("Command run failed\n");
    while (fgets(buff,sizeof(buff),fp))
    {
        strncat(response,buff,sizeof(buff));
    }
    int i = 0;
    char *tok = strtok(response," ");
    char *hello[100];
    while(tok != NULL){
        hello[i++] = tok;
        tok = strtok(NULL," ");
    }
    printf("Finally mac address found : %s\n",hello[1]);
}

int main(){
    list_connected_wifi("wlx98ba5fece6d3");
    // printf("%d",find_index("hello this is mine fucking game"));
}