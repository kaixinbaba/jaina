setAcl
========================
设置节点的权限信息
## Usage
```bash
(jaina) [/] setAcl -[vu] [scheme:type:perm]
```

```bash
(jaina) [/] setAcl /your/path scheme:type:perm
(jaina) [/] setAcl -v 1 /your/path scheme:type:perm
(jaina) [/] setAcl /your/path world:anyone:cdrwa
(jaina) [/] setAcl /your/path ip:192.168.1.11:cwa
(jaina) [/] setAcl /your/path ip:192.168.1.11/24:cd
(jaina) [/] setAcl /your/path digest:<username>:<base64sha1password>:r
(jaina) [/] setAcl -u /your/path digest:<username>:<originpassword>:r
```
查看帮助
```bash
(jaina) [/] help setAcl
(jaina) [/] setAcl --help
```
