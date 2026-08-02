# Exercise 2: Stream Management

Exercise2

ft_stream_management

Directory: ex2/

Files to Submit: ft_stream_management.py

Authorized: import sys, sys.argv, sys.stdin, sys.stdout, sys.stderr, len(), open(), import typing, typing.IO, io.read(), io.readline(), io.write(), io.flush(), io.close(), print()

Mission Briefing: The Archives operate through three sacred data channels that have been active since the founding of digital civilization. Master these channels that are older than the Internet itself!

Use the code created for the previous exercise. Update it to:

- Print error messages resulting from exceptions to the error output stream instead of to the standard output, with a clear prefix (see example)
- Get user input without using the input() built-in function.

## Example

```text
$> python3 ft_stream_management.py foo
=== Cyber Archives Recovery & Preservation ===
Accessing file 'foo'
[STDERR] Error opening file 'foo': [Errno 2] No such file or directory: 'foo'
python3 ft_stream_management.py ancient_fragment.txt
=== Cyber Archives Recovery & Preservation ===
Accessing file 'ancient_fragment.txt'
---
[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion
---
File 'ancient_fragment.txt' closed.
Transform data:
---
[FRAGMENT 001] Digital preservation protocols established 2087#
[FRAGMENT 002] Knowledge must survive the entropy wars#
[FRAGMENT 003] Every byte saved is a victory against oblivion#
---
Enter new file name (or empty): /etc/passwd
Saving data to '/etc/passwd'
[STDERR] Error opening file '/etc/passwd': [Errno 13] Permission denied: '/etc/passwd'
Data not saved.
```
