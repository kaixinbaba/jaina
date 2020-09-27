.. jaina documentation master file, created by
   sphinx-quickstart on Thu Sep 24 14:00:55 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
欢迎 Jaina 吉安娜
=================================
Jaina是一个简单好用又强大的 `Zookeeper`_ 客户端命令行工具，拥有彩色输出，自动提示，以及和类unix一样的体验.

.. _Zookeeper: https://baike.baidu.com/item/zookeeper

快速开始
===========

.. toctree::
   :caption: 快速开始
   :hidden:

   intro/overview.md
   intro/install.md
   intro/usage.md

:doc:`概览`
    Jaina是什么？

:doc:`安装`
    如何在你的电脑上安装Jaina

:doc:`基本使用`
    Jaina简单的示例

命令
==============

.. toctree::
   :caption: 命令
   :hidden:

   cmd/!.md
   cmd/alias.md
   cmd/cd.md
   cmd/create.md
   cmd/delete.md
   cmd/get.md
   cmd/help.md
   cmd/ls.md
   cmd/set.md
   cmd/history.md

:doc:`cmd/!`
   调用系统命令

:doc:`cmd/alias`
   设置或者查询别名

:doc:`cmd/cd`
   更换当前目录

:doc:`cmd/create`
   创建节点

:doc:`cmd/delete`
   删除节点

:doc:`cmd/get`
   获取数据

:doc:`cmd/help`
   获取帮助

:doc:`cmd/ls`
   获取目录

:doc:`cmd/set`
   设置数据

:doc:`cmd/history`
   查询历史命令

感谢
==============

`click <https://github.com/pallets/click>`_ 是一个强大的命令行库，帮助用户快速的实现自己的命令行应用

`rich <https://github.com/willmcgugan/rich>`_ 是一个强大的命令行UI库，可以在终端显示各种酷炫的效果

`python-prompt-toolkit <https://github.com/prompt-toolkit/python-prompt-toolkit>`_ 是一个强大的命令行交互库，帮助用户建立可交互的应用

`kazoo <https://github.com/python-zk/kazoo>`_ 是一个纯python编写的，Zookeeper的客户端，jaina底层和zk的交互都是通过该库来实现的

