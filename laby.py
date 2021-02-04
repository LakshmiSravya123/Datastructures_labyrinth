
import time


class Laby(object):
    def __init__(self, lab, dim):
        self.lab = lab
        self.dim = dim

    def solve(self):
        # convert string to matrix format(maze)
        matrix = self.string_to_maze()

        # Find the start and end in the matrix or maze
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'D':
                    start_D = tuple([i, j])
                elif matrix[i][j] == 'F':
                    end_F = tuple([i, j])

        # Start time and end time ... To keep the track of the time
        start_time = time.time()
        # Function call to  find the shortest path using BFS algorithm
        short_path = self.breadthFirstSearch(matrix, start_D, end_F)
        end_time = time.time()
        total_time = end_time - start_time

        if short_path == None:
            isShortPath = False
            print("No path Found.")
        else:
            isShortPath = True
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if tuple([i, j]) in short_path and matrix[i][j] != 'D' and matrix[i][j] != 'F':
                        print(".", end="")
                    else:
                        print(matrix[i][j], end="")
                print()
            print("Shortest path: ")
            print(short_path)

        print("Time taken for BFS to find the shortest path:", total_time, "secs")
        print("\n")
        return ((isShortPath, short_path))

    # Converts String to a maze format)
    def string_to_maze(self):
        lab = self.lab
        dim = self.dim
        matrix = []

        for i in range(len(lab)):
            if i % dim == 0:
                sub_string = lab[i:i + dim]  # divides large string  in to sub strings which are of length dim each
                char_list = []
                for j in sub_string:
                    char_list.append(j)  # a list which holds substring characters
                matrix.append(char_list)  # list that holds all the  character lists

        return matrix

    # BFS algorithm to find the shortestpath in the maze
    def breadthFirstSearch(self, matrix, start_D, end_F):
        # Initializing a queue
        que = [start_D]
        # creating a set to keep a track of all places visited
        visit = set()

        while len(que) != 0:
            if que[0] == start_D:
                shortest_path = [que.pop(0)]
            else:
                # a variable which keeps track of the path
                shortest_path = que.pop(0)

            # a temporary variable to move along
            temp = shortest_path[-1]

            # if the path reaches F return the path
            if temp == end_F:
                return shortest_path

            # move along the maze checking all the spaces and the wall
            elif temp not in visit:
                # create a list to check spaces beside the temp
                adjSpaces = list()
                # To check towards up
                adjSpaces.append((temp[0] - 1, temp[1]))
                # To check towards down
                adjSpaces.append((temp[0] + 1, temp[1]))
                # To check towards left
                adjSpaces.append((temp[0], temp[1] - 1))
                # To check towards Right
                adjSpaces.append((temp[0], temp[1] + 1))
                # Keeps the track of all adjacent spaces which is neither wall not already visited

                finalSpaces = list()
                for i in adjSpaces:
                    # check if there is not wall # and check if the temp didnt visit the space
                    if matrix[i[0]][i[1]] != '#' and i not in visit:
                        finalSpaces.append(i)

                for fin in finalSpaces:
                    # create a temporary path varibale which appends to the existing path
                    newPath = list(shortest_path)
                    newPath.append(fin)
                    # Add path to the que
                    que.append(newPath)
                # add the temp in to visit set as its been visited
                visit.add(temp)
        return None  # loop continues untill temp==end_F


