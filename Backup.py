import subprocess
backup_command = 'sqlcmd -S {local database server name}-d {local database name}-Q "BACKUP DATABASE [{local database name}] TO DISK=\’{path of destination to database}\'WITH INIT" -U {login} -P {password}'
subprocess.run(backup_command, shell=True)
