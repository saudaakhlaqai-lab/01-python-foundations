"""
Command:
netstat

Purpose:
Displays network connections, routing tables, interface statistics, and more.

Example:
netstat -tuln

Example Output:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp6       0      0 :::22                   ::::*                   LISTEN

When I Used It:
To view network connections and listening ports on my AWS EC2 instance.
"""