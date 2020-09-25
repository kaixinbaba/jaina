基本使用
========================
连接至Zk服务端
```bash
$ jaina -h 127.0.0.1:2181
# 或
$ jaina -h 127.0.0.1:2181/namespace
```
就会进入交互式的界面
```bash
Zookeeper connected

    _____     _       _____  ____  _____       _
   |_   _|   / \     |_   _||_   \|_   _|     / \
     | |    / _ \      | |    |   \ | |      / _ \
 _   | |   / ___ \     | |    | |\ \| |     / ___ \
| |__' | _/ /   \ \_  _| |_  _| |_\   |_  _/ /   \ \_
`.____.'|____| |____||_____||_____|\____||____| |____|


Welcome to use JAINA
If you have problem, just try 'help'!
If you want to quit, please input 'Ctrl+D' or 'Ctrl+C'

(jaina) [/]
```
`[/]`代表当前所在的路径, 通过`help`可以查看`jaina`支持的所有命令
```bash
(jaina) [/] help
```
或者通过`help <command>`查看某一个命令的帮助, 通过`<command> --help`查看对应命令的选项帮助，比如：
```bash
(jaina) [/] help cd
# 或
(jaina) [/] cd --help
```
如果要退出交互界面的话，可以使用`Ctrl + D`或`Ctrl + C`或`quit`命令