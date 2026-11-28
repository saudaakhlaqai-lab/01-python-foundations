"""
Command:
ps

Purpose:
Displays information about running processes.

Example:
ps aux

Example Output:
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1  12345  6789 ?        Ss   Jan01   0:01 /sbin/init
daemon       2  0.0  0.0      0     0 ?        S    Jan01   0:00 [kthreadd]
bin          3  0.0  0.0      0     0 ?        S    Jan01   0:00 [ksoftirqd/0]
...

When I Used It:
To view information about running processes on my AWS EC2 instance.
"""