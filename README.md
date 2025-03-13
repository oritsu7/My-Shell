# Python Shell - README

## Overview
This is a simple command-line shell implemented in Python. It supports basic file operations, directory navigation, system information retrieval, process management, and arithmetic expression evaluation.

## Features
- **Basic Commands**: `echo`, `exit`
- **Date & Time**: `date`, `time`
- **Screen Management**: `cls`, `clear`
- **File & Directory Operations**: `ls`, `cd`, `mkdir`, `rmdir`, `touch`, `rm`, `cat`
- **System Information**: `hostname`, `whoami`
- **Process Management**: `ps`
- **Mathematical Expressions**: Direct evaluation of arithmetic expressions

## Installation & Usage
### Prerequisites
- Python 3.x
- `wmi` module (for Windows users)

### Running the Shell
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repo-name
   ```
3. Run the script:
   ```sh
   python shell.py
   ```

## Example Usage
```sh
$ echo Hello, World!
Hello, World!

$ date
12-03-2025

$ mkdir test_folder
Directory test_folder created successfully

$ ls
['test_folder']

$ ps
pid   Process name
1234  python.exe
5678  explorer.exe
```

## Error Handling
- Invalid commands return `command not found`.
- File and directory operations check for existence before execution.
- Mathematical expressions handle `ZeroDivisionError` gracefully.

## Future Enhancements
- Implement command piping (`|`)
- Support background execution (`&`)
- Add scripting capabilities

## Author
Developed by Ansh Vardhan Yadav

## License
This project is open-source and licensed under the MIT License.

