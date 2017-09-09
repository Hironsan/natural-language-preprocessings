from keras.preprocessing.sequence import pad_sequences


def pad_char_sequences(sequences, maxlen=None, dtype='int32',
                       padding='pre', truncating='pre', value=0.):
    if maxlen is None:
        maxlen = max(len(max(seq, key=len)) for seq in sequences)

    padded_sequences = []
    for sequence in sequences:
        padded_sequence = pad_sequences(sequence, maxlen, dtype, padding, truncating, value)
        padded_sequences.append(padded_sequence)

    return pad_sequences(padded_sequences, dtype=dtype, padding=padding,
                         truncating=truncating, value=value)
