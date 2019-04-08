# 分别实现顺序栈/链式栈,并且支持动态扩容
# 利用栈检查括号匹配
# 实现浏览器的前进后退功能


class SequentialStack:
    def __init__(self, length):
        self.length = length
        self.space = [0] * length
        self.number = 0

    def push(self, data, dyna=False):
        if not dyna:  # 默认不扩容
            if self.number >= self.length:
                return -1
        else:  # 如果扩容
            if self.number >= self.length:
                self.space += [0] * self.length
                self.length += self.length
        self.space[self.number] = data
        self.number += 1

    def pop(self):
        if self.number == 0:
            return -1
        self.number -= 1
        return self.space[self.number]

    def __repr__(self):
        return 'stack space: {},number: {},length: {}'.format(','.join(map(lambda x: str(x), self.space)),
                                                              self.number,
                                                              self.length
                                                              )

    __str__ = __repr__


class DoublyLinkedNode:
    def __init__(self, data, prevnode=None, nextnode=None):
        self.data = data
        self.prevnode = prevnode
        self.nextnode = nextnode


class LinkedStack:  # 双向链表实现链式栈
    def __init__(self, length):
        self.length = length
        self.number = 0
        self.space = None
        self.tail = None

    def push(self, data, dyna=False):
        newnode = DoublyLinkedNode(data)
        if not self.space:
            self.space = newnode
            self.tail = newnode
            self.number += 1
            return
        if not dyna:
            if self.number >= self.length:
                return -1
        else:
            if self.number >= self.length:
                self.length += self.length
        self.tail.nextnode = newnode
        newnode.prevnode = self.tail
        self.tail = self.tail.nextnode
        self.number += 1

    def pop(self):
        if not self.space:
            return -1
        self.tail = self.tail.prevnode
        ret = self.tail.nextnode.data
        self.tail.nextnode = None
        self.number -= 1
        return ret

    def __repr__(self):
        if not self.space:
            return 'none'
        string = str(self.space.data)
        p = self.space
        for _ in range(self.number-1):
            p = p.nextnode
            string += '->{}'.format(p.data)
        return 'linked stack:{}, number:{}, length:{}'.format(string,self.number,self.length)

    __str__ = __repr__

class ForwardBackward:
    pass


class InspectBracketMatching:
    pass


if __name__ == '__main__':
    print('test1 ---------------------------')
    stack = SequentialStack(3)
    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    stack.push(4)
    stack.push(1, True)
    print(stack)
    print(stack.pop())
    print(stack)
    print('test2 ---------------------------')
    linkedstack = LinkedStack(3)
    linkedstack.pop()
    print(linkedstack)
    linkedstack.push(1)
    print(linkedstack)
    linkedstack.push(2)
    linkedstack.push(3)
    print(linkedstack)
    linkedstack.push(4)
    print(linkedstack)
    linkedstack.push(4, True)
    print(linkedstack)
    linkedstack.pop()
    print(linkedstack)

