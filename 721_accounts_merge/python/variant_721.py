from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        def dfs_variant_721(adjs, email_to_id, visited, curr_email, id):
            visited.add(curr_email)
            email_to_id[curr_email] = id
            for adj in adjs.get(curr_email, []):
                if adj not in visited:
                    dfs_variant_721(adjs, email_to_id, visited, adj, id)

        # Create adjacency list
        adjs = {}
        for id, emails in accounts.items():
            first_email = emails[0]
            for email in emails[1:]:
                if first_email not in adjs:
                    adjs[first_email] = []
                if email not in adjs:
                    adjs[email] = []
                adjs[first_email].append(email)
                adjs[email].append(first_email)

        # Helper structures
        email_to_id = {}
        visited = set()
        result = {}

        # Perform DFS and group by connected components
        for id, emails in accounts.items():
            first_email = emails[0]
            if first_email in visited:
                same_id = email_to_id[first_email]
                if same_id not in result:
                    result[same_id] = []
                result[same_id].append(id)
            else:
                result[id] = []
                dfs_variant_721(adjs, email_to_id, visited, first_email, id)

        # Prepare result as a list of lists
        result_v2 = []
        for id, same_ids in result.items():
            same = [id] + same_ids
            result_v2.append(same)

        return result_v2


if __name__ == "__main__":
    # Happy Case
    solution = Solution()
    input_data = {
        "C1": ["a", "b"],
        "C2": ["c"],
        "C3": ["b", "d"],
        "C4": ["d"],
        "C5": ["e"],
        "C6": ["c"],
        "C7": ["a"],
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["C1", "C3", "C7", "C4"])
    assert sorted(result[1]) == sorted(["C6", "C2"])
    assert sorted(result[2]) == sorted(["C5"])

    # Actual Email Strings
    input_data = {
        "ID1": ["aa@gmail.com", "bb@gmail.com"],
        "ID2": ["cc@gmail.com"],
        "ID3": ["bb@gmail.com", "dd@gmail.com"],
        "ID4": ["dd@gmail.com"],
        "ID5": ["ee@gmail.com"],
        "ID6": ["cc@gmail.com"],
        "ID7": ["aa@gmail.com"],
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["ID3", "ID7", "ID4", "ID1"])
    assert sorted(result[1]) == sorted(["ID2", "ID6"])
    assert sorted(result[2]) == sorted(["ID5"])

    # No Edges
    input_data = {
        "C1": ["a", "b"],
        "C2": ["c"],
        "C3": ["d", "e", "f"],
        "C4": ["g"],
        "C5": ["h"],
        "C6": ["i"],
        "C7": ["j", "k", "l", "m", "n"],
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 7
    assert sorted(result[0]) == sorted(["C1"])
    assert sorted(result[1]) == sorted(["C2"])
    assert sorted(result[2]) == sorted(["C3"])
    assert sorted(result[3]) == sorted(["C4"])
    assert sorted(result[4]) == sorted(["C5"])
    assert sorted(result[5]) == sorted(["C6"])
    assert sorted(result[6]) == sorted(["C7"])

    # One Connected Component Via One Email
    input_data = {
        "C1": ["a", "b"],
        "C2": ["a"],
        "C3": ["d", "a", "f"],
        "C4": ["a"],
        "C5": ["a"],
        "C6": ["a"],
        "C7": ["j", "a", "l", "m", "n"],
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C6", "C1", "C5", "C3", "C7", "C2", "C4"])

    # One Connected Component Via Two Emails
    input_data = {
        "C1": ["a", "b"],
        "C2": ["a"],
        "C3": ["d", "a", "f"],
        "C4": ["a", "x", "y", "z"],
        "C5": ["a"],
        "C6": ["a", "o", "p", "b"],
        "C7": ["j", "a", "l", "m", "n"],
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C6", "C1", "C5", "C3", "C7", "C2", "C4"])

    # One Id One Email
    input_data = {"C1": ["a"]}
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C1"])

    # One Id Multiple Emails
    input_data = {"C1": ["a@gmail.com", "b@gmail.com", "c@gmail.com"]}
    result = solution.accountsMerge(input_data)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["C1"])

    # Separate Connected Components
    input_data = {
        "C1": ["a", "b", "c", "d"],
        "C2": ["q", "r", "s", "t"],
        "C10": ["x", "y", "z"],
    }
    result = solution.accountsMerge(input_data)
    assert len(result) == 3
    assert sorted(result[0]) == sorted(["C1"])
    assert sorted(result[1]) == sorted(["C2"])
    assert sorted(result[2]) == sorted(["C10"])
