# co353 project 1.2
import sys

def find_one_component_vertices(cost_one_matrix, vertices_reached, u, v):
    if u > v:
        u = u + v
        v = u - v
        u = u - v

    if cost_one_matrix[u][v] == False:
        return
    else:
        cost_one_matrix[u][v] = False
        vertices_reached[u] = 1
        vertices_reached[v] = 1
    
    for l in range(len(cost_one_matrix)):
        find_one_component_vertices(cost_one_matrix, vertices_reached, u, l)
    
    for m in range(len(cost_one_matrix)):
        find_one_component_vertices(cost_one_matrix, vertices_reached, m, v)


def calculate_one_subtrees(cost_one_matrix):
    cost_one_subtrees = []
    for i in range(len(cost_one_matrix)):
        for j in range(i+1,len(cost_one_matrix)):
            if cost_one_matrix[i][j] == True:
                vertices_reached = [0 for _ in range(len(cost_one_matrix))]
                find_one_component_vertices(cost_one_matrix, vertices_reached, i, j)
                cost_one_subtrees.append(sum(vertices_reached))

    return cost_one_subtrees


if __name__ == '__main__':
    first_line = sys.stdin.readline().strip()
    n, k = map(int, first_line.split())

    print('Number of vertices (n):', n)
    print('Edges of subtree (k):', k)

    cost_one_matrix = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(n^2):
        line = sys.stdin.readline().strip()
        u, v, c = map(int, line.split())
        if c == 1:
            cost_one_matrix[u][v] = True

    #print('Incidence matrix:', cost_one_matrix)

    cost_one_subtrees = calculate_one_subtrees(cost_one_matrix)

    cost_one_subtrees.sort(reverse=True)
    #print('Cost one subtrees:', cost_one_subtrees)

    total_cost = 0
    for i in range(len(cost_one_subtrees)):
        if (cost_one_subtrees[i] > k):
            total_cost += k
            break
        else:
            total_cost += cost_one_subtrees[i]
            k -= cost_one_subtrees[i]-1
    
    print('Total cost:', total_cost)

        