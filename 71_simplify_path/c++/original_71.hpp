#pragma once

#include <string>
#include <sstream>
#include <stack>

std::string simplifyPath(std::string path) {
    std::stack<std::string> tokens;
    std::stringstream ss(path);
    std::string token;
    while (std::getline(ss, token, '/')) {
        if (token.empty())
            continue;

        if (token == ".")
            continue;

        if (token == "..") {
            if (tokens.empty())
                continue;
            tokens.pop();
        }
        else {
            tokens.push(token);
        }
    }

    if (tokens.empty())
        return "/";

    std::string result;
    while (!tokens.empty()) {
        result = '/' + tokens.top() + result;
        tokens.pop();
    }
    return result;
}