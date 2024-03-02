visited = []
def adjacencyTraversal(related, row, column, rowSize, columnSize):
    global visited
    visited.append([row, column])
    adjacency = [1, 0, -1, 0, 1]
    for i in range(4):
        nextRow = row + adjacency[i]
        nextColumn = column + adjacency[i + 1]
        if nextRow < rowSize and nextColumn < columnSize and [nextRow, nextColumn] not in visited:
            if related[nextRow][nextColumn] == '1':
                adjacencyTraversal(related, nextRow, nextColumn, rowSize, columnSize)

def countGroups(related):
    groups = 0
    global visisted
    rows = len(related)
    columns = len(related[0])
    for i in range(rows):
        for j in range(columns):
            if [i, j] not in visited and related[i][j] == '1':
                groups += 1
                adjacencyTraversal(related, i, j, rows, columns)
    return groups

if __name__ == '__main__':
    related = ['1100', '1110', '0110', '0001']
    related = ['10000', '01000', '00100', '00010', '00001']
    results = countGroups(related)
    print(results)
