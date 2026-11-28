"""
Command:
top

Purpose:
Displays information about running processes.

Example:
top

Example Output:
top - 12:00:00 up 1 day,  1:00,  2 users,  load average: 0.15, 0.10, 0.05
Tasks: 123 total,   1 running, 122 sleeping,   0 stopped,   0 zombie
%Cpu(s):  5.2 us,  2.1 sy,  0.0 ni, 92.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   7974.3 total,   1234.5 free,   2345.6 used,   4394.2 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   5678.9 avail Mem

PID USER      PR NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
1 root      20  0   libc-6.so   libc-6.so   libc-6.so S  

When I Used It:
To view information about running processes on my AWS EC2 instance.
"""