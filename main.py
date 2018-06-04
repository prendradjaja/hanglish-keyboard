from typing_display import TypingDisplay
from tokenize import tokenize
from encode import encode


class HanglishKeyboard(TypingDisplay):
    def translate(self, s):
        words = s.split()
        ret = ''
        for w in words:
            try:
                tokens = tokenize(w)
                hangul = encode(tokens)
            except:
                hangul = w
            ret += hangul + ' '
        return ret

HanglishKeyboard().start()
