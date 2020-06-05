#!/usr/bin/env bash
ifconfig # deprecated
# vs, https://computingforgeeks.com/ifconfig-vs-ip-usage-guide-on-linux/
ip

# why do you chane MAC address
# https://blog.technitium.com/2011/06/why-you-need-to-change-mac-address.html

# ip addr and net mast, vs cidr address

# understand TCP/IP, https://medium.com/@james_aka_yale/the-4-layer-internet-model-network-engineers-need-to-know-e78432614a4f
# it's great writing

# 用户访问网站基本流程及原理(史上最全,没有之一)
# https://blog.csdn.net/yonggeit/article/details/72857630

# check ip of host, or hostname of ip
host <ip or name>

# run command on remote machine
ssh $host <command to run>
ssh $host <command 1; command 2;>

# system port command
netstat
# check listen port
sudo netstat -plnt

nc
nc -vz <ip> <port>
#https://support.rackspace.com/how-to/testing-network-services-with-netcat/

curl -XGET -u admin --cacert /box/etc/pki/trust/es_nr.pem  'https://nr-es-master00006.us-rno-a.dc001.prod.box.net:9200/_cat/nodes?pretty'