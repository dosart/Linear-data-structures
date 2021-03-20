"""Tests of queue."""

import pytest

from data_structure.queue.oop_queue import Queue as ArrayQueue
from data_structure.queue.two_stacks_queue import Queue as StackQueue
from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption


@pytest.mark.parametrize("Queue", [ArrayQueue, StackQueue])
def test_make_queue(Queue):
    queue = Queue()
    assert queue.size == 0
    assert queue.is_empty == True
    assert len(queue) == 0


@pytest.mark.parametrize("Queue", [ArrayQueue, StackQueue])
def test_enqueue(Queue):
    queue = Queue()

    for i in range(3):
        queue.enqueue(i)

    assert queue.size == 3
    assert queue.is_empty == False
    assert len(queue) == 3


@pytest.mark.parametrize("Queue", [ArrayQueue, StackQueue])
def test_dequeue_positive1(Queue):
    queue = Queue()

    for i in range(11, 15):
        queue.enqueue(i)

    assert queue.dequeue() == 11
    assert queue.size == 3
    assert queue.is_empty == False
    assert len(queue) == 3


@pytest.mark.parametrize("Queue", [ArrayQueue, StackQueue])
def test_dequeue_positive2(Queue):
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


@pytest.mark.parametrize("Queue", [ArrayQueue, StackQueue])
def test_dequeue_positive3(Queue):
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.dequeue() == 1
    queue.enqueue(3)

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


@pytest.mark.parametrize("Queue", [ArrayQueue, StackQueue])
def test_dequeue_from_empty_queue(Queue):
    queue = Queue()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = queue.dequeue()

    assert str(exception_info.value) == 'Queue is empty'
