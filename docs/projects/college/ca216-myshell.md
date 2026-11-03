# CA216 Operating Systems: myshell

*[GitHub Repository Link](https://github.com/CheeseLad/ca216-myshell)*

# Project Grade: 99%

NAME
      myshell

SYNOPSIS
      myshell [command_name] [arguments] [options] [file_name]

DESCRIPTION

      myshell is a fully-featured shell written in C that can execute commands, redirect input and output and execute processes in the background. It supports a variety of built-in commands as well as the ability to execute any commands installed on your system. Forking to create child processes is used throughout the shell to execute commands and handle redirection.

STARTUP

      To start myshell, just run the myshell executable file where you will be greeted with a prompt that is waiting for your input. The prompt will display the directory that you are currently in along with your username.

BUILT-IN COMMANDS

      cd [directory_name]: Change directory (If blank, your current directory will be listed)
      clr: Clear the screen
      dir [directory_name]: List the contents of the current directory (If blank, the contents of your current directory will be listed)
      environ: List all environment variables
      echo: Print a string to the console
      help: Display the user manual
      pause: Pause the shell until the user presses enter
      quit: Exit the shell
      
ENVIRONMENT

      Environment variables are used to store data about your system and it's current operating environment.
      Examples of environment variables include `HOME`, which is your home directory `USER`, which is your username `SHELL`, which is the current shell (myshell).      Each environment variable is stored in a key-value pair such as `SHELL=/myshell`, allowing the shell to easily get and set variables by their key.
      When myshell is started, a new environment variable called `SHELL` is created and set to the path where the shell executable is located.
      The command `environ` can be used to list all of the environment variables currently set on the system.
      When executing a non-built-in command, an environment variable called `PARENT` is created and links to where the shell executable is stored.

I/O REDIRECTION

      myshell takes advantage of `stdin` and `stdout` to redirect input and output to and from files. When redirecting either input or output, the shell replaces the file stream with the file that the user requests.

      Redirecting to stdout has multiple options:
            `>`: Redirects the output of a command to a file, overwriting the file if it already exists, the file will be created if it does not exist
                  Example: `ls > file.txt`
            `>>`: Redirects the output of a command to a file, appending to the file if it already exists, the file will be created if it does not exist
                  Example: `ls >> file.txt`

      Redirecting to stdin has one option:
            `<`: Redirects the input of a command to a file
                  Example: `cat < file.txt`
            
      Error handling is in place for both redirections, alerting the user if the file does not exist or cannot be opened.

      The following internal commands can be redirected to stdout:
            `dir`, `environ`, `echo`, `help`

PROCESS CONCEPT

      When you launch myshell, you create a shell process in the foreground and this process will be the parent process for any external commands ran inside the shell.
      When executing internal commands, the command processing will be carried out within the shell process.
      When executing external commands, the shell will fork a child process to execute the command. This child process will be completely independent of the shell process with the shell waiting for the child process to complete before displaying the shell prompt again.

      Background processes can be executed by adding an `&` to the end of the command you want to run.
      Foreground processes are just ran by typing the command as normal.
      The difference between them is that foreground processes will wait for the shell to finish running the command where as background processes will create a fork and run the command elsewhere, displaying the shell prompt instantly to the user. This can be beneficial if the command you want to use will take a while to process.

REFERENCES

      [1] B. Fox and C. Ramey, “Bash(1): GNU bourne-again shell - linux man page,” bash(1): GNU Bourne-Again SHell - Linux man page, https://linux.die.net/man/1/bash (accessed Mar. 23, 2024). 

      [2] A. Silberschatz, P. B. Galvin, and G. Gagne, Operating System Concepts. Hoboken, NJ: Wiley, 2018. 
      
      [3] W. Joy, An Introduction to the C Shell. Berkeley, CA: University of California, Berkeley, 1980. 
      
      [4] S. Moritsugu, Practical Unix. Que, 2000. 

AUTHOR

      Name: Jake Farrell
      Student Number: 22XXXXXX
      I acknowledge the DCU Academic Integrity Policy in this submitted work
