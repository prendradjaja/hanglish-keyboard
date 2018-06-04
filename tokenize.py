from phoneme_info import by_kbd

legal_tokens = ['\\']
legal_tokens += sorted(by_kbd.keys(), key=lambda x: (-len(x), x))

def tokenize(word):
    i = 0
    tokens = []
    while i < len(word):
        t = match(word[i:])
        if t != '\\':
            tokens.append(by_kbd[t])
        i += len(t)
    return tokens

def match(s):
    for t in legal_tokens:
        if s.startswith(t):
            return t
    raise Exception('no matching token')

# test_cases = [
#     'tako',
#     'taiko',
#     'ta\\iko',
#     'tako3',
# ]
#
# for x in test_cases:
#     try:
#         print(x, ' '.join(x.kbd for x in tokenize(x)))
#     except:
#         print(x, 'failed')
