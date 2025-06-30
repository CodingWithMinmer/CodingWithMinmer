#pragma once

#include <vector>
#include <unordered_map>
#include <unordered_set>

// VARIANT: What if you were given the input as a map from an ID to a list of corresponding emails?
// Furthermore, you have to return a 2D list of all of the same IDs.
void dfs_variant_721(std::unordered_map<std::string, std::vector<std::string>>& adjs,
    std::unordered_map<std::string, std::string>& email_to_id,
    std::unordered_set<std::string>& visited,
    std::string curr_email,
    const std::string& id) {
    visited.insert(curr_email);
    email_to_id[curr_email] = id;
    for (auto adj : adjs[curr_email])
        if (!visited.contains(adj))
            dfs_variant_721(adjs, email_to_id, visited, adj, id);
}

std::vector<std::vector<std::string>> accountsMerge_variant_721(
    std::unordered_map<std::string, std::vector<std::string>>& accounts) {
    std::unordered_map<std::string, std::vector<std::string>> adjs;
    for (auto [id, emails] : accounts) {
        std::string first_email = emails[0];
        for (int i = 1; i < emails.size(); i++) {
            adjs[first_email].push_back(emails[i]);
            adjs[emails[i]].push_back(first_email);
        }
    }

    std::unordered_map<std::string, std::string> email_to_id;
    std::unordered_set<std::string> visited;
    std::unordered_map<std::string, std::vector<std::string>> result;
    for (auto [id, emails] : accounts) {
        std::string first_email = emails[0];
        if (visited.contains(first_email)) {
            std::string same_id = email_to_id[first_email];
            result[same_id].push_back(id);
        }
        else {
            result[id] = {};
            dfs_variant_721(adjs, email_to_id, visited, first_email, id);
        }
    }

    std::vector<std::vector<std::string>> result_v2;
    for (auto [id, same_ids] : result) {
        std::vector<std::string> same;
        same.push_back(id);
        for (auto same_id : same_ids)
            same.push_back(same_id);
        result_v2.push_back(same);
    }
    return result_v2;
}