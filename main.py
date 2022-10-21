from scripts.array_flattening import ArrayFlattening


if __name__ == '__main__':
    data_sets = [[1, [2, [3, [4, 5]]]], (1, (2, (3, (4, 5)))), [1, [2, [3, (4, 5)]]],
                 [1, [2, [3, [4, "Esto no es un numero"]]]]]
    af = ArrayFlattening()
    for data in data_sets:
        flat_list = af.array_flattening(data)
        print(flat_list)