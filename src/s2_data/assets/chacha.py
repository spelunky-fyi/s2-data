from struct import pack, unpack
import zstandard as zstd

def rotate_left(a, b):
    return ((((a) << (b)) | ((a) >> (32 - (b))))) & 0xFFFFFFFF

def quarter_round(w, a, b, c, d):
    w[a] += w[b]
    w[a] &= 0xFFFFFFFF
    w[d] ^= w[a]
    w[d] = rotate_left(w[d], 16)
    w[c] += w[d]
    w[c] &= 0xFFFFFFFF
    w[b] ^= w[c]
    w[b] = rotate_left(w[b], 12)
    w[a] += w[b]
    w[a] &= 0xFFFFFFFF
    w[d] ^= w[a]
    w[d] = rotate_left(w[d],  8)
    w[c] += w[d]
    w[c] &= 0xFFFFFFFF
    w[b] ^= w[c]
    w[b] = rotate_left(w[b],  7)

def round_pair(w):
    quarter_round(w,  0,  4,  8, 12)
    quarter_round(w,  1,  5,  9, 13)
    quarter_round(w,  2,  6, 10, 14)
    quarter_round(w,  3,  7, 11, 15)
    quarter_round(w,  0,  5, 10, 15)
    quarter_round(w,  1,  6, 11, 12)
    quarter_round(w,  2,  7,  8, 13)
    quarter_round(w,  3,  4,  9, 14)

def two_rounds(s):
    w = s_to_w(s)
    round_pair(w)
    round_pair(w)
    return w_to_s(w)

def quad_rounds(s):
    w = s_to_w(s)
    round_pair(w)
    round_pair(w)
    round_pair(w)
    round_pair(w)
    return w_to_s(w)

def sxor(x, y):
    return bytes(bytearray(a ^ b for a, b in zip(bytearray(x), bytearray(y))))

def s_to_w(s):
    return list(unpack(b'<'+(b'I'*(len(s)//4)), s))

def w_to_s(w):
    return pack(b'<'+(b'I'*len(w)), *w)

def s_to_q(s):
    return list(unpack(b'<'+(b'Q'*(len(s)//8)), s))

def q_to_s(w):
    return pack(b'<'+(b'Q'*len(w)), *w)

def add_qwords(h0, h1):
    return q_to_s([(a + b) & 0xFFFFFFFFFFFFFFFF for a,b in zip(s_to_q(h0), s_to_q(h1))])

def mix_in(h, s):
    def mix_partial(h, partial):
        assert len(partial) <= 0x40
        b = bytearray(h)
        for i, c in enumerate(partial[::-1]):
            b[i] ^= ord('%c' % c)
        return quad_rounds(bytes(b))

    while s != b'':
        h = mix_partial(h, s[:0x40])
        s = s[0x40:]

    return h

def filename_hash(s):
    # Generate initial hash from the string
    h0 = mix_in(b'\x00'*0x40, s)

    # Advance h0 by four round pairs to get h1
    h1 = quad_rounds(h0)
    # Add the two together, and advance by four round pairs.
    key = quad_rounds(add_qwords(h0, h1))

    # Do keyed hashing
    # NOTE: This appears to be an implementation mistake on the Spelunky 2 dev's part
    # They generate a quad_round advanced version of (nonce'd key), but then they
    # xor with the untweaked key instead of the tweaked key...
    h = b''
    for i in range(0, len(s), 0x40):
        partial = s[i:i+0x40]
        h += sxor(partial, key[:len(partial)][::-1])
    return h

def decrypt_data(s, data):
    # Untweaked key begins as half-advanced "0xBABE"
    h = two_rounds(pack(b'<QQQQQQQQ', 0xBABE, 0, 0, 0, 0, 0, 0, 0))

    # Mix the filename in to tweak the key
    for i in range(0, len(s), 0x40):
        partial = s[i:i+0x40]
        h = quad_rounds(sxor(h[:len(partial)], partial[::-1]) + h[len(partial):])

    # Add the tweaked key and its advancement, then advance by four round pairs.
    key = quad_rounds(add_qwords(h, quad_rounds(h)))

    # NOTE: This appears to be an implementation mistake on the Spelunky 2 dev's part
    # They generate a quad_round advanced version of (nonce'd key), but then they
    # xor with the untweaked key instead of the tweaked key...
    dec = b''
    if len(data) >= 0x40:
        blocks = len(data) // 0x40
        dec += sxor(data, key[::-1] * blocks)
        data = data[blocks * 0x40:]
    if len(data) > 0:
        dec += sxor(data, key[:len(data)][::-1])

    cctx = zstd.ZstdDecompressor()
    decompressed = cctx.decompress(dec)
    return decompressed
