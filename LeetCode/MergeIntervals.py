def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda interval: interval[0])
    merge = []

    for interval in intervals:
        if not merge or merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1] = [merge[-1][0], max(merge[-1][1], interval[1])]

    return merge

if __name__ == "__main__":
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
    assert merge_intervals([[4,7],[1,4]]) == [[1,7]]
    print(" 🎉 All tests passed successfully!")