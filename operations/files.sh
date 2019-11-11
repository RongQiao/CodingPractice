# this is for files related  shell scripts

# count file numbers in one directory
# https://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x700.html
ls -l | wc -l

# sort files based on data and time, latest one comes the first
ls -lt
# or reverst time
ls -ltr

# search files containing string in folder and subfolders
grep -R 'the string' .
