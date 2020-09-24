.. jaina documentation master file, created by
   sphinx-quickstart on Thu Sep 24 14:00:55 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================
欢迎
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

   cmd/alias.md
   cmd/cd.md

:doc:`cmd/alias`
   设置或者查询别名

:doc:`cmd/cd`
   更换当前目录

感谢
==============

`click`_ 是一个强大的命令行库，帮助用户快速的实现自己的命令行应用
.. _click: https://github.com/pallets/click

`rich`_ 是一个强大的命令行UI库，可以在终端显示各种酷炫的效果
.. _rich: https://github.com/willmcgugan/rich

`python-prompt-toolkit`_ 是一个强大的命令行交互库，帮助用户建立可交互的应用
.. _python-prompt-toolkit: https://github.com/prompt-toolkit/python-prompt-toolkit

`kazoo`_ 是一个纯python编写的，Zookeeper的客户端，jaina底层和zk的交互都是通过该库来实现的
.. _kazoo: https://github.com/python-zk/kazoo

