# Linux Interview Answers – Part 1

This document contains concise interview-ready answers for Linux fundamentals.

---

## 1. What is Linux?

Linux is an open-source operating system based on the Linux kernel. It is widely used for servers, cloud computing, software development, and embedded systems because it is secure, stable, and highly customizable.

---

## 2. Why is Linux widely used on servers?

Linux is preferred because it is reliable, secure, lightweight, cost-effective, and can efficiently handle multiple users and processes. Most cloud platforms, including AWS, Azure, and Google Cloud, support Linux servers.

---

## 3. What is the Linux Kernel?

The Linux kernel is the core component of the operating system. It manages communication between hardware and software by controlling memory, CPU, storage, devices, and system resources.

---

## 4. What is a Linux Distribution?

A Linux distribution (or distro) is a complete operating system built around the Linux kernel. It includes system utilities, package managers, and software applications.

Examples include Ubuntu, Debian, Fedora, Amazon Linux, and Red Hat Enterprise Linux.

---

## 5. Name some popular Linux distributions.

- Ubuntu
- Debian
- Fedora
- CentOS
- Amazon Linux
- Red Hat Enterprise Linux (RHEL)

---

## 6. What is the difference between Linux and Windows?

| Linux | Windows |
|--------|----------|
| Open-source | Proprietary |
| Highly customizable | Less customizable |
| Commonly used on servers | Commonly used on desktops |
| Command-line friendly | GUI-focused |

---

## 7. What is the command line?

The command line is a text-based interface that allows users to interact with the operating system by typing commands instead of using a graphical interface.

---

## 8. What is a Shell?

A shell is a program that accepts commands from the user and communicates with the operating system to execute them.

---

## 9. What is Bash?

Bash (Bourne Again Shell) is the most widely used Linux shell. It allows users to execute commands, automate tasks, and write shell scripts.

---

## 10. What is a Terminal?

A terminal is the application that provides access to the shell. You type commands into the terminal, and the shell processes them.

---

# File System

## 11. What does the `pwd` command do?

`pwd` stands for **Print Working Directory**. It displays the full path of the current directory.

Example:

```bash
pwd
```

Output:

```text
/home/ec2-user
```

---

## 12. What is the purpose of the `ls` command?

The `ls` command lists the files and directories in the current location.

---

## 13. What is the difference between `ls` and `ls -l`?

- `ls` displays only file and folder names.
- `ls -l` displays detailed information such as permissions, owner, size, and modification date.

---

## 14. How do you change directories?

Use the `cd` command.

Example:

```bash
cd Documents
```

---

## 15. What does `cd ..` do?

It moves one directory up in the folder hierarchy.

---

## 16. What does `cd ~` do?

It returns the user to their home directory.

---

## 17. What is the root directory?

The root directory (`/`) is the top-level directory in the Linux file system. All other directories branch from it.

---

## 18. What is the home directory?

The home directory is the default personal directory for a user.

Example:

```text
/home/ec2-user
```

---

## 19. What is the difference between an absolute path and a relative path?

An absolute path starts from the root directory.

Example:

```text
/home/ec2-user/Documents
```

A relative path starts from the current directory.

Example:

```text
Documents/report.txt
```

---

## 20. How do you create a directory?

Use:

```bash
mkdir project
```

This creates a directory named `project`.

---

## 21. How do you remove a directory?

For an empty directory:

```bash
rmdir project
```

For a directory with files:

```bash
rm -r project
```

---

## 22. How do you create a file?

Use:

```bash
touch notes.txt
```

---

## 23. How do you copy a file?

Use:

```bash
cp file.txt backup.txt
```

---

## 24. How do you move or rename a file?

Use:

```bash
mv old.txt new.txt
```

---

## 25. How do you delete a file?

Use:

```bash
rm notes.txt
```

---

# File Permissions

## 26. What are Linux file permissions?

File permissions determine who can read, write, or execute a file or directory. They help protect files from unauthorized access.

---

## 27. Explain the permission format.

Example:

```text
-rwxr-xr-x
```

- `-` = File
- `d` = Directory
- `r` = Read
- `w` = Write
- `x` = Execute

The permissions are grouped into:

- Owner
- Group
- Others

---

## 28. What do Read, Write, and Execute permissions mean?

- **Read (r):** View the file contents.
- **Write (w):** Modify the file.
- **Execute (x):** Run the file as a program or script.

---

## 29. What is the difference between Owner, Group, and Others?

- **Owner:** The user who owns the file.
- **Group:** Users who belong to the file's assigned group.
- **Others:** Everyone else on the system.

---

## 30. What does the `chmod` command do?

The `chmod` command changes the permissions of a file or directory.

Example:

```bash
chmod 755 script.sh
```

---

## 31. What does the `chown` command do?

The `chown` command changes the owner and/or group of a file.

Example:

```bash
sudo chown ec2-user:ec2-user file.txt
```

---

## 32. What is the difference between `chmod` and `chown`?

- `chmod` changes **permissions**.
- `chown` changes **ownership**.

---

## 33. What does `755` mean?

- Owner: Read, Write, Execute
- Group: Read, Execute
- Others: Read, Execute

---

## 34. What does `644` mean?

- Owner: Read, Write
- Group: Read
- Others: Read

This is commonly used for text and configuration files.

---

## 35. How do you make a script executable?

Use:

```bash
chmod +x script.sh
```

Then execute it:

```bash
./script.sh
```