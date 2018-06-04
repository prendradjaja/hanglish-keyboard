import syllabify
import phoneme_info
import pytest

@pytest.mark.parametrize('tokens,expected', [
    ('h ai',       [('h',   'ai', '')]),
    ('k A t s',    [('k',   'A',  't s')]),
    ('s p ai i z', [('s p', 'ai', ''),
                    ('',    'i',  'z')]),
])
def test__find_nuclei(tokens, expected):
    tokens = tokens.split()
    tokens = [phoneme_info.by_kbd[t] for t in tokens]

    actual = syllabify._find_nuclei(tokens)
    actual = [display_syllable(n) for n in actual]
    assert actual == expected

def display_syllable(n):
    return (display_phoneme_list(n.prev),
            n.vowel.kbd,
            display_phoneme_list(n.next))

def display_phoneme_list(lst):
    return ' '.join(t.kbd for t in lst)

@pytest.mark.parametrize('tokens,expected', [
    ('h ai', [['h'],['ai']]),
    ('s p ai i z', [['s','p'],['ai'],['i'],['z']]),
])
def test__to_sublists(tokens, expected):
    tokens = tokens.split()
    tokens = [phoneme_info.by_kbd[t] for t in tokens]

    actual = syllabify._to_sublists(tokens)
    actual = [[t.kbd for t in sublist] for sublist in actual]
    assert actual == expected

@pytest.mark.parametrize('tokens,expected', [
    ('k A t s', 'k / A / t s'),
    ('s p ai i z', 's p / ai / i / z'),
])
def test__add_separators(tokens, expected):
    tokens = tokens.split()
    tokens = [phoneme_info.by_kbd[t] for t in tokens]

    actual = syllabify._add_separators(tokens)
    actual = [t.kbd if t != syllabify.SEPARATOR else '/' for t in actual]
    actual = ' '.join(actual)
    assert actual == expected
