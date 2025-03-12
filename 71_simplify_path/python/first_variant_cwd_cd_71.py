class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for directory in path.split("/"):
            if directory == "..":
                if len(result) > 0:
                    result.pop()
            elif directory and directory != ".":
                result.append(directory)
        return "/" + "/".join(result)

    def applyChange(self, cwd: str, cd: str) -> str:
        if not cd:
            return cwd

        if cd.startswith("."):
            return self.simplifyPath(cwd + cd)
        return self.simplifyPath(cd)


if __name__ == "__main__":
    solution = Solution()
    assert solution.applyChange("/a/b/c", "/d/./e") == "/d/e"
    assert solution.applyChange("", "/d/./e") == "/d/e"
    assert solution.applyChange("/a/b/c", "") == "/a/b/c"
    assert solution.applyChange("/a/b", ".//c/../../d/f") == "/a/d/f"
