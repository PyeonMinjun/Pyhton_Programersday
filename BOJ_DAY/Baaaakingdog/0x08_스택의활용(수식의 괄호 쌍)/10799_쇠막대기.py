s = input()
ans = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if i > 0 and s[i - 1] == '(':  # 레이저일 경우
            stack.pop()  # 앞에서 막대라고 착각하고 스택에 s[i]를 넣었으므로 pop
            ans += len(stack)  # 막대의 개수만큼 ans에 추가
        else:  # 막대의 끝일 경우
            stack.pop()  # 막대의 개수를 1 감소
            ans += 1  # 막대 1개가 절단된 것과 동일한 상황이므로 ans에 1 추가

print(ans)
