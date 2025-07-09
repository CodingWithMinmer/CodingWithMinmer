#pragma once

#include <vector>
#include <stack>
#include <string>

struct Log {
    std::string function_name;
    std::string type;
    int timestamp;
};
class Solution636_Variant {
public:
    std::unordered_map<std::string, int> profile_app(std::vector<Log>& logs) {
        std::unordered_map<std::string, int> result;
        std::stack<std::string> stack;
        int prev = 0;
        for (Log& log : logs) {
            if (log.type == "start") {
                if (!stack.empty())
                    result[stack.top()] += log.timestamp - prev;
                stack.push(log.function_name);
            }
            else {
                stack.pop();
                result[log.function_name] += log.timestamp - prev;
            }
            prev = log.timestamp;
        }
    
        return result;
    }
};