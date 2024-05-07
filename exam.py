class Solution:
    #Q1
    def getMinSubsequences(self, source, target) -> int:
        n = len(source)
        j = 0
        count = 0
        while j < len(target):
            prev = j
            for i in range(n):
                if j < len(target) and source[i] == target[j]:
                    j += 1
            if prev == j:
                return -1
            count += 1
        return count
    
    #Q2
    def check_parentheses(self, s) -> list:
        stack = []
        marks = [' '] * len(s)
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop() 
                else:
                    marks[i] = '?' 
        for index in stack:
            marks[index] = 'x'
        result = s + "\n" + ''.join(marks)
        return result

#test Q1
test_cases1 = [
    ["abc", "abcbc"],
    ["abc","acdbc"],
    ["xyz", "xzyxz"]
]
for s, t in test_cases1:
    print(Solution().getMinSubsequences(s,t))

#test Q2
test_cases2 = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]


for case in test_cases2:
    print(Solution().check_parentheses(case))

