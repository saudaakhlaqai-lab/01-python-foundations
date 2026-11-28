"""
Command:
ip

Purpose:
Displays and manipulates network interfaces and routing tables.

Example:
ip addr show

Example Output:
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 12:34:56:78:9a:bc brd ff:ff:ff:ff:ff:ff

When I Used It:
To display and manage network interfaces and routing tables on my AWS EC2 instance.
"""