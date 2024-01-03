def longestPalindrome(s):
    if len(s) <= 1:
        return s

    longest = s[0]

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            substring = s[i : j + 1]
            reversed_substring = s[i : j + 1][::-1]
            if substring == reversed_substring and len(longest) < len(substring):
                longest = substring

    return longest


def longestPalindrome2(s):
    if s == s[::-1]:
        return s

    left = longestPalindrome2(s[1:])
    right = longestPalindrome2(s[:-1])

    if len(left) > len(right):
        return left
    else:
        return right


print(longestPalindrome2("aabbcbb"))
