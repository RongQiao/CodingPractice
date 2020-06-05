
# list cluster brokers from one zookeeper node
echo dump | nc localhost 2181 | grep brokers
