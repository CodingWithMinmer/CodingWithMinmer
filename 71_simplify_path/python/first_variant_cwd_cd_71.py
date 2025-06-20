class Solution:
    def changeDirectory(self, cwd: str, cd: str) -> str:
        
        if not cd: return cwd
        if cd[0] == '/':
            cwd = ''
        relativePaths = ['..','','.']
        dirPath = []

        for p in cwd.split('/'):
            if p not in relativePaths:
                dirPath.append(p)

        for p in cd.split('/'):
            if not p in relativePaths:
                dirPath.append(p)
            if p == '..' and dirPath:
                dirPath.pop()
        
        return '/'+'/'.join(dirPath)

if __name__ == "__main__":
    solution = Solution()
    assert solution.changeDirectory("/a/b/c", "/d/./e") == "/d/e"
    assert solution.changeDirectory("", "/d/./e") == "/d/e"
    assert solution.changeDirectory("/a/b/c", "") == "/a/b/c"
    assert solution.changeDirectory("/a/b", ".//c/../../d/f") == "/a/d/f"
    assert solution.changeDirectory("/", "foo") == "/foo"
    assert solution.changeDirectory("/", "foo/bar/././xyz///") == "/foo/bar/xyz"
    assert solution.changeDirectory("/baz", "/bar") == "/bar"
    assert solution.changeDirectory("/foo/bar", "../../../../..") == "/"
    assert solution.changeDirectory("/x/y", "../p/../q") == "/x/q"
    assert solution.changeDirectory("/x/y", "/p/./q") == "/p/q"
    assert solution.changeDirectory("/facebook/anin", "../abc/def") == "/facebook/abc/def"
    assert solution.changeDirectory("/facebook/instagram", "../../../../.") == "/"
    print('All Test Passed!!!')
