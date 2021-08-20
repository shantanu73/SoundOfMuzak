
class MemoizedFibo:
    fibo_table = {}

    def __init__(self):
        self.fibo_table = {
            1: 0,
            2: 1
        }

    def get_table(self):
        return self.fibo_table

    def fibo(self, n):
        if n <= 0:
            return "Invalid term index"
        a = self.fibo_table.get(n)
        if not a and n > 2:
            x = self.fibo(n - 1) + self.fibo(n - 2)
            self.fibo_table[n] = x
            return x
        return a


fibobj = MemoizedFibo()

print(fibobj.get_table())
print(fibobj.fibo(-5))
print(fibobj.get_table())
print(fibobj.fibo(0))
print(fibobj.get_table())
print(fibobj.fibo(2))
print(fibobj.get_table())
print(fibobj.fibo(3))
print(fibobj.get_table())
print(fibobj.fibo(5))
print(fibobj.get_table())
print(fibobj.fibo(11))
print(fibobj.get_table())
print(fibobj.fibo(7))
print(fibobj.get_table())
