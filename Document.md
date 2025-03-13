# Documentation for Python Shell

## Overview
This project is a simple shell implemented in Python that supports basic shell commands like file manipulation, directory management, system information retrieval, and mathematical operations. The shell takes user input, processes the commands, and executes the appropriate system functions.

---

## Features

### 1. **Basic Commands**
- `echo <text>` → Prints the given text to the console.
- `exit` → Exits the shell.

### 2. **Date & Time**
- `date` → Displays the current date in DD-MM-YYYY format.
- `time` → Displays the current time in HH:MM:SS format.

### 3. **Screen Management**
- `cls` or `clear` → Clears the screen.

### 4. **File & Directory Management**
- `ls` → Lists all files and directories in the current directory.
- `pwd` → Displays the current working directory.
- `cd <directory>` → Changes the working directory.
- `mkdir <directory>` → Creates a new directory.
- `rmdir <directory>` → Removes an empty directory.
- `touch <file>` → Creates an empty file.
- `rm <file>` → Deletes a file.
- `cat <file>` → Displays the contents of a file.

### 5. **System Information**
- `hostname` → Displays the system hostname.
- `whoami` → Displays the current logged-in user.
- `ps` → Lists all running processes.

### 6. **Mathematical Expressions**
- Supports direct evaluation of arithmetic expressions (e.g., `5 + 3 * (2 - 1)`).

---

## How It Works
- The shell takes user input through a `while` loop.
- It checks if the input matches any of the predefined commands.
- If a command is found, it executes the corresponding function.
- If an input contains mathematical expressions, it evaluates them.
- If the input is not recognized, it returns an error message: `command not found`.

---

## Error Handling
- Commands that require a filename or directory name check for existence before execution.
- Handles `ZeroDivisionError` for math expressions.
- Catches `OSError` for directory and file operations.
- Displays appropriate error messages for invalid inputs.

---

## Dependencies
- Python 3.x
- `os` for file and directory operations.
- `datetime` for date and time retrieval.
- `socket` for system hostname.
- `wmi` for process management (Windows only).

---

## Future Improvements
- Implement command piping (`|`) to pass output between commands.
- Add support for background execution using `&`.
- Introduce scripting capabilities for automation.

---

## Author
Developed by Ansh Vardhan Yadav

## License
This project is open-source and licensed under the MIT License.

