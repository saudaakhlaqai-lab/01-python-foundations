# Linux Interview Answers – Part 2

This document contains interview-ready answers covering Linux processes, networking, AWS EC2, Bash scripting, and Linux concepts relevant to AI Automation Engineering.

---

# Processes

## 36. How do you check the current logged-in user?

Use:

```bash
whoami
```

Example Output:

```text
ec2-user
```

This command displays the username of the currently logged-in user.

---

## 37. What does the `whoami` command do?

The `whoami` command prints the username of the current user. It is useful for verifying which account is executing commands.

---

## 38. How do you view running processes?

Use:

```bash
ps
```

or

```bash
ps -ef
```

For real-time monitoring:

```bash
top
```

---

## 39. What is the difference between `ps` and `top`?

- `ps` shows a snapshot of currently running processes.
- `top` continuously updates and displays CPU, memory, and running processes in real time.

---

## 40. How do you stop a running process?

Use:

```bash
kill PID
```

Example:

```bash
kill 1234
```

If the process doesn't stop:

```bash
kill -9 1234
```

---

## 41. What is a Process ID (PID)?

A Process ID (PID) is a unique number assigned to every running process. It helps identify and manage processes.

---

## 42. What is the purpose of the `kill` command?

The `kill` command sends a signal to terminate or control a running process.

---

## 43. What is `systemctl` used for?

`systemctl` is used to manage services in Linux.

Examples:

```bash
systemctl status sshd
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
```

---

# Networking

## 44. What is an IP address?

An IP address uniquely identifies a device on a network so it can communicate with other devices.

---

## 45. What is a Public IP?

A Public IP is accessible over the internet and is used to communicate with devices outside a private network.

---

## 46. What is a Private IP?

A Private IP is used within a local network and cannot be accessed directly from the internet.

---

## 47. What is DNS?

DNS (Domain Name System) translates domain names like:

```text
google.com
```

into IP addresses that computers understand.

---

## 48. What happens when you type google.com into a browser?

1. The browser asks DNS for Google's IP address.
2. DNS returns the IP address.
3. The browser sends an HTTPS request.
4. Google's server responds.
5. The webpage loads.

---

## 49. What is HTTP?

HTTP (HyperText Transfer Protocol) is used for communication between web browsers and web servers.

Default Port:

```text
80
```

---

## 50. What is HTTPS?

HTTPS is the secure version of HTTP. It encrypts data exchanged between the client and server using SSL/TLS.

Default Port:

```text
443
```

---

## 51. What is the difference between HTTP and HTTPS?

| HTTP | HTTPS |
|------|-------|
| Not encrypted | Encrypted |
| Port 80 | Port 443 |
| Less secure | More secure |

---

## 52. What is SSH?

SSH (Secure Shell) is a secure protocol used to remotely access Linux servers.

Default Port:

```text
22
```

---

## 53. Why is SSH used?

SSH provides encrypted communication for securely managing remote servers.

---

## 54. What does the `ping` command do?

`ping` checks whether another device or server is reachable and measures network latency.

Example:

```bash
ping google.com
```

---

## 55. What does `curl` do?

`curl` sends HTTP requests and retrieves data from APIs or websites.

Example:

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

---

## 56. What is `wget` used for?

`wget` downloads files from the internet using the command line.

Example:

```bash
wget https://example.com/file.zip
```

---

## 57. What does `ip addr` show?

It displays network interface information, including IP addresses assigned to the system.

---

## 58. What is a Port?

A port is a communication endpoint used by applications to send and receive network traffic.

---

## 59. What are Ports 22, 80, and 443 used for?

- Port 22 → SSH
- Port 80 → HTTP
- Port 443 → HTTPS

---

## 60. What is the difference between TCP and UDP?

**TCP**
- Reliable
- Connection-oriented
- Guarantees packet delivery

**UDP**
- Faster
- Connectionless
- Does not guarantee delivery

---

# AWS EC2

## 61. What is Amazon EC2?

Amazon EC2 (Elastic Compute Cloud) is a service that provides virtual servers in the cloud.

---

## 62. Why is Linux commonly used on EC2 instances?

Linux is lightweight, secure, stable, and widely supported. Most cloud workloads and web applications run on Linux.

---

## 63. How do you connect to an EC2 instance?

Using SSH:

```bash
ssh -i key.pem ec2-user@public-ip
```

Or by using AWS EC2 Instance Connect.

---

## 64. What is an SSH Key Pair?

An SSH key pair consists of:
- Public Key
- Private Key

The public key is stored on the server, while the private key remains with the user and is used for authentication.

---

## 65. What happens if you lose your private key?

You may lose access to the EC2 instance unless another authentication method or recovery option is available.

---

## 66. Why should private keys never be shared?

Anyone with your private key may be able to access your server. Private keys should always be kept secure.

---

# Bash Scripting

## 67. What is a Shell Script?

A shell script is a text file containing Linux commands that can be executed automatically.

---

## 68. What is the purpose of the Shebang (`#!/bin/bash`)?

The shebang tells Linux which interpreter should execute the script.

Example:

```bash
#!/bin/bash
```

---

## 69. How do you run a Bash script?

```bash
bash script.sh
```

or

```bash
./script.sh
```

(after making it executable)

---

## 70. How do you make a Bash script executable?

```bash
chmod +x script.sh
```

---

## 71. What are environment variables?

Environment variables store configuration values such as API keys, usernames, or file paths that applications can access.

Example:

```bash
echo $HOME
```

---

## 72. What is the PATH variable?

`PATH` is an environment variable that tells Linux where to look for executable programs when you type a command.

---

# Linux for AI Automation

## 73. Why do AI Engineers need Linux?

Most AI applications are developed, tested, and deployed on Linux servers or cloud platforms. Linux skills help engineers manage servers, automate tasks, and deploy applications.

---

## 74. Why do Docker containers usually run Linux?

Docker uses Linux kernel features such as namespaces and cgroups, making Linux the most common environment for containers.

---

## 75. Why do cloud servers mostly use Linux?

Linux is stable, efficient, open source, and well-supported by cloud providers like AWS, Azure, and Google Cloud.

---

## 76. How does Python interact with Linux?

Python can automate Linux tasks, execute shell commands, manage files, communicate with APIs, and deploy applications.

---

## 77. Why are command-line skills important for automation?

Many automation tasks run without a graphical interface. Command-line skills allow engineers to write scripts, schedule jobs, and manage remote servers efficiently.

---

## 78. Why are environment variables used for API keys?

Environment variables keep sensitive information out of source code, reducing the risk of exposing credentials in Git repositories.

---

## 79. How would you deploy a Python application on a Linux server?

Typical steps:

1. Connect to the server using SSH.
2. Install Python and dependencies.
3. Clone the project from GitHub.
4. Install required packages.
5. Configure environment variables.
6. Run the application or configure it as a service.

---

## 80. What Linux skills are most important for AI Automation Engineers?

- Linux command line
- File management
- Permissions
- SSH
- Networking basics
- Bash scripting
- Environment variables
- Process management
- Cloud server administration