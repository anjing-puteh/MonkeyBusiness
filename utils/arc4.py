from Cryptodome.Cipher import ARC4
from Cryptodome.Hash import MD5


class EamuseARC4:
    def __init__(self, seconds, prng):
        self.internal_key = b"\x69\xD7\x46\x27\xD9\x85\xEE\x21\x87\x16\x15\x70\xD0\x8D\x93\xB1\x24\x55\x03\x5B\x6D\xF0\xD8\x20\x5D\xF5"
        self.key = MD5.new(seconds + prng + self.internal_key).digest()

    def decrypt(self, data):
        return ARC4.new(self.key).decrypt(bytes(data))

    def encrypt(self, data):
        return ARC4.new(self.key).encrypt(bytes(data))
