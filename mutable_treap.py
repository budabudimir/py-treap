#!/usr/bin/python


from treap import Treap
from treap import TreapNode


class MutableTreap(Treap):

   def __init__(self):
      Treap.__init__(self)
      self.root = None

   def insert(self, value, priority=None):
      if not self.contains(value):
         self.root = MutableTreap._insert(self.root, value, priority)

   def delete(self, value):
      if self.contains(value):
         self.root = MutableTreap._delete(self.root, value)
      else:
         raise AttributeError("Value does not exist")

   def merge(self, other):
      self.root = MutableTreap._merge(self.root, other.root)

   def split(self, value):
      self.root = MutableTreap._insert(self.root, value, TreapNode.INFINITY)

      right = MutableTreap()
      right.root = self.root.right
      self.root = self.root.left

      return right
      



   @staticmethod
   def _insert(node, value, priority=None):
      if node is None:
         return TreapNode(value, priority)

      if node.value < value:
         node.right = MutableTreap._insert(node.right, value, priority)
         if node.right.priority > node.priority:
            node = Treap._rotateLeft(node)
      else:
         node.left  = MutableTreap._insert(node.left,  value, priority)
         if node.left.priority > node.priority:
            node = Treap._rotateRight(node)

      return node

   @staticmethod
   def _delete(node, value):
      if node.left is None and node.right is None:
         node = None
      elif node.value > value:
         node.left = MutableTreap._delete(node.left, value)
      elif node.value < value:
         node.right = MutableTreap._delete(node.right, value)
      elif Treap.cmp(node.left, node.right) > 0: 
         node = Treap._rotateLeft(node)
         node.left = MutableTreap._delete(node.left, value)
      elif Treap.cmp(node.left, node.right) < 0:
         node = Treap._rotateRight(node)
         node.right = MutableTreap._delete(node.right, value)
      else:
         assert False, "Impossible case"

      return node

   @staticmethod
   def _merge(A, B):
      if A is None: return B
      if B is None: return A

      if A.priority < B.priority:
         B.left = MutableTreap._merge(A, B.left)
         return B
      else:
         A.right = MutableTreap._merge(A.right, B)
         return A

