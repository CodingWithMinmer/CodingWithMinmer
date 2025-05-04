#pragma once

#include <string>
#include <vector>

bool validWordAbbreviation(std::string word, std::string abbr) {
    int a = 0, w = 0;
    while (a < abbr.size() && w < word.size()) {
        if (abbr[a] == word[w]) {
            a++;
            w++;
            continue;
        }
        if (!std::isdigit(abbr[a]) && abbr[a] != word[w])
            return false;

        if (abbr[a] == '0')
            return false;

        int skip = 0;
        while (a < abbr.size() && std::isdigit(abbr[a])) {
            skip = skip * 10 + (abbr[a] - '0');
            a++;
        }
        w += skip;
    }

    return a == abbr.size() && w == word.size();
}

