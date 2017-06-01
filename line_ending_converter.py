"""
Takes two command line arguments.
First, the name of the file to convert.
Second, a zero if we are converting from Windows to UNIX, or non-zero value for vice versa.
"""

import sys, os

file_contents = str()
fp = open(sys.argv[1], 'r')

while(True):
    one_char_string = fp.read(1)
    if one_char_string == "":
        break
    file_contents = file_contents + one_char_string

fp.close()
new_file_contents = str()

if sys.argv[2]==0:
    # DOS -> UNIX
    # '\r\n' -> '\n'
    new_file_contents = file_contents
    i = int(0)
    while(True):
        if new_file_contents[i] == '\r':
            if len(new_file_contents) <= i+1:
                if new_file_contents[i+1] == '\n':
                    new_file_contents = new_file_contents[:i] + '\n' + new_file_contents[i+2:]
        i = i + 1
        if len(new_file_contents) <= i:
            break
    new_filename = sys.argv[1]
    last_period = new_filename.rfind(".")
    if last_period != -1:
        new_filename = new_filename[:last_period] + "-UNIX_version" + new_filename[last_period:]
    else:
        new_filename = new_filename + "-UNIX_version"
    new_fp = open(new_filename, 'w')
    new_fp.write(new_file_contents)
    new_fp.close()
else:
    # UNIX -> DOS
    # '\n' -> '\r\n'
    new_file_contents = file_contents
    i = int(0)
    while(True):
        if new_file_contents[i] == '\n':
            new_file_contents = new_file_contents[:i] + '\r\n' + new_file_contents[i+1:]
        i = i + 2
        if len(new_file_contents) <= i:
            break
    new_filename = sys.argv[1]
    last_period = new_filename.rfind(".")
    if last_period != -1:
        new_filename = new_filename[:last_period] + "-Windows_version" + new_filename[last_period:]
    else:
        new_filename = new_filename + "-Windows_version"
    new_fp = open(new_filename, 'w')
    new_fp.write(new_file_contents)
    new_fp.close()
