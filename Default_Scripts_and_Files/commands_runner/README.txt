Info:
Very simple tool to run basic commands by just copy paste of files with the command line, into the shared space.
A simple reboot or shutdown without having to SSH.

This tool is auto started by the startup.sh script. If unwated, simply comment the setup line.


Usage:
1) Simply copy / past the desired file to the Scripts shared folder.
2) The commands runner will pick it up and run it.
3) The file will always be removed as the command is executed.
4) The command output is concatenated to the file "simple.command.out.txt" created in the Scripts folder.
