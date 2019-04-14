# 1.单链表反转
# 2.链表中环的检测
# 3.两个有序链表合并
# 4.删除链表倒数第n个节点
# 5.求链表的中间节点


class SingleLinkedNode:
    def __init__(self, data, nextnode=None):
        self.data = data
        self._next = nextnode


class SingleLinkedList:
    def __init__(self):
        self._head = None

    # 从头按node插入
    def insert_node_to_head(self, newnode: SingleLinkedNode):
        if newnode:
            newnode._next = self._head
            self._head = newnode

    # 从头按值插入
    def insert_value_to_head(self, data):
        newnode = SingleLinkedNode(data)
        self.insert_node_to_head(newnode)

    # 在某个节点前插入某个节点
    def insert_node_before(self, node, newnode):  # 找不到节点不插入, 返回-1
        if not self._head or not node or not newnode:
            return -1
        if self._head == node:
            self.insert_node_to_head(newnode)
            return
        current = self._head
        if current._next and current._next != node:
            current = current._next
        if not current._next:
            return -1
        newnode._next = current._next
        current._next = newnode
        # _head -> node1 -> node2 -> node3 -> None

    # 在某个节点前插入某个值
    def insert_value_before(self, node, data):
        newnode = SingleLinkedNode(data)
        self.insert_node_before(node, newnode)

    # 在某个节点后插入某个节点
    def insert_node_after(self, node, newnode):
        if not node or not newnode:
            return -1
        newnode._next = node._next
        node._next = newnode

    # 在某个节点后插入某个值
    def insert_value_after(self, node, data):
        newnode = SingleLinkedNode(data)
        self.insert_node_after(node, newnode)

    # 按节点删除
    def delete_by_node(self, node):
        if not self._head or not node:
            return -1
        if node._next:
            p = node._next
            node.data = node._next.data
            node._next = node._next._next
            del p
        # node._next is None:
        current = self._head
        while current and current._next != node:
            current = current._next
        if not current:
            return -1
        current._next = None

    # *按值删除
    def delete_by_value(self, value):  # 引入一个哨兵头节点
        if not self._head or not value:
            return
        fake_head = SingleLinkedNode('fake_head')
        fake_head._next = self._head
        prev, current = fake_head, self._head
        while current:  # 逐个检查, 只要看到一样的就将它跳过
            if current.data != value:
                prev._next = current
                prev = prev._next
            current = current._next
        if prev._next:  # 做后一个节点是相同的需要删除
            prev._next = None
        self._head = fake_head._next  # in case head.data == value
        ## head      ->  data1/next1 -> data2/next2 -> data3/next3 -> data4/next4 ->None

    # 删除导数第n个节点, 先反转,再删除,再返回新的
    def delete_last_n(self, n):
        self.link_reverse()
        fake_node = SingleLinkedNode('fake_node')
        fake_node._next = self._head
        self._head = fake_node
        p = self._head
        for _ in range(n - 1):
            if not p._next._next:
                self._head = node_reverse(fake_node._next)
                return
            p = p._next
        p._next = p._next._next
        self._head = node_reverse(fake_node._next)

    # 求中间节点
    def ret_middle(self):
        fast = self._head
        slow = self._head
        pos = 1
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next
            pos += 1
        return slow.data, pos

    # 值查找 通过值找到节点
    def find_by_value(self, value):
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    # head -> data1/next1 -> data2/next2 -> data3/next3 -> data4/next4 ->None

    # 索引查找
    def find_by_index(self, index):
        p = self._head
        pos = 0
        while p and pos != index:
            p = p._next
            pos += 1
        return p

    # 原地反转
    def link_reverse(self):
        head = self._head
        self._head = node_reverse(head)

    # 打印链表
    def print_all(self):
        current = self._head
        if current:
            print(f"{current.data}", end="")
            current = current._next
        while current:
            print(f"->{current.data}", end="")
            current = current._next
        print("\n", flush=True)

    # 容器化
    def __iter__(self):
        node = self._head
        while node:
            yield node.data
            node = node._next

    def __repr__(self):
        p = self._head._next
        string = str(self._head.data)
        while p:
            string += '->' + str(p.data)
            p = p._next
        return string

    __str__ = __repr__


l = SingleLinkedList()
l.insert_value_to_head('data1')
l.insert_value_to_head('data1')
l.insert_value_to_head('data3')
l.insert_node_before(l.find_by_index(2), SingleLinkedNode('add'))
l.print_all()

"""
检查一个单向链表构成的字符串是不是会问序列
快慢指针
将慢指针所指的的地方进行一次逆序
"""


# node的反转
def node_reverse(head):
    reversed_head = None
    while head:
        next = head._next
        head._next = reversed_head
        reversed_head = head
        head = next
    return reversed_head


# 判断一个链表中储存的字符是不是会问序列
def is_palindrome(l):
    l.print_all()
    slow = l._head
    fast = l._head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
    reverse_node = node_reverse(slow)
    head_node = l._head
    is_palin = True
    while (reverse_node and head_node):
        if (reverse_node.data == head_node.data):
            reverse_node = reverse_node._next
            head_node = head_node._next
        else:
            is_palin = False
            break
    return is_palin


# 链表中是否存在换
def if_loop(l):
    if not l._head:
        return False
    slow = l._head
    fast = l._head._next
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        if not fast:
            return False
        elif slow is fast:
            return True
    return False


# 两个有序链表的合并, 前提是有序
def cbind_linkedlist(la, lb):  # 原来都是由小到大, 合成由大到小, 再反转
    newlinkedlist = SingleLinkedList()
    ha = la._head
    hb = lb._head
    while ha and hb:
        if ha.data <= hb.data:
            newlinkedlist.insert_value_to_head(ha.data)
            ha = ha._next
        else:
            newlinkedlist.insert_value_to_head(hb.data)
            hb = hb._next
    while ha or hb:
        if ha:
            newlinkedlist.insert_value_to_head(ha.data)
            ha = ha._next
        if hb:
            newlinkedlist.insert_value_to_head(hb.data)
            hb = hb._next
    newlinkedlist.link_reverse()
    return newlinkedlist


if __name__ == '__main__':
    print('test1 --------------------------------------------')
    test_str = ['a', 'ab', 'aa', 'abc', 'aba', 'abab', 'abba']
    for s in test_str:
        l = SingleLinkedList()
        for c in s:
            l.insert_value_to_head(c)
        print(is_palindrome(l))

    print('test2 --------------------------------------------')
    test1 = [1, 3, 6, 8, 10, 23, 44]
    test2 = [3, 4, 5, 7]
    l1 = SingleLinkedList()
    l2 = SingleLinkedList()
    for it in test1:
        l1.insert_value_to_head(it)
    for it in test2:
        l2.insert_value_to_head(it)
    l1.link_reverse()
    l2.link_reverse()
    l1.print_all()
    l2.print_all()
    all = cbind_linkedlist(l1, l2)
    all.print_all()

    print('test3 --------------------------------------------')
    all.delete_last_n(9)
    all.print_all()
    all.delete_last_n(2)
    all.print_all()
    print(all.ret_middle())
    all.delete_last_n(8)
    all.print_all()
    all.delete_last_n(8)
    all.print_all()

    print('test3 --------------------------------------------')
    print(all.ret_middle())
