# 利用单链表实现LRU缓存
# 关键要正确实现一个单向链表的插入和删除操作

# 单链表分三种情况
# head -> None
# head -> data1/next1 -> None
# head -> data1/next1 -> data2/next2 -> None
# head -> data1/next1 -> data2/next2 -> data3/next3 -> None
# head -> data1/next1 -> data2/next2 -> data3/next3 -> data4/next4 ->None
# 插入操作
# 删除操作


"""
    我的思路是这样的：我们维护一个有序单链表，越靠近链表尾部的结点是越早之前访问的。
    当有一个新的数据被访问时，我们从链表头开始顺序遍历链表。
    1. 如果此数据之前已经被缓存在链表中了，
        我们遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。
    2. 如果此数据没有在缓存链表中，又可以分为两种情况：
        如果此时缓存未满，则将此结点直接插入到链表的头部；
        如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部。
"""


class LrcLinkedList:
    def __init__(self, length: int = 10):
        self.length = length  # all length
        self.instlength = 0  # instance length
        self.lrcspace = None

    def insert(self, data, pos):  # 将数据插入当前的n位置, 若果pos过大, 默认加在末尾
        if self.lrcspace is None:
            self.lrcspace = LinkedNode(data)
            self.instlength += 1
            return
        if pos > self.instlength:  # 若果pos过大, 默认加在末尾
            p = self.lrcspace
            while p.nextnode is not None:
                p = p.nextnode
            p.nextnode = LinkedNode(data)
            self.instlength += 1
            return
        if pos <= 1:  # 若pos <= 1, 默认加载开头
            newnode = LinkedNode(data)
            newnode.nextnode = self.lrcspace
            self.lrcspace = newnode
            self.instlength += 1
            return
        p = self.lrcspace
        for _ in range(pos - 2):
            p = p.nextnode
        newnode = LinkedNode(data)
        newnode.nextnode = p.nextnode
        p.nextnode = newnode
        self.instlength += 1

    def delete(self, pos):  # 将链表的第几个节点删除
        if self.lrcspace is None:
            print('empty!')
            return
        if pos <= 1:
            p = self.lrcspace
            self.lrcspace = self.lrcspace.nextnode
            del p
            self.instlength -= 1
            return
        if pos > self.instlength:
            if self.instlength == 1:
                p = self.lrcspace
                self.lrcspace = self.lrcspace.nextnode
                del p
                self.instlength -= 1
            p = self.lrcspace
            while p.nextnode.nextnode is not None:
                p = p.nextnode
            pdel = p.nextnode
            p.nextnode = p.nextnode.nextnode
            del pdel
            self.instlength -= 1
            return
        p = self.lrcspace
        for _ in range(pos - 2):
            p = p.nextnode
        pdel = p.nextnode
        p.nextnode = p.nextnode.nextnode
        del pdel
        self.instlength -= 1
        return

    def find_data(self, data):
        if self.lrcspace is None:
            self.lrcspace = LinkedNode(data)
            self.instlength += 1
            return
        p = self.lrcspace
        count = 1
        while p.data != data:
            p = p.nextnode
            if p is not None:
                count += 1
            if p is None:  # 遍历完了却没找到
                if self.instlength < self.length:
                    self.insert(data, 1)
                else:
                    self.delete(self.length)
                    self.insert(data, 1)
                return
        # 找到了
        self.delete(count)
        self.insert(data, 1)
        return


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.nextnode = None


def printlist(linkedlist):
    tempointer = linkedlist.lrcspace
    count = 1
    if tempointer is None:
        print("---node null, data = null.---")
        return
    while tempointer.nextnode is not None:
        print("---node {}, data = {}, {}th node, whole length = {}.---".format(count,
                                                                               tempointer.data,
                                                                               count,
                                                                               linkedlist.length))
        count += 1
        tempointer = tempointer.nextnode
    print("---node {}, data = {}, {}th node, whole length = {}.---".format(count,
                                                                           tempointer.data,
                                                                           count,
                                                                           linkedlist.length))


#  test
l = LrcLinkedList(4)
printlist(l)
l.find_data('data1')
l.find_data('data1')
printlist(l)
print('---')
l.find_data('data2')
l.find_data('data3')
l.find_data('data1')
l.find_data('data5')
l.find_data('data2')
l.find_data('data5')
printlist(l)
