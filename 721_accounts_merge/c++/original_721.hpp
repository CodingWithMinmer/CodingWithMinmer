#pragma once

#include <vector>
#include <unordered_map>
#include <unordered_set>


void dfs(std::unordered_map<std::string, std::vector<std::string>>& adjs,
    std::unordered_set<std::string>& visited,
    std::vector<std::string>& same_emails, 
    std::string curr_email) {
    visited.insert(curr_email);
    same_emails.push_back(curr_email);

    for (auto adj : adjs[curr_email])
        if (!visited.contains(adj))
            dfs(adjs, visited, same_emails, adj);
}
std::vector<std::vector<std::string>> accountsMerge(std::vector<std::vector<std::string>>& accounts) {
    std::unordered_map<std::string, std::vector<std::string>> adjs;
    for (auto emails : accounts) {
        std::string first_email = emails[1];
        for (int i = 2; i < emails.size(); i++) {
            adjs[first_email].push_back(emails[i]);
            adjs[emails[i]].push_back(first_email);
        }
    }
    
    std::vector<std::vector<std::string>> result;
    std::unordered_set<std::string> visited;
    for (auto emails : accounts) {
        std::string first_email = emails[1];
        if (!visited.contains(first_email)) {
            std::vector<std::string> same_emails;
            same_emails.push_back(emails[0]);
            dfs(adjs, visited, same_emails, first_email);
            std::sort(same_emails.begin() + 1, same_emails.end());
            result.push_back(same_emails);
        }
    }

    return result;
}