#include <vector>
#include <stack>
#include <sstream>

std::vector<int> exclusiveTime_636(int n, std::vector<std::string>& logs) {
    struct function {
        int id;
        int timestamp;
    };
    std::vector<int> result(n, 0);
    std::stack<function> stack;
    int prev = 0;
    for (std::string& log : logs) {
        std::string id_str;
        std::string timestamp_str;
        std::string start;

        std::stringstream ss(log);
        std::getline(ss, id_str, ':');
        std::getline(ss, start, ':');
        std::getline(ss, timestamp_str, ':');

        int id = std::stoi(id_str);
        int time = std::stoi(timestamp_str);
        if (start == "start") {
            if (!stack.empty())
                result[stack.top().id] += time - prev;
            stack.push(function{id});
            prev = time;
        }
        else {
            stack.pop();
            result[id] += time + 1 - prev;
            prev = time + 1;
        }
    }

    return result;
}
