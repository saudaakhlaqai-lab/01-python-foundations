# Lab 05 - Networking Commands

## Objective

Practice basic networking commands used on Linux systems.

---

## Step 1

Check connectivity.

```bash
ping google.com
```

Example Output

```text
64 bytes from ...
```

---

## Step 2

Retrieve data from a website.

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

---

## Step 3

Download a file.

```bash
wget https://example.com
```

---

## Step 4

Display IP address information.

```bash
ip addr
```

---

## Step 5

Connect to a remote server.

```bash
ssh ec2-user@your-public-ip
```

---

## Step 6

Display listening network connections.

```bash
netstat -tuln
```

*(in case of `netstat` is unavailable on your Linux distribution, use `ss -tuln` instead.)*

---

## Skills Practiced

- ping
- curl
- wget
- ip
- ssh
- netstat / ss