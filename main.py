from typing_display import TypingDisplay
from syllabify import syllabify
from tokenize import tokenize
from encode import encode


class HanglishKeyboard:
    def translate(self, s):
        words = s.split()
        return ' '.join(encode(w) for w in words)
