#!/usr/bin/env python3
import os
import json
import click
from subprocess import call

# 配置文件路径
CONFIG_FILE = os.path.expanduser("~/.quickcmd_commands.json")

def load_commands():
    """加载已保存的命令"""
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_commands(commands):
    """保存命令到文件"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(commands, f, indent=2)

@click.group()
def cli():
    """QuickCmd - 命令行快捷工具"""
    pass

@cli.command()
@click.argument('alias')
@click.argument('command', nargs=-1)  # 允许多参数命令
def add(alias, command):
    """添加一个快捷命令"""
    commands = load_commands()
    full_command = ' '.join(command)  # 合并多部分命令
    commands[alias] = full_command
    save_commands(commands)
    click.echo(f"✅ 已添加: {alias} = '{full_command}'")

@cli.command()
def list():
    """列出所有快捷命令"""
    commands = load_commands()
    if not commands:
        click.echo("暂无保存的命令。")
        return
    for alias, cmd in commands.items():
        click.echo(f"{alias}: {cmd}")

@cli.command()
@click.argument('alias')
def run(alias):
    """执行快捷命令"""
    commands = load_commands()
    if alias not in commands:
        click.echo(f"❌ 别名 '{alias}' 不存在！")
        return
    command = commands[alias]
    click.echo(f"🚀 执行: {command}")
    call(command, shell=True)  # 执行命令

if __name__ == '__main__':
    cli()