class Stack:
    class Elem:
        left = None
        value = None
        right = None


        def __init__(self, left, value, right):
            self.left = left
            self.value = value
            self.right = right

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

    stack_array: set[Elem] = set()

    last: Elem = None
    first: Elem = None


    def isEmpty(self) -> bool:
        return self.last is None


    def push(self, *args):
        for stack_elem in args:
            if self.isEmpty():

                elem = self.Elem(None, stack_elem, None)

                self.first = elem
                self.stack_array.add(elem)

            else:


                elem = self.Elem(self.last, stack_elem, None)
                self.last.right = elem

                self.stack_array.add(elem)

            self.last = elem


    def pop(self) -> Elem:

        if not self.isEmpty():

            elem = self.last

            self.stack_array.remove(elem)

            self.last = elem.left

            if not self.isEmpty():
                self.last.right = None

            else:
                self.last = None
                self.first = None


            return elem.value


    def __init__(self, array):
        for stack_elem in array:
            self.push(stack_elem)





    def get_array(self) -> list:
        array = []
        if self.isEmpty():
            return array

        elem = self.first
        while not (elem.right is None):
            array.append(elem.value)
            elem = elem.right
        array.append(elem.value)
        return array


    def stack_info(self):
        self.first.info("first:\n")
        self.last.info("last:\n")

        print("\nvalues:")

        print(self.get_array())

        print("\n\nelements (left, value, right):")
        stack_elem = self.first


        while not (stack_elem is None):
            stack_elem.info()
            stack_elem = stack_elem.right


if __name__ == '__main__':
    stack_arr = Stack([])
    stack_arr.push("123")
    stack_arr.stack_info()
