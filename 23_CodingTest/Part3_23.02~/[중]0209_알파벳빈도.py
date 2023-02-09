"""
알파벳 빈도
문제
길이가 N 인 문자열 S 가 주어질 때, 이 문자열의 L 번째 문자부터 R 번째 문자까지 알파벳 소문자 'e' 가 몇 번 등장했는지 구해보자.

힌트
문자열 S 를 수열로 바꿔서 저장할 수 있다. 문자열의 i 번째 문자가 'e' 라면 1 로 그렇지 않다면 0 으로 바꾸면 똑같이 길이가 N 인 수열 F 를 만들 수 있다. 예를 들어 문자열 seventeen 을 위와 같은 과정으로 수열로 바꾸면 [0, 1, 0, 1, 0, 0, 1, 1, 0] 이 된다.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 100), M (1 ≤ M ≤ 10 000) 이 주어진다.

둘째 줄에 알파벳 소문자로 이루어진 문자열 S 가 주어진다.

셋째 줄부터 M 개의 줄에 L, R (1 ≤ L ≤ R ≤ N) 이 주어진다.

출력
M 개의 줄에 문자열의 L 번째 문자부터 R 번째 문자까지 알파벳 소문자 'e' 가 몇 번 등장했는지 출력한다.

예제 입력 1
3 6
yee
1 1
1 2
1 3
2 2
2 3
3 3
예제 출력 1
0
1
2
1
2
1
"""
n, m = map(int,input().split())

text = (input())
text = list((''.join(text)))


arr = [0] * len(text)

cnt = -1
for i in text:
    cnt += 1
    if i == 'e':
       arr[cnt] = 1 # [0,1,1]

for i in range(m):
    L,R= map(int,input().split()) 
    e_cnt = arr[L-1:R]
    # print(e_cnt)
    print(e_cnt.count(1))