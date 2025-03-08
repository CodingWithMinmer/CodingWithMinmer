from typing import List

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create adjacency list
        adj = defaultdict(list)
        for account in accounts:
            emails = account[1:]
            canonical = emails[0]
            for email in emails[1:]:
                adj[canonical].append(email)
                adj[email].append(canonical)

        visited = set()

        def dfs(email, same_emails: List[str]):
            visited.add(email)
            same_emails.append(email)
            for nei in adj[email]:
                if nei not in visited:
                    dfs(nei, same_emails)

        # Merge
        merged = []
        for account in accounts:
            emails = account[1:]
            if emails[0] in visited:
                continue
            same_emails = []
            dfs(emails[0], same_emails)
            merged.append([account[0]] + sorted(same_emails))

        return merged
