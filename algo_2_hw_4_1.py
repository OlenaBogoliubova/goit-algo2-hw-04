class TrieNode:
    """Клас для вузла Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None  # Для збереження значення, яке передається в put()


class Trie:
    """Базовий клас Trie для зберігання слів."""
    def __init__(self):
        self.root = TrieNode()

    def put(self, word: str, value):
        """Додає слово в Trie та зберігає значення."""
        if not isinstance(word, str):
            raise ValueError("Слово повинно бути рядком.")

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.value = value  # Зберігаємо значення

    def search(self, word: str) -> bool:
        """Перевіряє, чи є слово в Trie."""
        if not isinstance(word, str):
            raise ValueError("Слово повинно бути рядком.")

        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


class Homework(Trie):
    """Клас Homework, який успадковує Trie і додає нові методи."""
    
    def count_words_with_suffix(self, pattern) -> int:
        """Підраховує кількість слів, що закінчуються заданим суфіксом."""
        if not isinstance(pattern, str):
            raise ValueError("Параметр має бути рядком.")

        count = 0
        words = self.get_all_words()  # Отримуємо всі слова з Trie
        for word in words:
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        """Перевіряє, чи є в Trie слова з заданим префіксом."""
        if not isinstance(prefix, str):
            raise ValueError("Параметр має бути рядком.")

        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Якщо дійшли до кінця префікса, то слова з цим префіксом існують

    def get_all_words(self) -> list:
        """Допоміжний метод для отримання всіх слів у Trie."""
        words = []
        self._dfs(self.root, "", words)
        return words

    def _dfs(self, node, prefix, words):
        """Рекурсивний обхід дерева для збору всіх слів."""
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, words)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)  # Додаємо слово в Trie

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("Усі тести пройдені успішно!")
