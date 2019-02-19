import sys
import numpy as np


def solve_task2(input_matrix):
    y_length, x_length = input_matrix.shape[0], input_matrix.shape[1]

    # print(y_length, x_length)

    class Node():

        def __init__(self):
            self.symbol = ''
            self.name = ''

        def __str__(self):
            return str(self.name)

    node_list = []
    point_list = []
    q = []

    for i in range(y_length):
        dummy_list = []
        for j in range(x_length):
            dummy = Node()
            dummy.name = '{0} {1}'.format(i, j)
            dummy.coords = (i, j)
            dummy.symbol = input_matrix[i][j]
            dummy_list.append(dummy)
        node_list.append(dummy_list)

    for i in range(y_length):
        for j in range(x_length):
            if i == 0 or i == y_length - 1 or j == 0 or j == x_length - 1:
                if node_list[i][j].symbol == ".":
                    q.append(node_list[i][j])

    def dontmakestars(q, point_list):

        explored = []

        while len(q) > 0:
            node = q.pop()
            explored.append(node)

            x = node.coords[1]
            y = node.coords[0]

            neighbor_list = [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]

            for i in neighbor_list:
                if i[0] < 0 or i[1] < 0 or i[0] > input_matrix.shape[1] - 1 or i[1] > input_matrix.shape[0] - 1:
                    continue
                if node_list[i[1]][i[0]].symbol == 'X':
                    continue
                if node_list[i[1]][i[0]] not in q and node_list[i[1]][i[0]] not in explored:
                    q.append(node_list[i[1]][i[0]])

        return explored

    explored = dontmakestars(q, point_list)

    for i in range(y_length):
        for j in range(x_length):
            if node_list[i][j] not in explored:
                node_list[i][j].symbol = "X"
                input_matrix[i][j] = "X"
    return input_matrix


# Get input from command prompt and run the program
input_arg = sys.argv[1]


# file_name = "input_for_task2.txt"

def run_program(filename=input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(filename, dtype='str')

    # Your main function to solve the matrix
    output = solve_task2(input_matrix)

    # print the matrix to a txt file
    np.savetxt('output_for_task2.txt', output, fmt="%s")


run_program()

# To test the result yourself,
# Open the command line tool, navigate to the folder and execute:
# python Solution2.py input_for_task2.txt
