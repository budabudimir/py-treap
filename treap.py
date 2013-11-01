#!/usr/bin/python

import sys
import random


class TreapNode(object):
   MAX_RAND = 10000000
   INFINITY = MAX_RAND + 1

   def __init__(self, value=None, priority=None, node=None):
      if node is not None:
         self.value = node.value
         self.left = node.left
         self.right = node.right
         self.priority = node.priority
         return

      self.value = value
      self.left = None
      self.right = None

      if priority is None:
         self.priority = random.randint(0, TreapNode.MAX_RAND)
      else:
         self.priority = priority


class Treap(object):

   def insert(self, value, priority=None):
      raise NotImplementedError

   def delete(self, value):
      raise NotImplementedError

   def merge(self, other):
      raise NotImplementedError

   def split(self, other):
      raise NotImplementedError

   def contains(self, value):
      return Treap._contains(self.root, value)

   def preorder(self):
      return Treap._preorder(self.root)

   def inorder(self):
      return Treap._inorder(self.root)

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
