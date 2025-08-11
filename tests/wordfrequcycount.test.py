```python
import pytest
import string
from wordfrequcycount import word_frequency

def test_empty_string():
    assert word_frequency("") == {}

def test_only_punctuation():
    assert word_frequency(".,!?:;") == {}

def test_multiple_sentences_repeated_words():
    text = "Hello world! This is a test. Hello again, world. This is a great test."
    expected = {'hello': 2, 'world': 2, 'this': 2, 'is': 2, 'a': 2, 'test': 2, 'again': 1, 'great': 1}
    assert word_frequency(text) == expected

def test_string_with_numbers():
    text = "This is a test 123"
    expected = {'this': 1, 'is': 1, 'a': 1, 'test': 1, '123': 1}
    assert word_frequency(text) == expected

def test_string_with_mixed_case():
    text = "Hello World! This Is A Test."
    expected = {'hello': 1, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
    assert word_frequency(text) == expected

def test_string_with_apostrophes():
    text = "Let's test this string's handling of apostrophes."
    expected = {'lets': 1, 'test': 1, 'this': 1, 'strings': 1, 'handling': 1, 'of': 1, 'apostrophes': 1}
    assert word_frequency(text) == expected

```
