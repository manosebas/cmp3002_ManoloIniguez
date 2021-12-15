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
visited = set()
def dfs(cave):
    global ans
    if cave == "end":
        ans += 1
        return
    if is_small(cave) and cave in visited:
        return
    if is_small(cave):
        visited.add(cave)
    for nbr in adj[cave]:
        if nbr == "start":

            continue
        dfs(nbr)


    if is_small(cave):
        visited.remove(cave)


dfs("start")


print(ans)