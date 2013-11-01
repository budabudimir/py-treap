#!/usr/bin/python


from treap import TreapNode
from treap import Treap


class ImmutableTreap(Treap):

   def __init__(self):
      Treap.__init__(self)
      self.root = None

   def insert(self, value, priority=None):
      ret = ImmutableTreap()

      if not self.contains(value):
         ret.root = ImmutableTreap._insert(self.root, value, priority)
      else:
         ret.root = self.root

      return ret

   def delete(self, value):
      if not self.contains(value):
         return self

      t = ImmutableTreap()
      t.root = ImmutableTreap._delete(self.root, value)
      return t

   def merge(self, other):
      t = ImmutableTreap()
      t.root = ImmutableTreap._merge(self.root, other.root)
      return t

   def split(self, value):
      root = ImmutableTreap._insert(self.root, value, TreapNode.INFINITY)

      left = ImmutableTreap()
      right = ImmutableTreap()
      left.root, right.root = root.left, root.right

      return left, right


   @staticmethod
   def _insert(node, value, priority=None):
      if node is None:
         return TreapNode(value, priority)

      new = TreapNode(node=node)

      if new.value < value:
         new.right = ImmutableTreap._insert(new.right, value, priority)
         if new.right.priority > new.priority:
            new = ImmutableTreap._rotateLeft(new)
      else:
         new.left  = ImmutableTreap._insert(new.left,  value, priority)
         if new.left.priority > new.priority:
            new = ImmutableTreap._rotateRight(new)

      return new

   @staticmethod
   def _delete(node, value, create=True):
      if node.left is None and node.right is None:
         return None

      new = TreapNode(node=node)

      if node.value > value:
         new.left = ImmutableTreap._delete(new.left, value)
      elif node.value < value:
         new.right = ImmutableTreap._delete(new.right, value)
      elif Treap.cmp(node.left, node.right) > 0:
         new.right = TreapNode(node=new.right)
         new = Treap._rotateLeft(new)
         new.left = ImmutableTreap._delete(new.left, value, False)
      else:
         new.left = TreapNode(node=new.left)
         new = Treap._rotateRight(new)
         new.right = ImmutableTreap._delete(new.right, value, False)

      return new


   @staticmethod
   def _merge(A, B):
      if A is None: return B
      if B is None: return A

      if A.priority < B.priority:
         R = TreapNode(node=B)
         R.left = ImmutableTreap._merge(A, B.left)
      else:
         R = TreapNode(node=A)
         R.right = ImmutableTreap._merge(A.right, B)

      return R


def main():

   return 0


if __name__ == '__main__':
   import sys
   sys.exit(main())

