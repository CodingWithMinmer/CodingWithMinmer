#include <string>
#include <unordered_map>
#include <vector>
#include <cmath>

class StickersToCreatePosters {
public:
    int minimum_stickers_for_poster(std::string sticker, std::string poster) {
        std::unordered_map<char, int> sticker_freqs;
        for (char letter : sticker)
            sticker_freqs[letter]++;
    
        std::unordered_map<char, int> poster_freqs;
        for (char letter : poster)
            poster_freqs[letter]++;
    
        int count = 0;
        for (auto [letter, freq] : poster_freqs) {
            if (!sticker_freqs.contains(letter))
                return -1;
            count = std::max(count, (int)std::ceil(freq * 1.0 / sticker_freqs[letter]));
        }
    
        return count;
    }
};