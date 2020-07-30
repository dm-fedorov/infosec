#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <errno.h>

void main() {
  char *data = malloc(0x100);
  sleep(1);

  printf("\nProcess ID : %d", getpid());
  printf("\nStart of region memory : %p\n", data);

  sleep(1);

  printf("\nPress any key to change page permissions");
  getchar();

  if (mprotect((void *)((unsigned int)data & ~(0x1000 - 1)), 
    0x1000, PROT_READ | PROT_WRITE | PROT_EXEC)) {
    printf("\nERROR: mprotect returns: %d\n\n", errno);
  } else {
    printf("\nPress any key to exit"); 
    getchar();
  }
  printf("\n");
  free(data);
}