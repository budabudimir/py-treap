#!/usr/bin/python

import sys
import random

class TreapNode(object):
   MAX_RAND = 10000000
   INFINITY = MAX_RAND + 1

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

   def insert(self, value, priority=None):
      if not self.contains(value):
         self.root = Treap._insert(self.root, value, priority)

   def inorder(self):
      return Treap._inorder(self.root)

   def preorder(self):
      return Treap._preorder(self.root)

   def delete(self, value):
      if self.contains(value):
         self.root = Treap._delete(self.root, value)
      else:
         raise AttributeError("Value does not exist")

   def contains(self, value):
      return Treap._contains(self.root, value)

   def merge(self, other):
      self.root = Treap._merge(self.root, other.root)

   def split(self, value):
      self.root = Treap._insert(self.root, value, TreapNode.INFINITY)

      right = Treap()
      right.root = self.root.right
      self.root = self.root.left

      return right
      

   @staticmethod
   def cmp(A, B):
      if A is None and B is None: 
         return 0

      if A is None: return +1
      if B is None: return -1

      return A.priority - B.priority


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
   def _insert(node, value, priority=None):
      if node is None:
         return TreapNode(value, priority)

      if node.value < value:
         node.right = Treap._insert(node.right, value, priority)
         if node.right.priority > node.priority:
            node = Treap._rotateLeft(node)
      else:
         node.left  = Treap._insert(node.left,  value, priority)
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
      elif Treap.cmp(node.left, node.right) > 0: 
         node = Treap._rotateLeft(node)
         node.left = Treap._delete(node.left, value)
      elif Treap.cmp(node.left, node.right) < 0:
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

   return 0


if __name__ == '__main__':
   sys.exit(main())
