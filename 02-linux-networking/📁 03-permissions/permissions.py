
"""
Command: To view permissions of files and directories, we use the command
ls -l

Purpose:
Displays detailed information about files and directories, including their permissions, owner, group, file size, and last modified date.

Example:
ls -l

Example Output:
-rwxr-xr-x 1 ec2-user ec2-user 245 Jan 10 14:30 script.sh
-rw-r--r-- 1 ec2-user ec2-user 128 Jan 10 14:35 notes.txt

Understanding the Permission Format:

-rwxr-xr-x

- : File type (- = file, d = directory)
rwx : Owner permissions (Read, Write, Execute)
r-x : Group permissions (Read, Execute)
r-x : Others permissions (Read, Execute)

When I Used It:
I used the `ls -l` command on my AWS EC2 instance to check file permissions before modifying them with the `chmod` command and to verify the owner and access rights of files and directories.
"""