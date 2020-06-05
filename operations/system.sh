#!/usr/bin/env bash
# why use env to run bash, see below post
# https://stackoverflow.com/questions/16365130/what-is-the-difference-between-usr-bin-env-bash-and-usr-bin-bash
# difference between several bin folder, https://www.quora.com/Whats-the-difference-between-usr-bin-and-usr-local-bin

# shell variable
# $1, $2 ...
# The following are the other special preset variables:
# $#: How many command line parameters were passed to the script.
# $@: All the command line parameters passed to the script.
# $?: The exit status of the last process to run.
# $$: The Process ID (PID) of the current script.
# $USER: The username of the user executing the script.
# $HOSTNAME: The hostname of the computer running the script.
# $SECONDS: The number of seconds the script has been running for.
# $RANDOM: Returns a random number.
# $LINENO: Returns the current line number of the script.

# BSD vs Linux
# https://helpdeskgeek.com/linux-tips/bsd-vs-linux-the-basic-differences/

# .bash_proflie vs .bashrc
# https://medium.com/@abhinavkorpal/bash-profile-vs-bashrc-c52534a787d3

# check current time
date

# check services
service --state-all
service <service name> start|stop|restart|status

# print linux kernel version
uname -r
https://www.youtube.com/watch?v=l0QGLMwR-lY

# check linux system version
cat /proc/version

# check uptime
uptime
# check system reboot/shutdown
last reboot | less
last shutdown | lee
# last -- last [...] prints information about connect times of users.
# head to keep the latest 10 events
# tac to invert the ordering
last -x | head | tac
# check system message
sudo vi /var/log/messages

