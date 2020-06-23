def solution(heights):
    temp_list = [0] * len(heights)
    while heights:
        right = heights.pop()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > right:
                temp_list[len(heights)] = i + 1
                break
    return temp_list

solution([6, 9, 5, 7, 4])
print(solution([6, 9, 5, 7, 4]))