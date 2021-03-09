def findCommon(array1, array2):
  common = set()
  pointer1 = 0
  pointer2 = 0
  while len(array1) > pointer1 and len(array2) > pointer2:
    if array1[pointer1] == array2[pointer2]:
        common.add(array1[pointer1])
        pointer1 += 1
        pointer2 += 1
    elif array1[pointer1] > array2[pointer2]:
        pointer2 += 1
    else:
        pointer1 += 1
  return common

def testFindCommon():
    testFindCommonEmpty()
    testFindCommonSame()
    testFindCommonDifferentLengths()
    testFindCommonSwitchingSides()
    testFindCommonString()

def testFindCommonEmpty():
    common = findCommon([], [1,3,4,5,8,8,9])
    assert len(common) == 0

def testFindCommonSame():
    arr1 = [1,3,4,5,8,9]
    arr2 = [1,3,4,5,8,9]
    common = findCommon(arr1, arr2)
    assert len(common) == len(arr1) and len(common) == len(arr2)
    for i in common:
        assert i in [1,3,4,5,8,9]

def testFindCommonSameWithDuplicates():
    arr1 = [1,3,4,5,8,8,9]
    arr2 = [1,3,4,5,8,8,9]
    common = findCommon(arr1, arr2)
    assert len(common) == len(arr1) - 1 and len(common) == len(arr2) - 1
    for i in common:
        assert i in [1,3,4,5,8,9]

def testFindCommonDifferentLengths():
    arr1 = [1,3,4,5,8,10]
    arr2 = [1,3,4,5,8,8,9,10]
    common = findCommon(arr1, arr2)
    assert len(common) == 6
    for i in common:
        assert i in [1,3,4,5,8,10]

def testFindCommonSwitchingSides():
    arr1 = [1,3,4,5,8,10]
    arr2 = [1,3,4,5,7,8,9,10]
    common1 = findCommon(arr1, arr2)
    common2 = findCommon(arr2, arr1)
    assert len(common1) == len(common2)
    for i in common1:
        assert i in [1,3,4,5,8,10]
    for i in common2:
        assert i in [1,3,4,5,8,10]

def testFindCommonString():
    arr1 = ['a','b','d']
    arr2 = ['c','d']
    common = findCommon(arr1, arr2)
    assert len(common) == 1
    for i in common:
        assert i in ['d']

testFindCommon()
