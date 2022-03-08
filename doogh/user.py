from getpass import getuser
from os.path import expanduser
from socket import gethostname

host_name = gethostname()
user_name = getuser()
user_home = expanduser(path="~")
