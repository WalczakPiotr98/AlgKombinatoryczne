# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def findCombinationsUtil(arr, index, num,
                             reducedNum):
        if (reducedNum < 0):
            return
        if (reducedNum == 0):
            for i in range(index):
                print(arr[i], end=" ")
            print()
            return
        prev = 1 if (index == 0) else arr[index - 1]
        for k in range(prev, num + 1):
            arr[index] = k
            findCombinationsUtil(arr, index + 1, num, reducedNum - k)

    def findCombinations(n):
        arr = [0] * n
        findCombinationsUtil(arr, 0, n, n)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i,cur,total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0,[],0)
        print(res)
        return res
    n = 6;
    findCombinations(n);
    print("-----------------------------------")
    combinationSum(0, [2, 4, 6], n)
