import base64
import getpass
import os
import socket
import sys
import traceback

import paramiko
from paramiko.py3compat import input


orion = "wedding.reeher-palmer.net"

local_content = "/home/travis/build/klreeher/wedding-pelican/connect"
remote_content = "var/www/html/wedding.reeher-palmer.net/public_html"

transport = paramiko.Transport((orion,22))
transport.connect(username = $FTP_USER, password = $FTP_PASSWORD)
stfp = paramiko.SFTPClient.from_transport(transport)

print('local_content '+local_content)
print('remote_content '+remote_content)

sftp.put(local_content, remote_content)

transport.close()
