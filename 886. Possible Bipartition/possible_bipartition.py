from collections import defaultdict


def possibleBipartition(n: int, dislikes: List[List[int]]) -> bool:
    # Construct the graph
    graph = defaultdict(list)
    for dislike in dislikes:
        a, b = dislike
        graph[a].append(b)
        graph[b].append(a)

    # Assign a group to each person
    groups = {}
    for i in range(1, n+1):
        if i not in groups:
            groups[i] = 0
            queue = [i]
            while queue:
                person = queue.pop(0)
                for neighbor in graph[person]:
                    if neighbor in groups:
                        # If the neighbor is already in a group, make sure it's not in the same group as the current person
                        if groups[neighbor] == groups[person]:
                            return False
                    else:
                        # If the neighbor is not yet in a group, assign it to the opposite group
                        groups[neighbor] = 1 - groups[person]
                        queue.append(neighbor)
    return True
