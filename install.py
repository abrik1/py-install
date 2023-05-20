from os import system, chmod, chdir
from os.path import isfile, isdir
from shutil import copy
from stat import S_IXOTH as exec_all
from stat import S_IWOTH as write_all
from stat import S_IROTH as read_all
from stat import S_IRWXO as rwe_all
from stat import S_IRWXU as rwe_user
from stat import S_IREAD as read_user
from stat import S_IWRITE as write_user
from stat import S_IEXEC as exec_user

permissions = [exec_all, write_all, read_all, rwe_all, read_user, write_user, exec_user]

def run_tests(TargetFile, Destination, Permissions):
    if isfile(TargetFile) == True:
        pass
    else:
        raise FileNotFoundError(TargetFile, "does not exists") 

    if isdir(Destination) == True:
        pass
    else:
        raise FileExistsError(Destination, "is invalid")

    if Permissions not in permissions:
        raise PermissionError(Permissions, "is invalid. use permissions from " , permissions)
    else:
        pass

    return "good"

def install(TargetFile, Destination, Permissions):
    if run_tests(TargetFile, Destination, Permissions) == "good":
        pass
    else:
        exit(1)

    chmod(Targetfile, Permissions)
    copy(TargetFile, Destination)
