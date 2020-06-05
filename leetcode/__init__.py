

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1

def search(arr, target):
    if not arr:
        return 0
    if arr[-1] < target:
        return len(arr)

    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (r+l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

print(search([1,3,5,6], 2))
print(search([1,3,5,6], 0))
print(search([1,3,5,6], 7))






Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def max_unique_substring(string):
    if not string:
        return 0
    substring_indices = {string[0]: 0}
    max_length = 1
    i = 0
    for j in range(1, len(string)):
        last_seen = substring_indices.get(string[j], -1)
        if last_seen == -1:
            max_length = max(j+1-i, max_length)
        else:
            while i <= last_seen:
                substring_indices[string[i]] = -1
                i += 1
        substring_indices[string[j]] = j
    return max_length


print(max_unique_substring('bbbb'))
print(max_unique_substring('pwwkew'))
print(max_unique_substring('abcabcbb'))


# [2,5,9,-1, -2, -5]

def getPairCount(arr):

    n = len(arr)

    dict_checkpair = {}
    count = 0

    for i in range(n):

        if arr[i] * -1 in dict_checkpair:
            count +=1
        else:
            dict_checkpair



# <property>
# <name>hive.server2.use.SSL</name>
# <value>true</value>
# </property>
#
# <property>
# <name>hive.server2.keystore.path</name>
# <value>/usr/lib/hive2/conf/dev.aic.box.com.combined.jks</value>
# </property>
#
# <property>
# <name>hive.server2.keystore.password</name>
# <value>zsJaNxqw69D=7R8=</value>
# </property>

jdbc:hive2://localhost:10003/default;ssl=true;sslTrustStore=/home/ec2-user/hive-truststore.jks;trustStorePassword=zsJaNxqw69D=7R8=

beeline -u "jdbc:hive2://10.0.0.173:10001/default;ssl=true;sslTrustStore=/home/ec2-user/cacerts;trustStorePassword=changeit?hive.server2.transport.mode=http;hive.server2.thrift.http.path=cliservice" -e "show databases;"