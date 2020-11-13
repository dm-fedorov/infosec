#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int a = 1;
  int b = 2;
  int c = 3;

  char str_1[15];
  char *str_2 = malloc(14 * sizeof(char));

  strcpy(str_1, "HelloFromStack");
  strcpy(str_2, "HelloFromHeap");

  printf("%s, %s - %d, %d, %d \n", str_1, str_2, a, b, c);

  free(str_2);
  return 0;
}
