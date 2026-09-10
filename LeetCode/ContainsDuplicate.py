def containsDuplicate(numbers: List[int]) -> bool:
    """
    A function that returns true if there are duplicates in a gicen list and flase if none
    """
    setList = set()
    for num in numbers:
        if num not in setList:
            setList.add(num)
        else:
            return True
    return False

if __name__ == "__main__":
    assert containsDuplicate([1,5,3,4,6,2,4,5]) == True
    assert containsDuplicate([2,4,5,6,7]) == False
    assert containsDuplicate([]) == False
    print(" 🎉 All tests passed successfully!")