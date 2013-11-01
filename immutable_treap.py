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
   def _delete(node, value):
      if node.left is None and node.right is None:
         node = None
      elif node.value > value:
         node.left = ImmutableTreap._delete(node.left, value)
      elif node.value < value:
         node.right = ImmutableTreap._delete(node.right, value)
      elif Treap.cmp(node.left, node.right) > 0: 
         node.right = TreapNode(node=node.right)
         node = Treap._rotateLeft(node)
         node.left = ImmutableTreap._delete(node.left, value)
      elif Treap.cmp(node.left, node.right) < 0:
         node.left = TreapNode(node=node.left)
         node = Treap._rotateRight(node)
         node.right = ImmutableTreap._delete(node.right, value)
      else:
         assert False, "Impossible case"

      return node

def main():
   t = ImmutableTreap()
   x = t.insert(1)
   y = x.insert(2)

   lst = []
   for i in range(3, 10):
      lst.append(y.insert(i))

   for tree in lst:
      print tree.preorder()

   print x.contains(1)

   return 0


if __name__ == '__main__':
   import sys
   sys.exit(main())

