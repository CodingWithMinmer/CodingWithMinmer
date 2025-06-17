#pragma once
#include <string>
#include <iostream>
#include <vector>

// VARIANT: What if you had to print all the paths using backtracking? No DP.
class Solution62Variant_PrintPaths {
public:
    void backtrack(std::string& path, int n, int row, int col) {
        if (row >= n || col >= n)
            return;
        if (row == n - 1 && col == n - 1) {
            std::cout << path << std::endl;
            return;
        }

        path.push_back('R');
        backtrack(path, n, row, col + 1);
        path.pop_back();

        path.push_back('D');
        backtrack(path, n, row + 1, col);
        path.pop_back();
    }

    void print_unique_paths(int n) {
        std::string path;
        backtrack(path, n, 0, 0);
    }
};

// VARIANT: What if you had to print all the paths using backtracking? No DP.
class Solution62Variant_ReturnPaths {
public:
    void backtrack(std::vector<std::string>& result, std::string& path, int n, int row, int col) {
        if (row >= n || col >= n)
            return;
        if (row == n - 1 && col == n - 1) {
            result.push_back(path);
            return;
        }

        path.push_back('R');
        backtrack(result, path, n, row, col + 1);
        path.pop_back();

        path.push_back('D');
        backtrack(result, path, n, row + 1, col);
        path.pop_back();
    }

    std::vector<std::string> get_unique_paths(int n) {
        std::string path;
        std::vector<std::string> result;
        backtrack(result, path, n, 0, 0);
        return result;
    }
};