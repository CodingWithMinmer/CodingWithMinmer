def removeDuplicates(s):
    result = []
    for ch in s:
        if not result or result[-1] != ch:
            result.append(ch)
        else:
            result.pop()

    return "".join(result)
