# Lab 02 - Connect to an EC2 Instance

## Objective

Connect to a running EC2 instance using AWS CloudShell.

---

## Steps

### Step 1

Open the EC2 Dashboard.

---

### Step 2

Select your running instance.

---

### Step 3

Click **Connect**.

---

### Step 4

Choose the **EC2 Instance Connect** or **CloudShell** option.

---

### Step 5

Connect to the server.

You should see something similar to:

```bash
[ec2-user@ip-172-31-47-65 ~]$
```

---

### Step 6

Verify your current user.

```bash
whoami
```

Example Output

```text
ec2-user
```

---

### Step 7

Check your current directory.

```bash
pwd
```

Example Output

```text
/home/ec2-user
```

---

## Skills Practiced

- Connecting to Linux servers
- Using CloudShell
- Verifying the logged-in user