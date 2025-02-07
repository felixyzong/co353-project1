# co353 project 1.2
# python version: 3.11.5
import sys

# find_one_component_vertices(cost_one_matrix, vertices_reached, u, v) is a recursive function
#           that finds the vertices that edge u,v could reach in the subgraph of G with only cost 1 edges
# requires:
#           cost_one_matrix: n*n matrix of boolean value
#           vertices_reached: n list indicating whether vertex i is reached in currect component
#           u: vertex index, between 0 and n-1
#           v: vertex index, between 0 and n-1
def find_one_component_vertices(cost_one_matrix, vertices_reached, u, v):
    # swap u,v
    if u > v:
        u = u + v
        v = u - v
        u = u - v

    # check if current edge is of cost 1
    if cost_one_matrix[u][v] == False:
        return
    else:
        cost_one_matrix[u][v] = False
        vertices_reached[u] = 1
        vertices_reached[v] = 1
    
    # recursively search with u fixed
    for l in range(len(cost_one_matrix)):
        find_one_component_vertices(cost_one_matrix, vertices_reached, u, l)
    
    # recursively search with v fixed
    for m in range(len(cost_one_matrix)):
        find_one_component_vertices(cost_one_matrix, vertices_reached, m, v)


# calculate_one_subtrees(cost_one_matrix) calculates a list of number of vertices of each non-singleton-vertex
#           component of a subgraph of G that only contains the cost 1 edges
# requires:
#           cost_one_matrix: n*n matrix of boolean value
def calculate_one_subtrees(cost_one_matrix):
    cost_one_subtrees = []
    for i in range(len(cost_one_matrix)):
        for j in range(i+1,len(cost_one_matrix)):
            # for each cost 1 edge, computes the vertices it could reach in the subgraph
            if cost_one_matrix[i][j] == True:
                vertices_reached = [0 for _ in range(len(cost_one_matrix))]
                find_one_component_vertices(cost_one_matrix, vertices_reached, i, j)
                cost_one_subtrees.append(sum(vertices_reached))

    return cost_one_subtrees


if __name__ == '__main__':
    # initialization
    first_line = sys.stdin.readline().strip()
    n, k = map(int, first_line.split())
    cost_one_matrix = [[False for _ in range(n)] for _ in range(n)]

    # setting up matrix entries
    for _ in range(n*(n-1)//2):
        line = sys.stdin.readline().strip()
        u, v, c = map(int, line.split())
        if c == 1:
            cost_one_matrix[u][v] = True

    cost_one_subtrees = calculate_one_subtrees(cost_one_matrix)

    # reversely sort the list
    cost_one_subtrees.sort(reverse=True)

    total_cost = 0
    for i in range(len(cost_one_subtrees)):
        if (cost_one_subtrees[i] > k):
            # if the largest subtree could cover k
            total_cost += k
            break
        else:
            # otherwise will need one cost 2 edge to connect the largest subtree to the second largest one
            total_cost += cost_one_subtrees[i]
            k -= cost_one_subtrees[i]-1
    
    print(total_cost)
        