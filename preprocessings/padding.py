from keras.preprocessing.sequence import pad_sequences


def pad_char_sequences(sequences, maxlen=None, dtype='int32',
                       padding='pre', truncating='pre', value=0.):
    """Pads each sequence to the same length (length of the longest sequence).

    If maxlen is provided, any sequence longer than maxlen is truncated to maxlen.
    Truncation happens off either the beginning (default) or the end of the sequence.

    Supports post-padding and pre-padding (default).

    # Arguments
        sequences: list of lists of lists where each element is a sequence
        maxlen: int, maximum length
        dtype: type to cast the resulting sequence.
        padding: 'pre' or 'post', pad either before or after each sequence.
        truncating: 'pre' or 'post', remove values from sequences larger than
            maxlen either in the beginning or in the end of the sequence
        value: float, value to pad the sequences to the desired value.

    # Returns
        x: numpy array with dimensions (number_of_sequences, maxlen)

    # Raises
        ValueError: in case of invalid values for `truncating` or `padding`,
            or in case of invalid shape for a `sequences` entry.
    """
    if maxlen is None:
        maxlen = max(len(max(seq, key=len)) for seq in sequences)

    padded_sequences = []
    for sequence in sequences:
        padded_sequence = pad_sequences(sequence, maxlen, dtype, padding, truncating, value)
        padded_sequences.append(padded_sequence)

    return pad_sequences(padded_sequences, dtype=dtype, padding=padding,
                         truncating=truncating, value=value)
