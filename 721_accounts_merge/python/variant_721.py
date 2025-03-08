from collections import defaultdict


class Solution:
    def accountsMerge(self, entries: list[dict[str, list[str]]]) -> list[list[str]]:
        # An entry is of form {"C1": ["a", "b"]} or {"C7": ["a"]}
        adj = defaultdict(list)
        email_to_ids = defaultdict(
            list
        )  # Stores mapping of email to list of ID, eg: "a": ["C1", "C7"], "b": ["C1"]
        for entry in entries:
            for id, emails in entry.items():
                canonical = emails[0]
                email_to_ids[canonical].append(id)
                for email in emails[1:]:
                    email_to_ids[email].append(id)
                    adj[canonical].append(email)
                    adj[email].append(canonical)

        visited = set()  # Visited set of emails

        def dfs(email: str, same_emails: list[str]):
            visited.add(email)
            same_emails.append(email)
            for nei in adj[email]:
                if nei not in visited:
                    dfs(nei, same_emails)

        res = []

        for email in email_to_ids:
            if email in visited:
                continue
            same_emails = []
            dfs(email, same_emails)
            id_set = set()
            for same_email in same_emails:
                id_set.update(email_to_ids[same_email])
            res.append(list(id_set))
        return res


if __name__ == "__main__":
    solution = Solution()
    entries = [
        {"C1": ["a", "b"]},
        {"C2": ["c"]},
        {"C3": ["b", "d"]},
        {"C4": ["d"]},
        {"C5": ["e"]},
        {"C6": ["c"]},
        {"C7": ["a"]},
    ]
    actual = [sorted(entry) for entry in solution.accountsMerge(entries)]
    expected = [["C1", "C3", "C4", "C7"], ["C2", "C6"], ["C5"]]
    assert actual == expected
