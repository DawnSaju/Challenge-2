def Solution(numCourses, prerequisites):
    var1 = [[] for i in range(numCourses)]
    var2 = [0 for i in range(numCourses)]
    for pairs in prerequisites:
        x, y = pairs
        var1[x].append(y)
    for i in range(numCourses):
        if not Func1(var1, var2, i):
            return False
    return True


def Func1(var1, var2, i):
    if var2[i] == -1:
        return False
    if var2[i] == 1:
        return True
    var2[i] = -1
    for j in var1[i]:
        if not Func1(var1, var2, j):
            return False
    var2[i] = 1
    return True

# Example 1
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print("numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]")
print(Solution(numCourses, prerequisites))


# Example 2
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print("\nnumCourses = 2, prerequisites = [[1, 0], [0, 1]]")
print(Solution(numCourses, prerequisites))
