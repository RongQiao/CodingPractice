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

# search files
# https://www.binarytides.com/linux-find-command-examples/

# zip and unzip tar.gz file
tar -xvzf zipfile
tar -cvzf zipfile directory

# check linux user/group
vi /etc/passwd
vi /etc/group

# change file/directory owner, perfmission
sudo chown username:group file
sudo chown username:group directory
sudo chown -R username:group directory
sudo chmod 777 file

# change symlink
ln -sf /new/target /path/to/symlink

# vi search and replace
:%s/pattern/toreplace

