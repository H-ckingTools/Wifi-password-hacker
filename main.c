#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<arpa/inet.h>

struct connected {
    char IP[20];
    char HW_type[10];
    char Flag[10];
    char Mac[30];
    char Mask[10];
    char Device_name[30];
};

void list_connected_wifi(){
    FILE *fp;
    char line[100];
    struct connected con_dev;
    fp = fopen("/proc/net/arp","r");
    if(fp == NULL) perror("File not opened");
    //Skip title or header section
    fgets(line,sizeof(line),fp);
    while(fgets(line,sizeof(line),fp)){
        sscanf(line,"%s %s %s %s %c %s",con_dev.IP,con_dev.HW_type,con_dev.Flag,con_dev.Mac,con_dev.Mask,con_dev.Device_name);
        printf("Connnected device : \n\n");
        printf("Device name : %s\n",con_dev.Device_name);
        printf("Device Ip : %s\n",con_dev.IP);
    }

    int sock;
    struct sockaddr_in server;

    // Create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("Socket creation failed");

    }

    // Server info
    server.sin_family = AF_INET;
    server.sin_port = htons(1234);
    server.sin_addr.s_addr = inet_addr("192.168.37.13");

    // Connect to server
    if (connect(sock, (struct sockaddr*)&server, sizeof(server)) < 0) {
        perror("Connection failed");
        close(sock);
    }

    printf("Connected successfully!\n");
    close(sock);
}

int main(){
    list_connected_wifi();
}