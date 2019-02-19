import sys
import numpy as np
import heapq

def solve_task1(input_matrix):


    heuristic_value = [6, 5]
    heuristic_matrix = np.zeros((input_matrix.shape[0], input_matrix.shape[1]))

    findindexr = np.where(input_matrix == "R")
    r_index = [findindexr[0][0], findindexr[1][0]]

    findindexx = np.where(input_matrix == "X")
    x_index = [findindexx[0][0], findindexx[1][0]]


    class Node():

        def __init__(self):
            self.f = 0
            self.g = 0
            self.h = 0
            self.symbol = ''
            self.name = ''

        def __lt__(self, other):
            return self.f < other.f

        def __eq__(self, other):
            return self.name == other.name

        def __str__(self):
            return str(self.name)

        def update_params(self):
            self.f = self.h + self.g

    for i in range(heuristic_matrix.shape[0]):
        for j in range(heuristic_matrix.shape[1]):
            vert_dif = abs(i - x_index[0]) * heuristic_value[0]
            hor_dif = abs(j - x_index[1]) * heuristic_value[1]
            total_dif = np.sqrt(vert_dif ** 2 + hor_dif ** 2)
            heuristic_matrix[i][j] = total_dif

    node_list = []

    for i in range(input_matrix.shape[0]):
        dummy_list = []
        for j in range(input_matrix.shape[1]):
            dummy = Node()
            dummy.name = '{0} {1}'.format(i, j)
            dummy.coords = (i, j)
            dummy.symbol = input_matrix[i][j]
            dummy.h = heuristic_matrix[i][j]
            dummy.update_params()
            dummy_list.append(dummy)
        node_list.append(dummy_list)

    def newCost(vertex, neighbour):

        dif_array = np.zeros(3)
        dif_array[0] = abs(vertex.coords[0] - neighbour.coords[0])
        dif_array[1] = abs(vertex.coords[1] - neighbour.coords[1])
        dif_array[2] = (sum(dif_array) == 2)

        if dif_array[0] == 1 and dif_array[1] == 0:
            new_cost = 6
        elif dif_array[0] == 0 and dif_array[1] == 1:
            new_cost = 5
        elif sum(dif_array) == 3:
            new_cost = 10
        else:
            new_cost = 0

        return new_cost

    def a_star(r_index, x_index, node_list):
        frontier = []
        end = []
        frontier.append((node_list[r_index[0]][r_index[1]]))
        end = node_list[x_index[0]][x_index[1]]
        heapq.heapify(frontier)
        explored = []

        while len(frontier) > 0:
            node = heapq.heappop(frontier)

            if node.name == end.name:
                return int(node.f)
            explored.append(node)

            for i in range(node.coords[0] - 1, node.coords[0] + 2):
                for j in range(node.coords[1] - 1, node.coords[1] + 2):

                    if i < 0 or j < 0 or i > input_matrix.shape[0] - 1 or j > input_matrix.shape[1] - 1:
                        continue
                    if node_list[i][j].coords == node.coords:
                        continue

                    if node_list[i][j].symbol == '*':
                        continue
                    step_g = newCost(node, node_list[i][j])
                    temp1 = node.g
                    temp1 = temp1 + step_g
                    temp2 = node_list[i][j].f
                    temps = temp1 + temp2
                    if node_list[i][j] not in frontier and node_list[i][j] not in explored:

                        node_list[i][j].g = temp1
                        node_list[i][j].update_params()
                        # print(node_list[i][j].f,node_list[i][j].g,node_list[i][j].h,node_list[i][j].name,"zubaa")

                        heapq.heappush(frontier, node_list[i][j])
                    elif node_list[i][j] in frontier and node_list[i][j].f > temps:
                        node_list[i][j] = temp1
                        temp1.update_params()

        return "No path found!"


    return a_star(r_index, x_index, node_list)

# Use as many helper functions as you like


# Get input from command prompt and run the program
input_arg = sys.argv[1]

def run_program(file_name = input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(file_name, dtype='str')

    # Your main function to solve the matrix
    print(solve_task1(input_matrix))

run_program()

# To test the result yourself,
# Open the command line tool, navigate to the folder and execute:
# python Solution1.py input_for_task1.txt


