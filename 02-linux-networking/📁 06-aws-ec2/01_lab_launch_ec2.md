# Lab 01 - Launch an AWS EC2 Instance

## Objective

Launch a Linux EC2 instance using the AWS Management Console.

---

## Steps

### Step 1

Log in to your AWS Management Console.

---

### Step 2

Search for **EC2** in the AWS search bar and open the EC2 Dashboard.

---

### Step 3

Click **Launch Instance**.

---

### Step 4

Enter a name for your instance.

Example:

```
linux-practice-server
```

---

### Step 5

Choose the operating system.

Example:

```
Amazon Linux 2023 AMI
```

---

### Step 6

Choose the instance type.

```
t2.micro
```

(Free Tier Eligible)

---

### Step 7

Create or select an existing key pair.

Example:

```
linux-key.pem
```

---

### Step 8

Leave the default storage settings.

```
8 GB
```

---

### Step 9

Click **Launch Instance**.

---

## Expected Result

Your EC2 instance should enter the **Running** state.

---

## Skills Practiced

- Launching virtual machines
- Selecting an AMI
- Choosing an instance type
- Managing key pairs