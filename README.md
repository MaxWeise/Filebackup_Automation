
# Backup Automation Script
This script is used to backup files (recursivley) either to a harddrive or a NAS

Feel free to clone this repo and use / experiment with the code
but please mention my name and the repo in the docstring.
Thanks

# How to use it
The script runs on Python 3, so be sure to have it installed. It can be run by './main.py' (PowerShell) or 'python main.py' (Bash).

## CMD Interface
The script will run in an infinite loop, until an 'x' is given as command.
There exist 3 commands to use in the loop:
 * file backup: Specifiy a root directory and a destination directory. All files and directories will get copied recursively from root to destination.
 * file type backup: In addition to root and dest, specify a number of filetypes (i.e.: txt, py, c, json). All other filetypes will sorted into a 'dump directory' and (after confirmation) this directory will get deleted. The remaining directory structure will get copied.
 * help: A list including all commands and a short description.


