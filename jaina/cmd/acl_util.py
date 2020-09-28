R = 1 << 0
W = 1 << 1
C = 1 << 2
D = 1 << 3
A = 1 << 4


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


def int2acl(perms):
    return f"{'c' if can_create(perms) else ''}{'d' if can_delete(perms) else ''}{'r' if can_read(perms) else ''}{'w' if can_write(perms) else ''}{'a' if can_acl(perms) else ''}"
