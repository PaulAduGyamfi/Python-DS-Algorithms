def solve(nums: List[int], target: int) -> List[int]:
    """
    Function that returns the indeces of first pair of values in 
    a list that are complements of the given target
    """
    seen = {}
    for index, value in enumerate(nums):
        if target - value in seen:
            return [seen[target - value], index]
        seen[value] = index
    return []

if __name__ == "__main__":
    assert solve([1,5,7,2,11], 12) == [1,2]
    assert solve([2,2], 4) == [0,1]
    assert solve([], 3) == []
    print(" 🎉 All tests passed successfully!")