import sys

vertexNum, edgeNum = map(int, input().rstrip().split(' '))
roads = [[10001]*vertexNum for i in range(vertexNum)]

for _ in range(edgeNum):
    start, end, cost = map(int, input().rstrip().split(' '))
    roads[start - 1][end - 1] = cost
    
for k in range(vertexNum): 
    for i in range(vertexNum): 
        for j in range(vertexNum):
            roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])

minCycle = 10001;
for i in range(vertexNum):
    minCycle = min(roads[i][i], minCycle)

if minCycle==10001:
    print(-1) 

print(minCycle)