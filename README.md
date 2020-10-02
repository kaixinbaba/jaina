jaina
===============================
![吉安娜](./jaina.jpg)

Release log
--------
1.0.0 - 第一个正式版本，支持了最重要的`zkCli`的原生命令以及一些常见的类似Linux系统命令，如: `cd`, `ls`, `alias`, `history`等

Overview
--------
*Jaina*是一个轻量级的`zookeeper`命令行交互客户端工具，特点是：安装方便，使用符合Linux的命令行习惯，zk原生自带的`zkCli`太难用，极其不友好，
所以萌生了自己写一个类似的工具的想法。

Installation / Usage
--------------------

To install use pip:

    $ pip install jaina


Or clone the repo:

    $ git clone https://github.com/kaixinbaba/jaina.git
    $ python setup.py install
    
Upgrade
-------
    $ pip install -U jaina

    
Example
-------
```bash
$ jaina -h 127.0.0.1:2181
```
You will see this if zk connected
```bash
Zookeeper connected

    _____     _       _____  ____  _____       _
   |_   _|   / \     |_   _||_   \|_   _|     / \
     | |    / _ \      | |    |   \ | |      / _ \
 _   | |   / ___ \     | |    | |\ \| |     / ___ \
| |__' | _/ /   \ \_  _| |_  _| |_\   |_  _/ /   \ \_
`.____.'|____| |____||_____||_____|\____||____| |____|


Welcome to use JAINA
If you have problem, just try help !
If you want to quit, please input Ctrl+D or Ctrl+C

(jaina) [/]
```
Then you can use `help` command for help!

Please review the online docs [jaina](https://jaina.readthedocs.io/zh_CN/latest/) get more help.
