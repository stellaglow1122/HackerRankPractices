def bit_count(self):
    return bin(self).count("1")

def rearrange(elements):
    results = []
    for element in elements:
        results.append([element, bit_count(element)])
    results.sort(key=lambda x: (x[1], x[0]))
    
    return [result[0] for result in results]

if __name__ == '__main__':
    arr = [7, 8, 6, 5]
    results = rearrange(arr)
    print(results)
