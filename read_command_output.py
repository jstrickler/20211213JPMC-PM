import os
with os.popen('netstat -an') as ns_in:
    for line in ns_in:
        print(line.rstrip())

# if os.access(file_path, O_RD | O_WR)
