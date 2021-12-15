from collections import defaultdict, deque
from pprint import pprint


def is_small(cave):
    return cave.islower()

with open("./input_12.txt") as fin:
    raw_data = fin.read().strip()
data = [i.split("-") for i in raw_data.split("\n")]
adj = defaultdict(list)
for a, b in data:
    adj[a].append(b)
    adj[b].append(a)

global ans
ans = 0
visited = defaultdict(int)

def dfs(cave):
    global ans

    if cave == "end":
        ans += 1
        return
    if is_small(cave):
        visited[cave] += 1
        more_than_once = 0  
        for small in visited:
            more_than_once += visited[small] > 1

            if visited[small] > 2:
                visited[cave] -= 1
                return

        if more_than_once > 1:
            visited[cave] -= 1
            return

    for nbr in adj[cave]:
        if nbr == "start":

            continue
        dfs(nbr)

    if is_small(cave):
        visited[cave] -= 1


dfs("start")

print(ans)