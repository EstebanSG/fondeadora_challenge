from scripts.array_flattening import ArrayFlattening


if __name__ == '__main__':
    data = [1, [2, [3, (4, 5)]]]
    af = ArrayFlattening()
    flat_list = af.array_flattening(data)
    print(flat_list)