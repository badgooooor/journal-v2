---
title: "Binary Trees"
date: 2026-10-23
tags: [algorithms, data-structures]
draft: true
---

A **binary tree** is a hierarchical data structure where each node has at most two children — a left child and a right child. It's one of the most fundamental structures in computer science.

The :viz{scene="BinaryTree"}[tree is built by inserting nodes one at a time based on comparison]. When a new value arrives, it travels down from the root: go left if smaller, go right if larger, until it finds an empty spot.

## Traversal

Reading all nodes in order requires a traversal strategy. The most common is **in-order traversal**, which visits nodes in sorted sequence.

When we :viz{scene="TreeTraversal"}[traverse the tree in-order, we visit left → root → right at each node]. For a valid binary search tree, this always produces a sorted sequence.

## Complexity

For a balanced tree with `n` nodes:

| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

An unbalanced tree degrades to O(n) in the worst case — which is why self-balancing variants like AVL trees and Red-Black trees exist.
