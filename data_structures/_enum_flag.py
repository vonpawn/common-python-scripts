import enum


class Permission(enum.Flag):
    EXECUTE = enum.auto()
    WRITE = enum.auto()
    READ = enum.auto()

    def to_linux_perms(self):
        r = 'r' if Permission.READ in self else '-'
        w = 'w' if Permission.WRITE in self else '-'
        x = 'x' if Permission.EXECUTE in self else '-'
        return f'{r}{w}{x}'


class FileObj:
    # fictional example class to demonstrate enum functionality in-context; do not actually use this
    def __init__(self, filepath, filename, perms: Permission):
        print('init perms')
        self.filepath = filepath
        self.filename = filename
        self.permissions = perms
        self.list_perms()

    def has_permission(self, perm: Permission):
        # less readable, but sticks to bitwise operations: return self.permissions & perm == perm
        return perm in self.permissions

    def add_perm(self, new_perm: Permission):
        # bitwise "OR" to combine
        print(f'adding perm: {new_perm}')
        self.permissions |= new_perm
        self.list_perms()

    def remove_perm(self, del_perm):
        # equivelant to bitwise "AND NOT"
        # Note: be very careful with using the NOT (~) operator in python. Python's NOT behaves very different to expectations
        # if used on numbers. enums thankfully work the way the rest of the programming world expects
        print(f'removing flags: {del_perm}')
        self.permissions &= ~del_perm
        self.list_perms()

    def toggle_perm(self, perm: Permission):
        # bitwise "XOR" to toggle perm
        print(f'toggling flag: {perm}')
        self.permissions ^= perm
        self.list_perms()

    def clear_perms(self):
        print(f'clearing perms')
        self.permissions = Permission(0)
        self.list_perms()

    def list_perms(self):
        print(f'{self.permissions} (value: {self.permissions.value}) (linux: {self.permissions.to_linux_perms()})')
        print()


if __name__ == '__main__':
    my_file = FileObj('/users/myuser/', 'test.txt', Permission.READ | Permission.WRITE)

    my_file.clear_perms()
    my_file.add_perm(Permission.READ | Permission.WRITE | Permission.EXECUTE)
    my_file.add_perm(Permission.READ)  # should have no effect, READ was already added
    my_file.remove_perm(Permission.EXECUTE | Permission.WRITE)
    my_file.remove_perm(Permission.WRITE)  # should have no effect, WRITE was already removed
    my_file.toggle_perm(Permission.READ | Permission.WRITE)
