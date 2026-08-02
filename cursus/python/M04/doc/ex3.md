# Exercise 3: Vault Security

Exercise3

ft_vault_security

Directory: ex3/

Files to Submit: ft_vault_security.py

Authorized: open(), read(), write(), print()

Mission Briefing: The Head Archivist has noticed your potential and is promoting you to Vault Security operations. This is where the real archivists prove themselves.

This exercise requires the use of the with statement (context manager) to ensure proper file handling. The with statement automatically closes files even if errors occur, preventing resource leaks.

Create a function secure_archive() that provides safe access to any file for reading or writing. It returns a tuple (True|False, str) that indicates whether the operation succeeded (the boolean) and provides the associated content (either the file's contents or an error message). The function takes the following parameters: a mandatory file name, an optional int or str (your choice) that indicates the action to perform (read or write), and another optional string that contains the content to write to the file.

During the defense, the structure of the code will be reviewed to match these requirements.

## Example

```text
$> python3 ft_vault_security.py
=== Cyber Archives Security ===
Using 'secure_archive' to read from a nonexistent file:
(False, "[Errno 2] No such file or directory: '/not/existing/file'")
Using 'secure_archive' to read from an inaccessible file:
(False, "[Errno 13] Permission denied: '/etc/master.passwd'")
Using 'secure_archive' to read from a regular file:
(True, '[FRAGMENT 001] Digital preservation protocols established 2087\n[FRAGMENT 002] Knowledge must survive the entropy wars\n[FRAGMENT 003] Every byte saved is a victory against oblivion\n')
Using 'secure_archive' to write previous content to a new file:
(True, 'Content successfully written to file')
```
