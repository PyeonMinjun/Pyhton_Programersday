""" 레이저 포인터
문제
2차원 좌표 평면 (x1, y1) 에 레이저 포인터가 위치해 있다. 레이저 포인터는 상하좌우 방향 중 한 방향으로 레이저를 발사할 수 있고, 레이저는 발사한 방향으로 영원히 뻗어나간다.

레이저 포인터로 (x2, y2) 에 위치한 물체를 맞히려고 한다. 만약 직접적으로 레이저 포인터로 맞힐 수 없다면 2차원 좌표 평면에 아무 곳에나 대각선으로 비스듬히 거울을 설치할 수 있다. 레이저는 거울에 부딪힌 후에 진행 방향이 바뀐다.
1.png
2.png
예를 들어 위 그림과 같은 예시에서 (1, 4) 위치에 비스듬히 거울을 설치하면 레이저로 물체를 맞힐 수 있다.

레이저로 물체를 맞히기 위해 필요한 최소의 거울 개수는 얼마일까?

입력
첫째 줄에 정수 x1, y1, x2, y2 (1 ≤ x1, y1, x2, y2 ≤ 100) 이 주어진다. 두 위치는 서로 다르다.

출력
레이저로 물체를 맞히기 위해 설치 해야하는 최소 거울 개수를 출력한다.

예제 입력 1
1 2 4 4
예제 출력 1
1
예제 입력 2
4 2 2 4
예제 출력 2
1
3.png
(4, 4) 에 거울을 위와 같이 설치하면 된다.

예제 입력 3
5 3 1 3
예제 출력 3
0
4.png
거울을 설치하지 않고 물체를 맞힐 수 있다. """

x1,y1,r1,r2 = (map(int,input().split()))

if x1 == r1 or y1 == r2:
    print(0)
    
else:
    print(1)
    
