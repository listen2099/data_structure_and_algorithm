# 分别实现顺序栈/链式栈,并且支持动态扩容
# 利用栈检查括号匹配
# 实现浏览器的前进后退功能


class SequentialStack:
    def __init__(self, length):
        self.length = length
        self.init = length
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

    def read_last(self):
        if self.number == 0:
            return 'no content'
        return str(self.space[self.number - 1])

    def clean(self):
        self.length = self.init
        self.number = 0

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
        for _ in range(self.number - 1):
            p = p.nextnode
            string += '->{}'.format(p.data)
        return 'linked stack:{}, number:{}, length:{}'.format(string,
                                                              self.number,
                                                              self.length)

    __str__ = __repr__


class ForwardBackward:
    """
    考虑到内存空间和访问速度这里用顺序栈
    我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X;
    当点击后退按钮时，再依次从栈 X 中出栈，并将出栈的数据依次放入栈 Y。
    当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。
    当栈 Y 中没有数据，那就说明没有页面可以点击前进按钮浏览了。
    """

    def __init__(self, backward=20, forward=20):
        self.xstack = SequentialStack(backward)
        self.ystack = SequentialStack(forward)

    def new_page(self, page='content'):
        self.xstack.push(page)
        self.ystack.clean()

    def read_page(self):
        print(self.xstack.read_last())

    def backward(self):
        content = self.xstack.pop()
        if content != -1:
            self.ystack.push(content, True)

    def forward(self):
        content = self.ystack.pop()
        if content != -1:
            self.xstack.push(content, True)


class InspectBracketMatching:
    def __init__(self, string: str):
        self.string = string
        self.stack = SequentialStack(50)

    def is_legal(self):
        for char in self.string:
            if char in '([{':
                self.stack.push(char, True)
            if char in ')]}':
                temp = self.stack.read_last()
                if temp == 'no content':
                    return False
                if temp == '(' and char == ')' or temp == '[' and char == ']' or temp == '{' and char == '}':
                    self.stack.pop()
        if self.stack.number > 0:
            return False
        return True


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
    print('test3 ---------------------------')
    fb = ForwardBackward()
    fb.read_page()
    fb.new_page('page1')
    fb.read_page()
    fb.new_page('page2')
    fb.read_page()
    fb.backward()
    fb.read_page()
    fb.forward()
    fb.forward()
    fb.read_page()
    print('test4 ---------------------------')
    ins = InspectBracketMatching('(asdkfn(a(sldfk{askjdfn}asn)))')
    print(ins.is_legal())
