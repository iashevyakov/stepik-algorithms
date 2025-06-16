"""
https://stepik.org/lesson/13239/step/5?unit=3425
"""
from collections import defaultdict
from typing import Optional, Dict


class Node:
    """Класс для внутренних вершин кучи."""

    def __init__(self, left: "Node", right: "None"):
        self.left = left
        self.right = right

    def walk(self, coding: Dict[str, str], acc: str):
        self.left.walk(coding, acc + '0')
        self.right.walk(coding, acc + '1')


class Leaf:
    """Класс для листов кучи."""

    def __init__(self, char: str):
        self.char = char

    def walk(self, coding: dict, acc: str):
        coding[self.char] = acc or '0'


def huffman_coding(s: str):
    frequence = defaultdict(int)
    for c in s:
        frequence[c] += 1
    # очередь с приоритетами, реализованная на основе списка
    priority_queue = set()
    for c, f in frequence.items():
        priority_queue.add((c, f, Leaf(c)))
    n = len(frequence)
    for _ in range(n + 1, 2 * n):
        char_with_min_f = min(priority_queue, key=lambda e: e[1])
        priority_queue.discard(char_with_min_f)
        char_with_min_f_2 = min(priority_queue, key=lambda e: e[1])
        priority_queue.discard(char_with_min_f_2)
        priority_queue.add(
            (
                char_with_min_f[0] + char_with_min_f_2[0],
                char_with_min_f[1] + char_with_min_f_2[1],
                Node(char_with_min_f[2], char_with_min_f_2[2])
            )
        )

    coding = {}
    _, _, root = priority_queue.pop()
    root.walk(coding, "")
    return coding


def print_coding(coding: Dict[str, str]):
    for ch, code in coding.items():
        print(f"{ch}: {code}")


def coding_sequence(s: str, coding: Dict[str, str]) -> str:
    return "".join(coding[c] for c in s)

if __name__ == "__main__":
    s = input()
    coding = huffman_coding(s)
    sequence = coding_sequence(s, coding)
    print(len(coding), len(sequence))
    print_coding(coding)
    print(sequence)