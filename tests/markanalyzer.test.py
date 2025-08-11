```python
import pytest
from markanalyzer import analyze_marks

def test_valid_marks_grade_a():
    marks = [90, 95, 92, 98]
    avg, highest, lowest, grade = analyze_marks(marks)
    assert avg >= 90
    assert highest == 98
    assert lowest == 90
    assert grade == "A"

def test_valid_marks_grade_d():
    marks = [50, 55, 60, 58]
    avg, highest, lowest, grade = analyze_marks(marks)
    assert avg >= 50 and avg <60
    assert highest == 60
    assert lowest == 50
    assert grade == "D"

def test_empty_marks_list():
    marks = []
    with pytest.raises(ZeroDivisionError):
        analyze_marks(marks)

def test_non_numeric_marks():
    marks = [85, 90, "A", 95]
    with pytest.raises(TypeError):
        analyze_marks(marks)

def test_negative_marks():
    marks = [85, 90, -5, 95]
    avg, highest, lowest, grade = analyze_marks(marks)
    assert avg < 90
    assert highest == 95
    assert lowest == -5
    assert grade != "A"

def test_edge_case_grade_b():
    marks = [75, 75, 75, 75]
    avg, highest, lowest, grade = analyze_marks(marks)
    assert avg == 75
    assert highest == 75
    assert lowest == 75
    assert grade == "B"

def test_edge_case_grade_c():
    marks = [60,60,60,60]
    avg, highest, lowest, grade = analyze_marks(marks)
    assert avg == 60
    assert highest == 60
    assert lowest == 60
    assert grade == "C"

def test_edge_case_grade_d_boundary():
    marks = [59,59,59,59]
    avg, highest, lowest, grade = analyze_marks(marks)
    assert avg ==59
    assert highest == 59
    assert lowest == 59
    assert grade == "D"

```