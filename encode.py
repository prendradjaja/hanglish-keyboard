import phoneme_info
import hgtk
from util import with_prev, with_prev_and_next


SEPARATOR = '[SEP]'

# res = hgtk.letter.compose(*jamos)
# except hgtk.exception.NotHangulException:

# PHONEME:
# kbd
# ipa
# arpa
# hangul
# is_vowel
# final_allowed
# is_double


class Syllable:
    def __init__(self, vowel, prev, next):
        self.vowel = vowel

        # Consonant lists (before and after this vowel) to pull from, ...
        self.prev = prev
        self.next = next

        # ... which will become your onset and coda
        self.onset = None
        self.coda = None

def encode(tokens):
    if any([t.is_vowel for t in tokens]):
        syllables = _find_nuclei(tokens)

        # each vowel pulls one pre- consonant if possible, limited by:
        #     availability
        for s in syllables:
            if s.prev:
                s.onset = s.prev.pop()

        # each vowel pulls one post- consonant if possible, limited by:
        #     availability
        #     legality for final position
        for s in syllables:
            if s.next and s.next[0].final_allowed:
                s.coda = s.next.pop(0)

        # each vowel pulls one more post- consonant if possible, limited by:
        #     availability
        #     if the previous post- consonant was a double, this is not allowed
        #     legality for second final position, dependent on first final
        # ptodo implement second finals

        syllables = _handle_remaining_consonants(syllables)
    else:
        syllables = _syllabify_consonant_cluster(tokens)

    _add_placeholders(syllables)

    return _to_hangul(syllables)

def _to_hangul(syllables):
    ret = ''
    for s in syllables:
        jamos = [s.onset.hangul,
                 s.vowel.hangul,
                 s.coda.hangul if s.coda else None]
        character = hgtk.letter.compose(*jamos)
        ret += character
    return ret

def _add_placeholders(syllables):
    for s in syllables:
        if not s.onset:
            s.onset = phoneme_info.null_consonant
        if not s.vowel:
            s.vowel = phoneme_info.null_vowel

def _handle_remaining_consonants(syllables):
    """
    Split remaining vowelless consonants into "syllables" of their own
    """
    ret = []
    for s in syllables:
        if s.prev:
            ret.extend(_syllabify_consonant_cluster(s.prev))
            s.prev[:] = []
        ret.append(s)
        if s.next:
            ret.extend(_syllabify_consonant_cluster(s.next))
            s.next[:] = []
    return ret

def _syllabify_consonant_cluster(tokens):
    # Greedy implementation
    ret = []
    for t in tokens:
        if ret and not (ret[-1].coda) and t.final_allowed:
            ret[-1].coda = t
        else:
            s = Syllable(None, [], [])
            s.onset = t
            ret.append(s)
    return ret

def _find_nuclei(tokens):  # => Nucleus[]
    """
    s p ai i z =>
    [
      * Consonants(s, p),
        Vowel(ai),
      * Consonants(),
        Vowel(i),
      * Consonants(z),
    ]
    Starred elements are not in the "nuclei" list, but...

    If the word begins or ends in a vowel, an empty consonant list is
    prepended or appended as needed.
    """
    sublists = _to_sublists(tokens)
    ret = []
    for (prev, sublist, next) in with_prev_and_next(sublists, lambda: []):
        if sublist[0].is_vowel:
            if prev and prev[0].is_vowel:
                prev = []
            if next and next[0].is_vowel:
                next = []
            ret.append(Syllable(sublist[0], prev, next))
    return ret

def _to_sublists(tokens):
    """
    s p ai i z =>
    [[s p] [ai] [i] [z]]

    Each sublist is only consonants (1 or more) or exactly 1 vowel.
    """
    ret = []
    curr = []
    for t in _add_separators(tokens):
        if t == SEPARATOR:
            if curr:
                ret.append(curr)
                curr = []
        else:
            curr.append(t)
    if curr:
        ret.append(curr)
    return ret

def _add_separators(tokens):
    """
    Adds "separators" around vowels.

    s p ai i z =>
    s p / ai / i / z

    / here represents the constant `SEPARATOR`
    """
    with_separators = []
    for t in tokens:
        if t.is_vowel:
            with_separators += [SEPARATOR, t, SEPARATOR]
        else:
            with_separators += [t]

    # Collapse adjacent separators.
    # s p / ai / / i / z
    # s p / ai / i / z =>
    ret = []
    for (prev, t) in with_prev(with_separators):
        if prev == SEPARATOR and t == SEPARATOR:
            continue
        ret.append(t)
    return ret


#     for t in tokens:
#
# def to_homogeneous_substrings(tokens):
#     """
#     s p ai i z =>
#     [[s p] [ai] [i] [z]]
#
#     Each sublist is only consonants (1 or more) or exactly 1 vowel.
#     """
#     ret = []
#     curr = [tokens[0]]
#     curr_is_consonants = not tokens[0].is_vowel
#     for t in tokens[1:]:
#
#
