import math
from collections import defaultdict

class Solution:
    def minimum_stickers_for_poster(self, sticker, poster):
        sticker_freqs = defaultdict(int)
        for letter in sticker:
            sticker_freqs[letter] += 1

        poster_freqs = defaultdict(int)
        for letter in poster:
            poster_freqs[letter] += 1

        count = 0
        for letter, freq in poster_freqs.items():
            if letter not in sticker_freqs:
                return -1
            count = max(count, math.ceil(freq / sticker_freqs[letter]))

        return count