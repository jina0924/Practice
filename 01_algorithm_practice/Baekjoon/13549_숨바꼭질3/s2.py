# 백준 13549번 숨바꼭질3

import sys
sys.stdin = open('input2.txt')
import heapq


def dijkstra():
    heap = []                           # 최소 거리 위주로 뽑아오기 위해 힙 사용
    heapq.heappush(heap, (0, N))        # (걸린 시간, 수빈이 위치)를 힙에 담음

    while heap:
        w, v = heapq.heappop(heap)      # w: v로 오기까지 걸린 시간, v: 좌표값
        if not visited[v]:              # 아직 방문하지 않은 곳이라면 방문 체크 & 거리 갱신
            visited[v] = 1
            dist[v] = w
        if v == K:                      # 주의! 방문 체크 전에 동생 위치 먼저 확인하지 말 것(거리 갱신 되지 않았으니까)
            return dist[K]
        left, right, doubleV = v - 1, v + 1, v * 2
        if 0 <= left <= 100000 and not visited[left]:
            heapq.heappush(heap, (w + 1, left))
        if 0 <= right <= 100000 and not visited[right]:
            heapq.heappush(heap, (w + 1, right))
        if 0 <= doubleV <= 100000 and not visited[doubleV]:
            heapq.heappush(heap, (w, doubleV))      # 순간이동은 0초 걸리므로 현재 위치랑 동일한 가중치로 힙에 넣음


N, K = map(int, input().split())        # N: 수빈이의 위치, K: 동생의 위치
dist = [987987987] * 100001             # 거리 정보 담을 리스트
dist[N] = 0
visited = [0] * 100001                  # 방문 체크 리스트
if K < N:                               # K가 N보다 앞에 있다면 뒷걸음질밖에 못하므로 다익스트라 쓸 필요x
    print(N-K)
else:
    print(dijkstra())
