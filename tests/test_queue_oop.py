"""Tests of oop stack."""

import pytest

from data_structure.queue.oop_queue import Queue
from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption


def test_make_queue():
    queue = Queue()

    assert queue.size == 0
    assert queue.is_empty == True
    assert len(queue) == 0


def test_enqueue():
    queue = Queue()

    for i in range(3):
        queue.enqueue(i)

    assert queue.size == 3
    assert queue.is_empty == False
    assert len(queue) == 3


def test_dequeue_positive1():
    queue = Queue()

    for i in range(11, 15):
        queue.enqueue(i)

    assert queue.dequeue() == 11
    assert queue.size == 3
    assert queue.is_empty == False
    assert len(queue) == 3


def test_dequeue_positive2():
    queue = Queue()

    for i in range(21, 25):
        queue.enqueue(i)

    assert queue.dequeue() == 21
    assert queue.size == 3
    assert queue.is_empty == False
    assert len(queue) == 3

    assert queue.dequeue() == 22
    assert queue.size == 2
    assert queue.is_empty == False
    assert len(queue) == 2

    assert queue.dequeue() == 23
    assert queue.dequeue() == 24


def test_dequeue_from_empty_queue():
    queue = Queue()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = queue.dequeue()

    assert str(exception_info.value) == 'Queue is empty'
