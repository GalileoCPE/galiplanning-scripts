#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int
main(int argc, char *argv[])
{
char *newenviron[] = { NULL };
char * newargv[] = {NULL, "start", "-a", "container-anglais", NULL};
char * exec="/usr/bin/docker";

newargv[0] = exec;

execve(exec, newargv, newenviron);
perror("execve"); /* execve() only returns on error */
exit(EXIT_FAILURE);
}
