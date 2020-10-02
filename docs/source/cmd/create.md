create
========================
创建ZK节点
## Usage
```bash
(jaina) [/] create -[seR] [path] [data]
```
创建空节点（无数据）
```bash
(jaina) [/] create /test
```
创建节点（有数据）
```bash
(jaina) [/] create /test abc
# 临时节点
(jaina) [/] create -e /test abc
# 顺序节点
(jaina) [/] create -s /test abc
# 递归创建（若上级目录不存在）
(jaina) [/] create -R /test/notExistsPath1/notExistsPath2/path abc
```

查看帮助
```bash
(jaina) [/] help create
(jaina) [/] create --help
```
