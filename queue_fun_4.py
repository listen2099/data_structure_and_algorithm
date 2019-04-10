from single_linkedlist_fun_2 import SingleLinkedNode


class SequentialQueue:
    def __init__(self, length):
        self.length = length
        self.space = [0] * length
        self.head = 0
        self.tail = 0

    def enqueue(self, item, dy=True):
        if self.tail == self.length:
            if dy:
                if self.head == 0:
                    return -1
                for i in range(self.head, self.length):
                    self.space[i - self.head] = self.space[i]
                self.tail -= self.head
                self.head = 0
            else:
                return -1
        self.space[self.tail] = item
        self.tail += 1

    def printqueue(self):
        print('|' + '|'.join(map(str, self.space)) + '|')

    def dequeue(self):
        if self.head == self.tail:
            return -1
        ret = self.space[self.head]
        self.space[self.head] = None  # 这一步不是必须的只是为了看的清楚
        self.head += 1
        return ret


class ChainQueue:  # 首先要实现一个链表
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        newnode = SingleLinkedNode(item)
        if self.tail:
            self.tail._next = newnode
            # self.tail = self.tail._next
        else:
            self.head = newnode
        self.tail = newnode

    def dequeue(self):
        if self.head:
            ret = self.head.data
            self.head = self.head._next
            if not self.head:
                self.tail = None
            return ret
        else:
            return -1

    def __repr__(self):
        string = []
        p = self.head
        while p:
            string.append(p.data)
            p = p._next
        return '->'.join(map(str, string))

    __str__ = __repr__


class CircularQueue:
    def __init__(self, length):
        self.length = length
        self.space = [0] * length
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if (self.tail + 1) % self.length == self.head:  # full
            return -1
        self.space[self.tail] = item
        self.tail = (self.tail + 1) % self.length

    def dequeue(self):
        if self.tail == self.head:
            return -1
        ret = self.space[self.head]
        self.head = (self.head + 1) % self.length
        return ret

    def __repr__(self):
        string = []
        for i in range(self.length):
            string.append(self.space[i])
        return '|'.join(map(str, string))


if __name__ == '__main__':
    print('test1 ------------------------------')
    s = SequentialQueue(4)
    s.enqueue(9)
    print(s.dequeue())
    s.enqueue(1)
    print(s.dequeue())
    s.enqueue(2)
    s.enqueue(3)
    # s.enqueue(4)
    s.enqueue(5)
    s.printqueue()

    print('test2 ------------------------------')
    c = ChainQueue()
    print(c)
    print(c.dequeue())
    c.enqueue(9)
    print(c)
    c.enqueue(9)
    print(c)
    print(c.dequeue())
    print(c)
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    print(c)

    print('test3 ------------------------------')
    cir = CircularQueue(4)
    print(cir)
    cir.enqueue(1)
    print(cir)
    cir.enqueue(2)
    print(cir)
    cir.enqueue(3)
    print(cir)
    cir.enqueue(4)
    print(cir)
    cir.dequeue()
    cir.dequeue()
    cir.enqueue(9.1)
    cir.enqueue(9.2)
    print(cir)
