import os


class QueueModified:
    class Elem:
        left = None
        value = None
        right = None
        index_of_operation = None

        def __init__(self, left, value, right, index_of_operation):
            self.left = left
            self.value = value
            self.right = right
            self.index_of_operation = index_of_operation

        def info(self, string=""):
            print(string, end="")
            if not (self.left is None):
                print(self.left.value, end=" ")
            else:
                print("-", end=" ")
            print(self.value, end=" ")

            if not (self.right is None):
                print(self.right.value)
            else:
                print("-")

    queue_array: set[Elem] = set()

    first: Elem = None
    length_queue = 0
    operations = 0
    operations_array = []

    def isEmpty(self) -> bool:
        return self.length_queue == 0


    def enqueue(self, *args):

        for adding_element_value in args:

            if self.isEmpty():

                elem = self.Elem(None, adding_element_value, None, self.operations)
                self.queue_array.add(elem)
                self.first = elem


            else:

                checking_elem = self.first

                if adding_element_value < self.first.value:
                    elem = self.Elem(None, adding_element_value, self.first, self.operations)
                    self.queue_array.add(elem)

                    self.first.left = elem
                    self.first = elem

                    self.length_queue += 1
                    self.operations += 1
                    self.operations_array.append(elem)

                    continue

                while (adding_element_value > checking_elem.value) and (checking_elem.right is not None):
                    checking_elem = checking_elem.right

                elem = self.Elem(checking_elem, adding_element_value, checking_elem.right, self.operations)
                self.queue_array.add(elem)
                checking_elem.right = elem


            self.length_queue += 1
            self.operations += 1
            self.operations_array.append(elem)


    def __init__(self, arr=None):
        if arr is None:
            arr = []

        for elem in arr:
            self.enqueue(elem)



    def get_array(self) -> list:
        arr = []
        if self.isEmpty():
            return arr

        elem = self.first

        while elem.right is not None:
            arr.append(elem.value)
            elem = elem.right

        arr.append(elem.value)

        return arr

    def get_min(self):

        self.operations += 1
        self.operations_array.append(None)


        if self.isEmpty():
            return "*"


        answer_elem = self.first

        self.first = self.first.right

        self.queue_array.remove(answer_elem)
        self.length_queue -= 1


        return answer_elem.value




    def queue_info(self):
        print(self.get_array())


    def D(self, x, y):

        self.operations_array[x+1].value = int(y)

        self.operations += 1
        self.operations_array.append(None)


def main(array: list[str]):
    """
    array ['A 1', 'A 2', ... , 'D 2 1', 'X']
    A x is enqueue x
    X is get_min
    D x y is 'заменить значение элемента, добавленного в очередь
операцией A в строке входного файла номер x + 1, на y'
    """
    queue = QueueModified()
    answer = []
    for operand in array:
        if "A" in operand:
            value = int(operand.split()[1])
            queue.enqueue(value)
        elif "D" in operand:
            x = int(operand.split()[1])
            y = int(operand.split()[2])
            queue.D(x, y)
        elif "X" in operand:
            answer.append(queue.get_min())



    return answer



if __name__ == '__main__':
    path_input = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt')
    path_output = os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt')

    from lab5.utils import read_file_line, vertical_norm_view, write_file
    num = int(read_file_line(path_input, 0))
    array = []

    for i in range(num):
        array.append(read_file_line(path_input, i + 1))


    write_file(path_output, vertical_norm_view(main(array)))
