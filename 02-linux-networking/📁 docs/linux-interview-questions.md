# Linux Interview Questions

This document contains Linux interview questions that I studied while learning AI Automation Engineering and Cloud fundamentals.

---

# Level 1 — Linux Basics

### 1. What is Linux?

### 2. Why is Linux widely used on servers?

### 3. What is the Linux Kernel?

### 4. What is a Linux Distribution?

### 5. Name some popular Linux distributions.

- Ubuntu
- Debian
- Fedora
- CentOS
- Amazon Linux
- Red Hat Enterprise Linux (RHEL)

### 6. What is the difference between Linux and Windows?

### 7. What is the command line?

### 8. What is a Shell?

### 9. What is Bash?

### 10. What is a Terminal?

---

# Level 2 — File System

### 11. What does the `pwd` command do?

### 12. What is the purpose of the `ls` command?

### 13. What is the difference between `ls` and `ls -l`?

### 14. How do you change directories?

### 15. What does `cd ..` do?

### 16. What does `cd ~` do?

### 17. What is the root directory?

### 18. What is the home directory?

### 19. What is the difference between an absolute path and a relative path?

### 20. How do you create a directory?

### 21. How do you remove a directory?

### 22. How do you create a file?

### 23. How do you copy a file?

### 24. How do you move or rename a file?

### 25. How do you delete a file?

---

# Level 3 — File Permissions

### 26. What are Linux file permissions?

### 27. Explain the permission format.

```
-rwxr-xr-x
```

### 28. What do Read, Write, and Execute permissions mean?

### 29. What is the difference between Owner, Group, and Others?

### 30. What does the `chmod` command do?

### 31. What does the `chown` command do?

### 32. What is the difference between `chmod` and `chown`?

### 33. What does `755` mean?

### 34. What does `644` mean?

### 35. How do you make a script executable?

---

# Level 4 — Users & Processes

### 36. How do you check the current logged-in user?

### 37. What does the `whoami` command do?

### 38. How do you view running processes?

### 39. What is the difference between `ps` and `top`?

### 40. How do you stop a running process?

### 41. What is a Process ID (PID)?

### 42. What is the purpose of the `kill` command?

### 43. What is `systemctl` used for?

---

# Level 5 — Networking

### 44. What is an IP address?

### 45. What is a Public IP?

### 46. What is a Private IP?

### 47. What is DNS?

### 48. What happens when you type google.com into a browser?

### 49. What is HTTP?

### 50. What is HTTPS?

### 51. What is the difference between HTTP and HTTPS?

### 52. What is SSH?

### 53. Why is SSH used?

### 54. What does the `ping` command do?

### 55. What does `curl` do?

### 56. What is `wget` used for?

### 57. What does `ip addr` show?

### 58. What is a Port?

### 59. What are Ports 22, 80, and 443 used for?

### 60. What is the difference between TCP and UDP?

---

# Level 6 — AWS & Linux

### 61. What is Amazon EC2?

### 62. Why is Linux commonly used on EC2 instances?

### 63. How do you connect to an EC2 instance?

### 64. What is an SSH Key Pair?

### 65. What happens if you lose your private key?

### 66. Why should private keys never be shared?

---

# Level 7 — Bash & Scripting

### 67. What is a Shell Script?

### 68. What is the purpose of the Shebang (`#!/bin/bash`)?

### 69. How do you run a Bash script?

### 70. How do you make a Bash script executable?

### 71. What are environment variables?

### 72. What is the PATH variable?

---

# Level 8 — AI Automation & DevOps

### 73. Why do AI Engineers need Linux?

### 74. Why do Docker containers usually run Linux?

### 75. Why do cloud servers mostly use Linux?

### 76. How does Python interact with Linux?

### 77. Why are command-line skills important for automation?

### 78. Why are environment variables used for API keys?

### 79. How would you deploy a Python application on a Linux server?

### 80. What Linux skills are most important for AI Automation Engineers?

---

# Hands-on Questions

Be prepared to demonstrate these tasks:

- Navigate to another directory.
- Create a new folder.
- Create a file.
- Copy a file.
- Rename a file.
- Delete a file.
- Display file contents.
- Change file permissions.
- Make a script executable.
- Connect to an EC2 instance.
- Check your current IP address.
- Download a file using `wget`.
- Retrieve data using `curl`.
- View running processes.
- Stop a process.
- Display file permissions.
- Explain the difference between relative and absolute paths.

---

# Common Interview Scenarios

### Scenario 1

You receive a "Permission denied" error while trying to execute a script.

- How would you investigate?
- Which commands would you use?

---

### Scenario 2

A Python application cannot connect to an API hosted on another server.

- What networking checks would you perform?

---

### Scenario 3

Your application is running slowly on a Linux server.

- How would you inspect running processes?

---

### Scenario 4

You accidentally deleted an important file.

- What steps would you take?

---

### Scenario 5

You need to securely connect to a remote Linux server.

- Which command would you use?
- Why is SSH preferred over Telnet?