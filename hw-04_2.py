from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        # Перевірка на коректність введених даних (захист від "дурня")
        if not isinstance(pattern, str):
            raise TypeError("Параметр pattern повинен бути рядком (string)")
        
        count = 0
        
        # Допоміжна функція для глибокого обходу дерева (DFS)
        def dfs(node, current_path):
            nonlocal count  # Дозволяємо функції змінювати змінну count ззовні
            
            # Якщо ми стоїмо на вузлі, де закінчується якесь слово
            if node.value is not None:
                # Склеюємо букви з нашого шляху у повноцінне слово
                word = "".join(current_path)
                # Перевіряємо, чи закінчується воно на наш суфікс
                if word.endswith(pattern):
                    count += 1
            
            # Йдемо далі вглиб по всіх гілках (шухлядках)
            for char, next_node in node.children.items():
                current_path.append(char)    # Кладемо букву в кошик
                dfs(next_node, current_path) # Рекурсивно спускаємось глибше
                current_path.pop()           # Витягуємо букву, коли повертаємось назад
                
        # Запускаємо обхід від самого кореня дерева з порожнім кошиком шляху
        dfs(self.root, [])
        return count

    def has_prefix(self, prefix) -> bool:
        # Перевірка на коректність
        if not isinstance(prefix, str):
            raise TypeError("Параметр prefix повинен бути рядком (string)")
        
        current = self.root
        # Йдемо по буквах префікса, відкриваючи відповідні "шухлядки"
        for char in prefix:
            if char not in current.children:
                # Якщо потрібної шухлядки з буквою немає — такого префікса не існує
                return False
            current = current.children[char]
            
        # Якщо ми успішно пройшли всі букви префікса — він існує!
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    
    for i, word in enumerate(words):
        trie.put(word, i)

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
    
    print("Усі тести пройдено успішно! Алгоритми працюють бездоганно. ")