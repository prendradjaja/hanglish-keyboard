def encode(word):
    tokens = tokenize(word)
    syllables = syllabify(tokens)
    encoded = ''.join(encode_syllable(s) for s in syllables)
    return encoded
