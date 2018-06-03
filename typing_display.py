from getch import getch
import os

def clear():
    os.system('clear')


# ptodo name
class TypingDisplay:
    def translate(self, x):
        """Override me"""
        return x

    def start(self):
        s = ''
        clear()
        print()
        while True:
            s = self._apply_char(s, getch())
            clear()
            print(self.translate(s))

    def _apply_char(self, s, c):
        if c == '\r':  # enter, ctrl-r
            s += '\n'
        elif c in ('\x7f', '\x08'):  # backspace, ctrl-h
            s = s[:-1]
        elif c == '\x03':  # ctrl-c
            exit()
        elif c == '\x15':  # ctrl-u
            s = ''
        else:
            s += c
        return s

TypingDisplay().start()
