import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    translator = str.maketrans('', '', string.punctuation.replace('-', ''))
                    text = text.translate(translator)
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('text1.txt')
print(finder2.get_all_words())
print(finder2.find('FEARFUL'))
print(finder2.count('heART'))
