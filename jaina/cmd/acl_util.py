import re

from kazoo.security import Permissions

R = Permissions.READ
W = Permissions.WRITE
C = Permissions.CREATE
D = Permissions.DELETE
A = Permissions.ADMIN


def can_create(perms):
    return perms & C


def can_write(perms):
    return perms & W


def can_delete(perms):
    return perms & D


def can_read(perms):
    return perms & R


def can_acl(perms):
    return perms & A


def int2perm(perms):
    return f"{'c' if can_create(perms) else ''}{'d' if can_delete(perms) else ''}{'r' if can_read(perms) else ''}{'w' if can_write(perms) else ''}{'a' if can_acl(perms) else ''}"


def perm2int(perm):
    if perm == 'all':
        return C | D | R | W | A
    else:
        perm_int = 0
        if 'c' in perm:
            perm_int |= C
        elif 'd' in perm:
            perm_int |= D
        elif 'r' in perm:
            perm_int |= R
        elif 'w' in perm:
            perm_int |= W
        elif 'a' in perm:
            perm_int |= A
        return perm_int


schemes = ['world', 'ip', 'digest', 'super']


def validate_scheme(scheme):
    return scheme in schemes


def validate_perm(perm):
    if perm == 'all':
        return True
    else:
        # 找不到cdrwa以外的字母
        return not re.search('[^cdrwa]', perm)

def _validate_ip(ip):
    ip_nums = ip.split('.')
    if len(ip_nums) != 4:
        raise ValueError(f"Illegal ip address '{ip}'")
    for num in ip_nums:
        # TODO ip 网段的支持, 需要ZK服务端支持, 不行的话，是否需要通过客户端拆成多次调用
        # if '/' not in num and '~' not in num:
        # pure number, must between 0 and 255
        try:
            num = int(num)
        except Exception as e:
            raise ValueError(f"Illegal ip number '{num}'")
        if num < 0 or num > 255:
            raise ValueError(f"Illegal ip number '{num}'")
    return True




def validate_id(scheme, id):
    if scheme == 'world':
        return id == 'anyone'
    elif scheme == 'ip':
        return _validate_ip(id)
    elif scheme == 'digest' or scheme == 'super':
        return len(id.split(':')) == 2


if __name__ == '__main__':
    perm = 'crwdwww wwa'
    matchObj = re.search('[^cdrwa]', perm)
    print(matchObj)
    print('match' if matchObj else 'not match')
