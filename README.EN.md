# QuickCmd - Command Line Shortcut Tool

## Overview

QuickCmd is a simple command-line shortcut utility that allows you to create short aliases for frequently used commands, boosting your productivity. Key features include:

1. **Add shortcuts**: Create memorable aliases for long commands
2. **List all commands**: View all saved shortcuts
3. **Execute commands**: Run saved commands using their aliases

## Installation & Usage

### Requirements
- Python 3.x
- click library (install via pip)

### Installation Steps

1. Save the script as `quickcmd.py`
2. Make it executable:
   ```bash
   chmod +x quickcmd.py
   ```
3. Create a symlink:
   ```bash
   sudo ln -s $(pwd)/quickcmd.py /usr/local/bin/qc
   ```

### Usage

#### 1. Add a shortcut
```bash
qc add <alias> "<full command>"
```
Examples:
```bash
qc add gs "git status"
qc add update "sudo apt update && sudo apt upgrade -y"
```

#### 2. List all shortcuts
```bash
qc list
```

#### 3. Execute a shortcut
```bash
qc run <alias>
```
Example:
```bash
qc run gs
```

#### 4. Get help
```bash
qc --help
```

## Configuration

All shortcuts are stored in `~/.quickcmd_commands.json` in your home directory. You can directly edit this file for advanced configuration.

## Example Workflow

```bash
# Add common commands
qc add push "git push origin main"
qc add pull "git pull origin main"

# View saved commands
qc list
# Output:
# push: git push origin main
# pull: git pull origin main

# Use shortcuts
qc run push
```

## Notes

- Wrap commands containing special characters in quotes
- Commands execute in the current shell environment
- Aliases cannot contain spaces

## License

This project is open-source under the MIT License.