# -*- coding: utf-8 -*-
import unittest

from linked_list.node import Node


class NodeTestCase(unittest.TestCase):

    def test_node_str_representation_without_next(self):
        self.assertEqual(str(Node(9)), "Node(9) > /")

    def test_node_str_representation_with_next(self):
        n = Node(9)
        n.next = Node('X')
        self.assertEqual(str(n), "Node(9) > Node(X)")

    def test_node_equal_value(self):
        self.assertEqual(Node(1), Node(1))
        self.assertEqual(Node('hello'), Node('hello'))
        self.assertEqual(Node(True), Node(True))
        self.assertEqual(Node([1, 2, 3]), Node([1, 2, 3]))

    def test_node_not_equal_value(self):
        self.assertNotEqual(Node(1), Node(2))
        self.assertNotEqual(Node('hello'), Node('bye'))
        self.assertNotEqual(Node(True), Node(False))
        self.assertNotEqual(Node([1, 2, 3]), Node([3, 2, 1]))

    def test_node_equal_value_different_next_node(self):
        self.assertNotEqual(Node(1, next=Node('next1')),
                            Node(1, next=Node('next2')))
        self.assertNotEqual(Node('hello', next=Node('next1')),
                            Node('hello', next=Node('next2')))
        self.assertNotEqual(Node(True, next=Node('next1')),
                            Node(True, next=Node('next2')))
        self.assertNotEqual(Node([1, 2, 3], next=Node('next1')),
                            Node([1, 2, 3], next=Node('next2')))
