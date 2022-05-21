from typing import List


class KahnAlgorithms:

    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> List:
        adj_list = {}

        indegree = [0] * numCourses
        for prerequisite in prerequisites:
            if prerequisite[0] in adj_list:
                adj_list[prerequisite[0]].append(prerequisite[1])
            else:
                adj_list[prerequisite[0]] = [prerequisite[1]]
            indegree[prerequisite[1]] += 1

        topo_sorted = []
        queue = []
        index = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                indegree[i] = -1

        while queue:

            node = queue.pop(0)
            topo_sorted.insert(0, node)
            index += 1

            if node not in adj_list:
                continue

            for v in adj_list[node]:
                if indegree[v] == 1:
                    queue.append(v)
                    indegree[v] = -1
                else:
                    indegree[v] -= 1

        if index != numCourses:
            raise ValueError("Graph is not a valid DAG")

        return topo_sorted


if __name__ == '__main__':
    num_courses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(KahnAlgorithms.canFinish(numCourses=num_courses, prerequisites=prerequisites))
