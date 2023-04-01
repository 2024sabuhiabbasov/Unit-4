# Quiz 053


## Codes
### My solution
```.py
# Program for Quiz 053
class WordCounter():
    def __init__(self, text):
        self.text = text
        self.word_count = {}

    def count_words(self):
        words = self.text.split()

        for word in words:
            word = word.split('.')[0].lower()
            if word in self.word_count:
               self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def get_results(self):
        return self.word_count


word_counter = WordCounter("This is a test Text. THis TEXT will be counted.")
word_counter.count_words()
print(word_counter.get_results())
```
### Test code
```.py
from Quiz_053 import WordCounter

def test_word_count():
    text = "This is a test text. It contains some words that will be counted."
    counter = WordCounter(text)
    counter.count_words()
    result = counter.get_results()
    assert result["this"] == 1
    assert result["is"] == 1
    assert result["a"] == 1
    assert result["test"] == 1
    assert result["text"] == 1
    assert result["it"] == 1
    assert result["contains"] == 1
    assert result["some"] == 1
    assert result["words"] == 1
    assert result["that"] == 1
    assert result["will"] == 1
    assert result["be"] == 1
    assert result["counted"] == 1

def test_word_count_empty_text():
    text = ""
    counter = WordCounter(text)
    counter.count_words()
    result = counter.get_results()
    assert result == {}

def test_word_count_multiple_occurrences():
    text = "This is a test text. This text will be counted."
    counter = WordCounter(text)
    counter.count_words()
    result = counter.get_results()
    assert result["this"] == 2
    assert result["is"] == 1
    assert result["a"] == 1
    assert result["test"] == 1
    assert result["text"] == 2
    assert result["will"] == 1
    assert result["be"] == 1
    assert result["counted"] == 1

def test_word_count_case_insensitive():
    text = "This is a test Text. THis TEXT will be counted."
    counter = WordCounter(text)
    counter.count_words()
    result = counter.get_results()
    assert result["this"] == 2
    assert result["is"] == 1
    assert result["a"] == 1
    assert result["test"] == 1
    assert result["text"] == 2
    assert result["will"] == 1
    assert result["be"] == 1
    assert result["counted"] == 1
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/223279343-47fde476-c1fb-443c-8d8b-aa8dda0a9dab.png)
