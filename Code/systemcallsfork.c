#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

int main() {
    // Process-related system calls: fork and wait
    pid_t pid;

    pid = fork(); // Create a child process

    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) {
        // This code runs in the child process
        printf("Child process (PID: %d)\n", getpid());

        // File-related system calls: open, write, close
        int fd;
        fd = open("child.txt", O_CREAT | O_WRONLY | O_TRUNC, 0644);

        if (fd == -1) {
            perror("open");
            exit(EXIT_FAILURE);
        }

        char *message = "Hello from the child process!\n";
        ssize_t bytes_written = write(fd, message, strlen(message));

        if (bytes_written == -1) {
            perror("write");
            exit(EXIT_FAILURE);
        }

        close(fd);

        exit(EXIT_SUCCESS);
    } else {
        // This code runs in the parent process
        printf("Parent process (PID: %d)\n", getpid());

        int status;
        wait(&status); // Wait for the child to finish

        if (WIFEXITED(status)) {
            printf("Child process exited with status %d\n", WEXITSTATUS(status));
        }
    }

    // File-related system calls: open, read, close in the parent
    int fd;
    fd = open("child.txt", O_RDONLY);

    if (fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    char buffer[100];
    ssize_t bytes_read = read(fd, buffer, sizeof(buffer));

    if (bytes_read == -1) {
        perror("read");
        exit(EXIT_FAILURE);
    }

    printf("Read from file:\n%s", buffer);

    close(fd);

    return 0;
}

