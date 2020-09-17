# 原生的命令必须支持
- addauth scheme auth
- close
- config [-c] [-w] [-s]
- connect host:port
- create [-s] [-e] [-c] [-t ttl] path [data] [acl]
- delete [-v version] path
- deleteall path
- delquota [-n|-b] path
- get [-s] [-w] path
- getAcl [-s] path
- history
- listquota path
- ls [-s] [-w] [-R] path
- ls2 path [watch]
- printwatches on|off
- quit
- reconfig [-s] [-v version] [[-file path] | [-members serverID=host:port1:port2;port3[,...]*]] | [-add serverId=host:port1:port2;port3[,...]]* [-remove serverId[,...]*]
- redo cmdno
- removewatches path [-c|-d|-a] [-l]
- rmr path
- set [-s] [-v version] path data
- setAcl [-s] [-v version] [-R] path acl
- setquota -n|-b val path
- stat [-w] path
- sync path

# 符合*unix 习惯的命令
- cd
- pwd
- rm

# 自定义的命令
- exists

# home目录下的配置文件
- 别名
- 历史记录
- 引入log

