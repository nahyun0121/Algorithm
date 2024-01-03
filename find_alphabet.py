import string


# O(n^2)
def get_index(S):
    result = [-1] * len(string.ascii_lowercase)
    for i in range(len(S)):
        char = S[i]
        for j in range(len(string.ascii_lowercase)):
            alpha = string.ascii_lowercase[j]
            if result[j] == -1 and char == alpha:
                result[j] = i
    print(" ".join([str(num) for num in result]))


# O(n)
def get_index2(S):
    # ord: 문자 -> 숫자로 바꿔줌. a -> 97, b -> 98, ...
    result = [-1] * len(string.ascii_lowercase)
    for i in range(len(S)):
        idx = ord(S[i]) - 97  # 주어진 문자열의 각 문자의 알파벳 인덱스 구하기
        if result[idx] == -1:
            result[idx] = i
    print(" ".join([str(num) for num in result]))


get_index2(input())
