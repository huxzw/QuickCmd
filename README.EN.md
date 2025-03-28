# QuickCmd - Command Line Shortcut Tool  

## Overview  

QuickCmd is a simple command-line shortcut tool that allows you to create short aliases for frequently used commands, improving productivity. Key features include:  

1. **Add Shortcut Commands**: Create memorable aliases for long commands  
2. **List All Commands**: View all saved shortcuts  
3. **Execute Commands**: Quickly run saved commands using aliases  

## Installation & Usage  

### Requirements  
- Python 3.x  
- `click` library (install via pip)  

### Installation Steps  

1. Save the script as `quickcmd.py`  
2. Make it executable:  
   ```bash  
   chmod +x quickcmd.py  
   ```  
3. (Optional) Move to a PATH directory (e.g., `/usr/local/bin`):  
   ```bash  
   sudo mv quickcmd.py /usr/local/bin/qc  
   ```  

### Usage  

#### 1. Add a Shortcut Command  
```bash  
qc add <alias> "<full command>"  
```  
Examples:  
```bash  
qc add gs "git status"  
qc add update "sudo apt update && sudo apt upgrade -y"  
```  

#### 2. List All Shortcuts  
```bash  
qc list  
```  

#### 3. Run a Shortcut Command  
```bash  
qc run <alias>  
```  
Example:  
```bash  
qc run gs  
```  

#### 4. Get Help  
```bash  
qc --help  
```  

## Configuration  

All shortcuts are stored in `~/.quickcmd_commands.json`. You can manually edit this file for advanced configurations.  

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

# Execute a shortcut  
qc run push  
```  

## Notes  

- Use quotes for commands containing special characters  
- Commands execute in the current shell environment  
- Aliases cannot contain spaces  

## License  

This project is open-source under the MIT License.