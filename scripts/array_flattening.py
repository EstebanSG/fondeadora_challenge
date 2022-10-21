class ArrayFlattening:
    flat_list = []

    def __init__(self):
        self.flat_list = []

    def array_flattening(self, matrix: 'List[List[int]]'):
        if type(self.flat_list) != list and len(self.flat_list) > 0:
            self.reset_flat_list()

        try:
            for element in matrix:
                if type(element) == list:
                    self.array_flattening(element)
                else:
                    self.flat_list.append(element)
        except Exception as e:
            pass
        return self.flat_list

    def reset_flat_list(self):
        self.flat_list = []
