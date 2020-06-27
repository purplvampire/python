#! Python3
# Create SSH connection script to remote control devices.
import paramiko
# Windows path convertion
import os.path
# Using time fuction
import time
# Using exception
import sys
# Using regular expression
import re

#### File check: users & commands file.

# Checking username/password file
# Prompting use for input - Username/Password file
user_file = input("\n# Enter user file path and name:\n(e.g. D:\MyApps\myfile.txt)")

# Verifying the validity of the Username/Password file.
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid ^_^\n")

else:
    print("\n* File {} does not exist :(\nPlease check and try again. \n".format(user_file))
    sys.exit()

# Checking commands file
# Prompting use for input - Commands file
cmd_file = input("\n# Enter commands file path and name:\n(e.g. D:\MyApps\myfile.txt)")

# Verifying the validity of the Username/Password file.
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid ^_^\n")

else:
    print("\n* File {} does not exist :(\nPlease check and try again. \n".format(cmd_file))
    sys.exit()

#### Open SSHv2 connection to the device.

def ssh_connection(ip):

    global user_file
    global cmd_file

    # Creating SSH Connection
    try:
        # Define SSH parameters
        selected_user_file = Open(user_file, 'r')

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading the username form the file.
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Reading the password form the file.
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        # Logging into device
        session = paramiko.SSHClient()

        # For testing purposes, this allows auto-accepting unknown host keys.
        # Do not use in production! The default would be RejectPolicy 
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device using username and password.
        session.connect(ip.rstrip("\n"), username = username, password = passord)

        # Start an interactive shell session on the router.
        connection = session.invoke_shell()

        # Setting terminal length for entire output - disable pagination.
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        # Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        #### Input commands to the devices.
        # Open user selected file for reading.
        selected_cmd_file = open(cmd_file, 'r')

        # Starting from the beginning of the file.
        selected_cmd_file.seek(0)

        # Writing each line in the file to the device.
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        # Closing the user file
        selected_user_file.close()

        # Closing the commands file
        selected_cmd_file.close()

        # Checking command output for IOS syntax errors.
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))
        
        else:
            print("\nDone for device {} :D\n".format(ip))
        
        # Test for reading command output
        print(str(router_output) + "\n")

        # Closing the connection
        session.close()

    except paramiko.AuthenticationException:
        print("""
        * Invalid username or password :( 
        * Please check the username/password file or the device configuration.
        """)
        print("Closing program...Bye!")



router = ssh_connection("10.10.10.2")
router = str(router)
# Deal with string \\r\\n and convert to list.
router = router.split("\\r\\n") 
# Convert list to string
router = "\n".join(router)
# Save string to an file.
with open("E:\log.txt", "w") as f:
    f.write(router)





        
