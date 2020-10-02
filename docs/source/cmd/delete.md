delete
========================
删除节点
## Usage
```bash
(jaina) [/] delete -[vR] [path]
```

```bash
(jaina) [/] delete /leaf
# 对删除的节点版本有要求
(jaina) [/] delete -v 1 /leaf
# 递归删除
(jaina) [/] delete -R /very/deep/path
```

## 查看帮助
```bash
(jaina) [/] help delete
(jaina) [/] delete --help
```
