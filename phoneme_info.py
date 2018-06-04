from collections import namedtuple

Phoneme = namedtuple('Phoneme', 'kbd ipa arpa hangul is_vowel final_allowed is_double')

                       # kbd ipa arp hangl vowel  final double
null_vowel =     Phoneme('', '', '', 'ㅡ', True,  None, None)
null_consonant = Phoneme('', '', '', 'ㅇ', False, None, None)

by_kbd = {
    ## CONSONANTS
               # kbd  ipa arp hangl vowel final   double
    'p': Phoneme('p', '', '', 'ㅍ', False, True,  False),
    'b': Phoneme('b', '', '', 'ㅂ', False, True,  False),
    't': Phoneme('t', '', '', 'ㅌ', False, True,  False),
    'd': Phoneme('d', '', '', 'ㄷ', False, True,  False),
    'k': Phoneme('k', '', '', 'ㅋ', False, True,  False),
    'g': Phoneme('g', '', '', 'ㄱ', False, True,  False),
    'm': Phoneme('m', '', '', 'ㅁ', False, True,  False),
    'n': Phoneme('n', '', '', 'ㄴ', False, True,  False),
    'l': Phoneme('l', '', '', 'ㄹ', False, True,  False),
    's': Phoneme('s', '', '', 'ㅅ', False, True,  False),
    'j': Phoneme('j', '', '', 'ㅈ', False, True,  False),
    'c': Phoneme('c', '', '', 'ㅊ', False, True,  False),
    'h': Phoneme('h', '', '', 'ㅎ', False, True,  False),
    'z': Phoneme('z', '', '', 'ㅇ', False, True,  False),

               # kbd  ipa arp hangl vowel final   double
    'G': Phoneme('G', '', '', 'ㄲ', False, True,  True),
    'S': Phoneme('S', '', '', 'ㅆ', False, True,  True),
    'B': Phoneme('B', '', '', 'ㅃ', False, False, True),
    'D': Phoneme('D', '', '', 'ㄸ', False, False, True),
    'J': Phoneme('J', '', '', 'ㅉ', False, False, True),

    ## VOWELS
                # kbd   ipa arp hangl vowel N/A   N/A
    'a':  Phoneme('a',  '', '', 'ㅏ', True, None, None),
    'e':  Phoneme('e',  '', '', 'ㅓ', True, None, None),
    'i':  Phoneme('i',  '', '', 'ㅣ', True, None, None),
    'o':  Phoneme('o',  '', '', 'ㅗ', True, None, None),
    'u':  Phoneme('u',  '', '', 'ㅜ', True, None, None),
    'A':  Phoneme('A',  '', '', 'ㅑ', True, None, None),
    'ai': Phoneme('ai', '', '', 'ㅐ', True, None, None),
    'au': Phoneme('au', '', '', 'ㅒ', True, None, None),
    'E':  Phoneme('E',  '', '', 'ㅕ', True, None, None),
    'ei': Phoneme('ei', '', '', 'ㅔ', True, None, None),
    'oi': Phoneme('oi', '', '', 'ㅚ', True, None, None),
    'O':  Phoneme('O',  '', '', 'ㅛ', True, None, None),
    'U':  Phoneme('U', '', '',  'ㅠ', True, None, None),

                 # kbd    ipa arp hangl vowel N/A   N/A
    'ue':  Phoneme('ue',  '', '', 'ㅝ', True, None, None),
    'oa':  Phoneme('oa',  '', '', 'ㅘ', True, None, None),
    'uei': Phoneme('uei', '', '', 'ㅞ', True, None, None),
    'ui':  Phoneme('ui',  '', '', 'ㅟ', True, None, None),
    'oai': Phoneme('oai', '', '', 'ㅙ', True, None, None),
    'Ei':  Phoneme('Ei',  '', '', 'ㅖ', True, None, None),
    'I':   Phoneme('I',   '', '', 'ㅢ', True, None, None),
}

# these don't need to be specially-encoded
# oaO	ㅘㅛ
# Eii	ㅖㅣ

