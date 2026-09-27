class Counter:
    def __init__(self, max_num):
        self.i = 0
        self.max_num = max_num

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_num:
            raise StopIteration
        return self.i

count1 = Counter(5)

'''
for i in count1:
    print(i)
'''

print(count1.__next__())

print(count1.__next__())
print(count1.__iter__())
print(next(count1))
print(next(count1))