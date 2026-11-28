"""
Command:
systemctl

Purpose:
Controls the systemd system and service manager.

Example:
systemctl status ssh

Example Output:
● ssh.service - OpenSSH server daemon
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2023-01-01 12:00:00 UTC; 1 day ago
     Docs: man:sshd(8)
           man:sshd_config(5)
 Main PID: 1234 (sshd)
    Tasks: 1 (limit: 4915)
   Memory: 1.2M
      CPU: 0.1s
   CGroup: /system.slice/ssh.service
           └─1234 /usr/sbin/sshd -D


When I Used It:
To view the status of systemd services on my AWS EC2 instance.
"""