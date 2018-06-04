import util
import pytest

@pytest.mark.parametrize('lst,expected', [
    (['a', 'b', 'b', 'c'], ['a', 'b', 'c']),
])
def test_dedupe(lst, expected):
    assert util.dedupe(lst) == expected
