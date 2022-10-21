import logging

logger = logging.getLogger(__name__)


class ArrayFlattening:
    flat_list = []

    def __init__(self):
        self.flat_list = []

    def array_flattening(self, matrix: 'List[List[int]]'):
        if len(self.flat_list) > 0:
            self.reset_flat_list()
        try:
            if type(matrix) != list:
                raise TypeError('Input value are not type list', matrix)
            self.flattening(matrix)
        except TypeError as t_error:
            logger.error(t_error.args)
            self.flat_list = matrix
        return self.flat_list

    def flattening(self, matrix: 'List[List[int]]'):
        try:
            for element in matrix:
                if type(element) == list:
                    self.flattening(element)
                elif type(element) == int:
                    self.flat_list.append(element)
                else:
                    raise TypeError(f'Input value type expect list or int get {type(element)}', element)
        except TypeError as t_error:
            logger.error(t_error.args)
            self.flat_list = matrix
        except:
            logger.error("Something not expected happened")
            self.flat_list = []

    def reset_flat_list(self):
        self.flat_list = []
