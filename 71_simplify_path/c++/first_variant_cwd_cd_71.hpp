#pragma once

#include <cassert>
#include <string>
#include <sstream>
#include <stack>

// VARIANT: What if you were given a new "cd" parameter to change where you currently
// were on your filesystem (represented by "cwd")? If "cd" starts with "/" then this has
// many implications on the code.
std::string change_directory(std::string cwd, std::string cd) {
    if (cd.empty())
        return cwd;
    if (cd[0] == '/')
        cwd = "";
    std::stack<std::string> tokens;
    std::string token;
    std::stringstream cwd_ss(cwd);
    while (std::getline(cwd_ss, token, '/')) {
        if (token.empty())
            continue;
        tokens.push(token);
    }

    std::stringstream cd_ss(cd);
    while (std::getline(cd_ss, token, '/')) {
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

void change_directory() {
    std::string cwd = "/";
    std::string destination = "foo";
    assert(change_directory(cwd, destination) == "/foo");

    cwd = "/";
    destination = "foo/bar/././xyz///";
    assert(change_directory(cwd, destination) == "/foo/bar/xyz");

    cwd = "/baz";
    destination = "/bar";
    assert(change_directory(cwd, destination) == "/bar");

    cwd = "/foo/bar";
    destination = "../../../../..";
    assert(change_directory(cwd, destination) == "/");

    cwd = "/x/y";
    destination = "../p/../q";
    assert(change_directory(cwd, destination) == "/x/q");

    cwd = "/x/y";
    destination = "/p/./q";
    assert(change_directory(cwd, destination) == "/p/q");

    cwd = "/facebook/anin";
    destination = "../abc/def";
    assert(change_directory(cwd, destination) == "/facebook/abc/def");

    cwd = "/facebook/instagram";
    destination = "../../../../.";
    assert(change_directory(cwd, destination) == "/");
}
