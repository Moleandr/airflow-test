import datetime
import socket
import os
import time

print("Hello from kubernetes2!!!")
print("datetime now =", datetime.datetime.now())
print("Hostname =", socket.gethostname())
time.sleep(10)
print("Home directory =", os.path.expanduser('~'))