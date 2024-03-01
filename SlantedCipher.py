def decode(encodedString, numberOfRows):
    column = int(len(encodedString) / numberOfRows) if len(encodedString) % numberOfRows == 0 else int((len(encodedString) / numberOfRows)) + 1
    encodedStringList = []
    i = 0
    while i < len(encodedString):
        encodedStringList.append(encodedString[i:i + column])
        i += column
    result = ''
    for i in range(column):
        row = 0
        col = i
        for j in range(numberOfRows):
            if row + j < numberOfRows and col + j < column:
                result += encodedStringList[row + j][col + j]
                
    stringEndIndex = len(result)
    for i in range(len(result) - 1, -1, -1):
        if result[i] == '_':
            stringEndIndex -= 1
        else:
            break
    result = result[:stringEndIndex + 1]
    return result.replace('_', ' ')

if __name__ == '__main__':
    string = 'mnes__ya_____mi'
    numberOfRows = 3
    print(decode(string, numberOfRows))
