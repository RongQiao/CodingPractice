import unittest


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        # to mark if the partial of branch is one inserted word
        self.iswordend = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(' ')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            candidates = current.children
            if letter not in candidates:
                newnode = self.insert_helper(letter, current)
                current = newnode
            else:
                current = candidates.get(letter)
        # the last letter, mark sign
        current.iswordend = True

    def insert_helper(self, letter, current_parent) -> TrieNode:
        newnode = TrieNode(letter)
        current_parent.children[letter] = newnode
        return newnode

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        last_letter_node = self.search_helper(word, 0, self.root)
        if last_letter_node is not None:
            if last_letter_node.iswordend:
                return True
            else:
                return False
        else:
            return False

    def search_helper(self, word, index, current_root) -> bool:
        n = len(word)
        candidates = current_root.children
        if index < n:
            letter = word[index]
            if letter in candidates:
                if index == n-1:
                    return candidates.get(letter)
                else:
                    current_root = candidates.get(letter)
                    return self.search_helper(word, index+1, current_root)
            else:
                return None
        else:
            None

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        last_letter_node = self.search_helper(prefix, 0, self.root)
        if last_letter_node is not None:
            return True
        else:
            return False


class MyTestCase(unittest.TestCase):
    def test_trie_normal(self):
        trie = Trie()
        trie.insert("there")
        assert trie.search("there")     # returns true
        assert not trie.search("the")   # returns false
        assert trie.startsWith("the")   # returns true
        trie.insert("the")
        assert trie.search("the")       # returns true


if __name__ == '__main__':
    unittest.main()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# Implement a trie with insert, search, and startsWith methods.
#
# root
# /    \ \
#     t    a      b
# |    |      |
# h    n      y
# |    |  \   |
# e    s  y   e
# /  |    |
# i   r    w
# |   |    |
# r   e    e
# |
# r
#
# Trie trie = new Trie();
#
# trie.insert("there");
# trie.search("there");   // returns true
# trie.search("the");     // returns false
# trie.startsWith("the"); // returns true
# trie.insert("the");
# trie.search("the");     // returns true
#
# Note:
# You may assume that all inputs consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.