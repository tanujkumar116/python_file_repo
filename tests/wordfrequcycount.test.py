```python
import pytest
import string
from wordfrequcycount import word_frequency

def test_empty_string():
    assert word_frequency("") == {}

def test_only_punctuation():
    assert word_frequency(".,!?:;") == {}

def test_multiple_sentences_repeated_words():
    text = "Hello world! This is a test. Hello again, world. This is a test."
    expected = {'hello': 2, 'world': 2, 'this': 2, 'is': 2, 'a': 2, 'test': 2, 'again': 1}
    assert word_frequency(text) == expected

def test_string_with_numbers():
    text = "This is a test 123"
    expected = {'this': 1, 'is': 1, 'a': 1, 'test': 1, '123':1}
    assert word_frequency(text) == expected

def test_string_with_special_characters():
    text = "This is a test with special characters like @#$%^&*()"
    expected = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'with': 1, 'special': 1, 'characters': 1, 'like': 1}
    assert word_frequency(text) == expected

def test_string_with_mixed_case():
    text = "This Is A Test"
    expected = {"this": 1, "is": 1, "a": 1, "test": 1}
    assert word_frequency(text) == expected

def test_string_with_apostrophes():
    text = "This is a test with apostrophes like don't and can't"
    expected = {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'with': 1, 'apostrophes': 1, 'like': 1, "dont": 1, "cant": 1}
    assert word_frequency(text) == expected

```
