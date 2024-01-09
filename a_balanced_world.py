while 1:
    stack = []
    flag = 0
    opener = "(["
    closer = ")]"
    pair = {")": "(", "]": "["}
    string = input()

    if string == ".":
        break

    for char in string:
        if char in opener:
            stack.append(char)
        elif char in closer:
            if not stack:
                print("no")
                flag = 1
                break
            top = stack.pop()
            if pair[char] != top:
                print("no")
                flag = 1
                break

    if flag == 0:  # no가 출력되지 않았을 때
        if not stack:
            print("yes")
        else:
            print("no")
