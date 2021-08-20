MAX = 5


class LRU:
    elements = {}
    size = 0

    def __init__(self):
        pass

    def print_elements(self):
        print(self.elements)

    def add(self, new_elem):
        if self.elements.get(new_elem):
            self.elements[new_elem] += 1
        else:
            if self.size < MAX:
                self.size += 1
            else:
                min_key = list(self.elements.keys())[0]
                for key, value in self.elements.items():
                    if self.elements[min_key] > value:
                        min_key = key
                self.elements.pop(min_key)

            self.elements[new_elem] = 1


x = LRU()

x.print_elements()
x.add(1)
x.print_elements()
x.add(2)
x.print_elements()
x.add(2)
x.print_elements()
x.add(3)
x.print_elements()
x.add(3)
x.print_elements()
x.add(4)
x.print_elements()
x.add(4)
x.print_elements()
x.add(5)
x.print_elements()
x.add(5)
x.print_elements()
x.add(6)
x.print_elements()