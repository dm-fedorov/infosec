#include <stdio.h>
#include <string.h>

void vuln_func(char *data) { 
  char buff[256]; 
  strcpy(buff, data); 
} 

void main(int argc, char *argv[]) {
  vuln_func(argv[1]);
} 
