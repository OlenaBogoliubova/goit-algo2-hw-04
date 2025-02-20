class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""
        
        # Додаємо всі слова в Trie
        for word in strings:
            self.insert(word)
        
        # Знаходимо найдовший спільний префікс
        node = self.root
        common_prefix = ""
        
        while node and len(node.children) == 1 and not node.is_end_of_word:
            char = next(iter(node.children))  # Отримуємо єдиного наявного нащадка
            common_prefix += char
            node = node.children[char]
        
        return common_prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    
    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    
    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    
    print("✅ Усі тести пройдено успішно!")