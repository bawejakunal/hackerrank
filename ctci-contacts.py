# https://www.hackerrank.com/challenges/ctci-contacts/

class Trie(object):
    def __init__(self, char):
        if len(char) > 1:
            raise ValueError("Expected a char, got string")
        self.data = char
        self.count = 0
        self.child = dict()
    
    def add(self, string):
        self.count += 1 #control reached this node as prefix search
        if len(string) < 1:
            return
        if string[0] not in self.child:
            self.child[string[0]] = Trie(string[0])
        self.child[string[0]].add(string[1:]) # insert in subtree of child node
    
    def find(self, partial):
        if len(partial) < 1:
            return self.count
        elif partial[0] not in self.child:
            return 0
        else:
            return self.child[partial[0]].find(partial[1:])

n = int(input().strip())
trie = Trie("")
for a0 in range(n):
    op, contact = input().strip().split()
    if op == "add":
        trie.add(contact)
    elif op == "find":
        print(trie.find(contact))
