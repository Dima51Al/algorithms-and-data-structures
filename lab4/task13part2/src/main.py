class Queue:
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

    queue_array: set[Elem] = set()

    last: Elem = None
    first: Elem = None
    limit_queue = 10**6
    length_queue = 0

    def isEmpty(self) -> bool:
        return self.last is None


    def enqueue(self, *args):
        if not self.check_limit():
            return

        for queue_elem in args:
            if self.isEmpty():

                elem = self.Elem(None, queue_elem, None)

                self.first = elem
                self.queue_array.add(elem)

            else:


                elem = self.Elem(self.last, queue_elem, None)
                self.last.right = elem
                self.queue_array.add(elem)

            self.last = elem
            self.length_queue += 1


    def check_limit(self):
        if self.length_queue < self.limit_queue:
            return True


    def dequeue(self) -> Elem:

        if not self.isEmpty():

            elem = self.first

            self.queue_array.remove(elem)
            self.length_queue -= 1

            self.first = elem.right

            if not self.isEmpty():
                self.first.left = None

            else:
                self.last = None
                self.first = None


            return elem.value


    def __init__(self, array):
        for queue_elem in array:
            self.enqueue(queue_elem)






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


    def queue_info(self):
        self.first.info("first:\n")
        self.last.info("last:\n")

        print("\nvalues:")
        print(self.get_array())


        print("\n\nelements (left, value, right):")
        queue_elem = self.first


        while not (queue_elem is None):
            queue_elem.info()
            queue_elem = queue_elem.right



if __name__ == '__main__':
    queue_arr = Queue([1, 2, 3, 4, 5])
    queue_arr.dequeue()
    queue_arr.queue_info()
