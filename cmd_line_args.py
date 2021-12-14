import sys  # load builtin module sys
import os   #  find and run os.py

print("sys.argv: {}".format(sys.argv))
print("sys.argv[0] (script name): {}".format(sys.argv[0]))
print("sys.argv[1]: {}".format(sys.argv[1]))

number_value = float(sys.argv[1])
print(number_value + 1)



