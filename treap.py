#!/usr/bin/python

import sys
import random

class TreapNode(object):
   MAX_RAND = 10000000

   def __init__(self, value, priority=None):
      self.value = value
      self.left = None
      self.right = None

      if priority is None:
         self.priority = random.randint(0, TreapNode.MAX_RAND)
      else:
         self.priority = priority


# max heep is used for balancing the treap

class Treap(object):

   def __init__(self):
      self.root = None

   def insert(self, value):
      if not self.contains(value):
         self.root = Treap._insert(self.root, value)

   def inorder(self):
      return Treap._inorder(self.root)

   def preorder(self):
      return Treap._preorder(self.root)

   def delete(self, value):
      if self.contains(value):
         self.root = Treap._delete(self.root, value)

   def contains(self, value):
      return Treap._contains(self.root, value)

   def merge(self, other):
      ''' 
      Works only if every element in other thee is bigger than 
      first tree.
      Works in O(log n)
      '''
      self.root = Treap._merge(self.root, other.root)


   @staticmethod
   def cmp(A, B):
      if A is None and B is None: return 0
      if A is None: return +1
      if B is None: return -1

      if A.priority < B.priority:
         return -1
      else:
         return +1

   @staticmethod
   def _contains(node, value):
      if node is None:
         return False

      if node.value < value:
         return Treap._contains(node.right, value)
      elif node.value > value:
         return Treap._contains(node.left, value)

      return True

   @staticmethod
   def _insert(node, value):
      if node is None:
         return TreapNode(value)

      if node.value < value:
         node.right = Treap._insert(node.right, value)
         if node.right.priority > node.priority:
            node = Treap._rotateLeft(node)
      else:
         node.left  = Treap._insert(node.left,  value)
         if node.left.priority > node.priority:
            node = Treap._rotateRight(node)

      return node

   @staticmethod
   def _delete(node, value):
      if node.left is None and node.right is None:
         node = None
      elif node.value > value:
         node.left = Treap._delete(node.left, value)
      elif node.value < value:
         node.right = Treap._delete(node.right, value)
      elif Treap.cmp(node.left, node.right) == +1: 
         node = Treap._rotateLeft(node)
         node.left = Treap._delete(node.left, value)
      elif Treap.cmp(node.left, node.right) == -1:
         node = Treap._rotateRight(node)
         node.right = Treap._delete(node.right, value)
      else:
         assert False, "Impossible case"

      return node

   @staticmethod
   def _merge(A, B):
      if A is None: return B
      if B is None: return A

      if A.priority < B.priority:
         B.left = Treap._merge(A, B.left)
         return B
      else:
         A.right = Treap._merge(A.right, B)
         return A

   @staticmethod
   def _rotateLeft(node):
      tmp = node.right.left
      node.right.left, node = node, node.right
      node.left.right = tmp
      return node

   @staticmethod
   def _rotateRight(node):
      tmp = node.left.right
      node.left.right, node = node, node.left
      node.right.left = tmp
      return node

   @staticmethod
   def _inorder(node):
      lst = []
      if node is not None:
         lst.extend(Treap._inorder(node.left))
         lst.append(node.value)
         lst.extend(Treap._inorder(node.right))

      return lst

   @staticmethod
   def _preorder(node):
      lst = []
      if node is not None:
         lst.append(node.value)
         lst.append(Treap._preorder(node.left))
         lst.append(Treap._preorder(node.right))

      return lst


def main():

   LEN = 10 if len(sys.argv) == 1 else int(sys.argv[1])
   PRT = 20

   lst = [i for i in xrange(LEN)]
   random.shuffle(lst)

   if LEN < PRT: print lst

   t = Treap()
   for value in lst:
      t.insert(value)

   if LEN < PRT: print t.inorder()

   print "OK" if t.inorder() == sorted(lst) else "WA"

   x = random.randint(0, LEN)
   print x
   t.delete(x)

   if LEN < PRT: print t.inorder()

   print "OK" if t.inorder() == range(x) + range(x + 1, LEN) else "WA"

   return 0


if __name__ == '__main__':
   sys.exit(main())
