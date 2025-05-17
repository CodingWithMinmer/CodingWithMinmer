from typing import List


def merge_56_python(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    result = []
    for curr_interval in intervals:
        if not result or curr_interval[0] > result[-1][1]:
            result.append(curr_interval)
        else:
            result[-1][1] = max(curr_interval[1], result[-1][1])

    return result
