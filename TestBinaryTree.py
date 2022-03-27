#  File: TestBinaryTree.py

#  Description: Creates and performs multiple methods for a binary tree.

# vStudent Name: Sneha Venkatesan

#  Student UT EID: sv23377

#  Partner Name: Liyan Deng

#  Partner UT EID: ld26995

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: 3-27-2022

#  Date Last Modified: 3-27-2022

import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1

class Queue(object):
  '''Queue implements the FIFO principle.'''
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    if(not self.isEmpty()):
      return self.queue.pop(0)
    else:
      return None

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

  # a string representation of this stack.
  def __str__(self):
    return str(self.queue)

class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        left_most = self.root
        right_most = self.root
        while(left_most.lChild is not None):
            left_most = left_most.lChild

        while(right_most.rChild is not None):
            right_most = right_most.rChild

        return right_most.data - left_most.data

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        if (self.root is None or level >= self.get_height()):
            return []

        if (level == 0):
            return [self.root]
        else:
            list = []
            tree_queue = Queue()
            total = 2 ** level
            tree_queue.enqueue(self.root)
            while (tree_queue.size() <= total):
                current = tree_queue.dequeue()
                tree_queue.enqueue(current.rChild)
                tree_queue.enqueue(current.lChild)

            for i in range(total - 1):
                list.append(tree_queue.dequeue())

        return list


    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        pass


    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        pass






def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
