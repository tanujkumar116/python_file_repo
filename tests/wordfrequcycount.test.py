```python
import pytest
import string
from wordfrequcycount import word_frequency

def test_empty_string():
    assert word_frequency("") == {}

def test_only_punctuation():
    assert word_frequency("!!!...,,??") == {}

def test_repeated_words_and_punctuation():
    text = "Hello, world! This is a test. Hello, world!"
    expected = {'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
    assert word_frequency(text) == expected

def test_edge_case_leading_and_trailing_spaces():
    text = "  Hello, world!  "
    expected = {'hello': 1, 'world': 1}
    assert word_frequency(text) == expected

def test_edge_case_multiple_spaces_between_words():
    text = "Hello  world! This  is a test."
    expected = {'hello': 1, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1}
    assert word_frequency(text) == expected

def test_edge_case_numbers_in_string():
    text = "Hello 123 world!"
    expected = {'hello': 1, 'world': 1}
    assert word_frequency(text) == expected

def test_edge_case_mixed_case():
    text = "Hello World!"
    expected = {'hello': 1, 'world': 1}
    assert word_frequency(text) == expected

```
