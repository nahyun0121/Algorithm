def groupAnagrams(strs):
    anagram = {}

    for word in strs:
        represent = "".join(sorted(word))  # 정렬 후 다시 문자열로 바꿔줌(아래 줄을 위해)
        if represent in anagram:
            anagram[represent].append(word)
        else:
            anagram[represent] = [word]

    return list(anagram.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
