#pragma once

#include <string>

class Solution_408_Variant {
    bool recurse(std::string& word, std::string& abbr, int w, int a)
    {
        if (w == word.size() && a == abbr.size())
            return true;
        if (w < word.size() && a == abbr.size())
            return false;
        if (w == word.size() && a < abbr.size()) {
            for (int i = a; i < abbr.size(); i++)
                if (abbr[i] != '*')
                    return false;
            return true;
        }

        if (std::isdigit(abbr[a])) {
            int skip = 0;
            while (a < abbr.size() && std::isdigit(abbr[a]))
            {
                skip = skip * 10 + abbr[a] - '0';
                a++;
            }
            w += skip;
            if (w > word.size())
                return false;
            return recurse(word, abbr, w, a);
        }

        if (abbr[a] == '*')
            return recurse(word, abbr, w, a + 1) ||
                   recurse(word, abbr, w + 1, a);

        if (word[w] == abbr[a])
            return recurse(word, abbr, w + 1, a + 1);
        return false;
    }
public:
    bool validWordAbbreviation(std::string& word, std::string& abbr) {
        return recurse(word, abbr, 0, 0);
    }
};