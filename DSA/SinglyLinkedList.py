class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

  def __str__(self):
    return str(self.val)


class SinglyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def push(self, val):
    new_node = Node(val)
    if not self.head:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = new_node

    self.length += 1

    return self

  def traverse(self):
    currNode = self.head
    while currNode:
      print(currNode.val)
      currNode = currNode.next

  def pop(self):
    if not self.head:
      return None

    currNode = self.head
    prevNode = currNode

    while currNode.next:
      prevNode = currNode
      currNode = currNode.next

    self.tail = prevNode
    self.tail.next = None
    self.length -= 1

    if self.length == 0:
      self.head = None
      self.tail = None

    return currNode

  def shift(self):
    """Remove First/head Node"""
    if not self.head:
      return None

    currNode = self.head
    self.head = currNode.next
    self.length -= 1

    return currNode

  def unshift(self, item):
    """Add new node at head"""

    new_node = Node(item)

    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      currNode = self.head
      self.head = new_node
      new_node.next = currNode

    self.length += 1

    return self

  def get(self, idx):
    if idx < 0 or idx >= self.length:
      return None

    count = 0
    currNode = self.head
    while count != idx:
      currNode = currNode.next
      count += 1

    return currNode

  def set(self, val, idx):
    reqVal = self.get(idx)

    if reqVal:
      reqVal.val = val
      return True

    return False

  def insert(self, idx, val):
    if idx < 0 or idx > self.length:
      return False

    if idx == self.length:
      self.push(val)
      return True

    if idx == 0:
      self.unshift(val)
      return True

    new_node = Node(val)
    prevNode = self.get(idx-1)
    new_node.next = prevNode.next
    prevNode.next = new_node
    self.length += 1

    return True

  def Remove(self, idx):
    if idx < 0 or idx >= self.length:
      return False

    if idx == self.length -1:
      return self.pop()

    if idx == 0:
      return self.shift()

    prevNode = self.get(idx-1)
    removed = prevNode.next
    prevNode.next = removed.next
    self.length -= 1

    return removed

  def reverse(self):

    prev = None
    curr = self.head
    self.tail = curr

    while curr != None:
      mynext = curr.next
      curr.next = prev
      prev = curr
      curr = mynext

    self.head = prev
    print(self.tail.next)
    return self