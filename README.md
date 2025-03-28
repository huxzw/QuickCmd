# QuickCmd - 命令行快捷工具

## 功能简介

QuickCmd 是一个简单的命令行快捷工具，允许你为常用命令创建简短的别名，提高工作效率。主要功能包括：

1. **添加快捷命令**：为长命令创建简短易记的别名
2. **列出所有命令**：查看已保存的所有快捷命令
3. **执行快捷命令**：通过别名快速执行保存的命令

## 安装与使用

### 安装要求
- Python 3.x
- click 库（可通过pip安装）

### 安装步骤

1. 将脚本保存为 `quickcmd.py`
2. 添加可执行权限：
   ```bash
   chmod +x quickcmd.py
   ```
3. （可选）将脚本移动到PATH目录，如`/usr/local/bin`：
   ```bash
   sudo mv quickcmd.py /usr/local/bin/quickcmd
   ```

### 使用方式

#### 1. 添加快捷命令
```bash
qc add <别名> "<完整命令>"
```
示例：
```bash
qc add gs "git status"
qc add update "sudo apt update && sudo apt upgrade -y"
```

#### 2. 列出所有快捷命令
```bash
qc list
```

#### 3. 执行快捷命令
```bash
qc run <别名>
```
示例：
```bash
qc run gs
```

#### 4. 获取帮助
```bash
qc --help
```

## 配置文件

所有快捷命令保存在用户主目录下的 `~/.quickcmd_commands.json` 文件中，可直接编辑该文件进行高级配置。

## 示例工作流

```bash
# 添加常用命令
qc add push "git push origin main"
qc add pull "git pull origin main"

# 查看保存的命令
qc list
# 输出:
# push: git push origin main
# pull: git pull origin main

# 使用快捷命令
qc run push
```

## 注意事项

- 如果命令中包含特殊字符，请使用引号包裹
- 命令会在当前shell环境中执行
- 别名不能包含空格

## 许可证

本项目采用MIT许可证开源。
给出对应英文版的