import paramiko
import sys

# Set args
host = sys.argv[1]
port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

# Register SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect
try:
	conn = client.connect(host, port=port, username=username, password=password, timeout=1)
	if conn is None:
        	print("Auth success")
except:
	print("Auth failed")

# Close the client
client.close()
