"""Tests of queue."""

import pytest

from data_structure.linked_list.lincked_list import LinkedList
from data_structure.exceptions.collection_exeption import CollectionIsEmptyExeption
from data_structure.exceptions.error_messages import list_is_empty, index_out_of_range


def test_make_list():
    list = LinkedList()

    assert list.size == 0
    assert list.is_empty == True
    assert len(list) == 0


def test_push_front_in_empty_list():
    list = LinkedList()
    list.push_front(10)

    assert list.size == 1
    assert list.is_empty == False
    assert len(list) == 1


def test_front():
    list = LinkedList()
    list.push_front(1)

    assert list.front == 1
    assert list.size == 1
    assert list.is_empty == False
    assert len(list) == 1


def test_front_from_empty_list():
    list = LinkedList()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = list.front
    assert str(exception_info.value) == list_is_empty()


def test_push_back_in_empty_list():
    list = LinkedList()
    list.push_back(10)

    assert list.size == 1
    assert list.is_empty == False
    assert len(list) == 1


def test_back():
    list = LinkedList()
    list.push_back(10)

    assert list.back == 10
    assert list.size == 1
    assert list.is_empty == False
    assert len(list) == 1


def test_back_from_empty():
    list = LinkedList()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = list.back
    assert str(exception_info.value) == list_is_empty()


def test_back_and_push():
    list = LinkedList()
    list.push_back(11)

    assert list.back == 11
    assert list.front == 11

    assert list.size == 1
    assert list.is_empty == False
    assert len(list) == 1


def test_push_front_using_front():
    list = LinkedList()
    list.front = 10

    assert list.front == 10
    assert list.back == 10
    assert list.size == 1
    assert list.is_empty == False
    assert len(list) == 1


def test_push_back_using_back():
    list = LinkedList()
    list.back = 1

    assert list.front == 1
    assert list.back == 1
    assert list.size == 1
    assert list.is_empty == False
    assert len(list) == 1


def test_change_back_element():
    list = LinkedList()

    for i in range(5):
        list.push_back(i)

    assert list.back == 4
    assert list.front == 0

    list.back = 100

    assert list.back == 100
    assert list.front == 0


def test_change_front_element():
    list = LinkedList()

    for i in range(5):
        list.push_front(i)

    assert list.front == 4
    assert list.back == 0

    list.front = 100

    assert list.front == 100
    assert list.back == 0


def test_search_in_empty_list():
    list = LinkedList()

    assert list.contains(10) == False


@pytest.fixture()
def search_fixture():
    list = LinkedList()

    for i in range(5):
        list.push_front(i)

    return list


def test_search_first_element(search_fixture):
    list = search_fixture

    assert list.contains(0) == True


def test_search_middle_element(search_fixture):
    list = search_fixture

    assert list.contains(3) == True


def test_search_last_element(search_fixture):
    list = search_fixture

    assert list.contains(4) == True


def test_search_negative(search_fixture):
    list = search_fixture

    assert list.contains(11) == False


def test_search_in_empty_list_using_in():
    list = LinkedList()

    assert (10 in list) == False


def test_search_first_element_using_in(search_fixture):
    list = search_fixture

    assert (0 in list) == True


def test_search_middle_element_using_in(search_fixture):
    list = search_fixture

    assert (3 in list) == True


def test_search_last_element_using_in(search_fixture):
    list = search_fixture

    assert (4 in list) == True


def test_search_negative_using_in(search_fixture):
    list = search_fixture

    assert (12 in list) == False


@pytest.fixture()
def value_at_fixture():
    list = LinkedList()

    for i in range(10):
        list.push_back(i)

    return list


def test_value_at_zero(value_at_fixture):
    list = value_at_fixture

    assert list.value_at(0) == 0


def test_value_at_middle(value_at_fixture):
    list = value_at_fixture

    assert list.value_at(5) == 5


def test_value_at_last(value_at_fixture):
    list = value_at_fixture

    assert list.value_at(list.size - 1) == 9


def test_value_at_index_negative(value_at_fixture):
    list = value_at_fixture

    with pytest.raises(IndexError) as exception_info:
        value = list.value_at(-1)
    assert str(exception_info.value) == index_out_of_range()


def test_value_at_index_bigger(value_at_fixture):
    list = value_at_fixture

    with pytest.raises(IndexError) as exception_info:
        value = list.value_at(list.size)
    assert str(exception_info.value) == index_out_of_range()


def test_value_at_empty_list():
    list = LinkedList()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = list.value_at(list.size)
    assert str(exception_info.value) == list_is_empty()


def test_pop_front_positive(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.front == 0
    assert list.pop_front() == 0
    assert list.size == size - 1

    assert list.front == 1


def test_pop_front_negative(value_at_fixture):
    list = LinkedList()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = list.pop_front()
    assert str(exception_info.value) == list_is_empty()


def test_pop_back_positive(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.front == 0
    assert list.pop_back() == 9
    assert list.size == size - 1

    assert list.back == 8


def test_pop_front_negative(value_at_fixture):
    list = LinkedList()

    with pytest.raises(CollectionIsEmptyExeption) as exception_info:
        value = list.pop_back()
    assert str(exception_info.value) == list_is_empty()


def test_erase_first_element(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.front == 0

    list.erase(0)

    assert list.front == 1
    assert list.size == size - 1


def test_erase_back_element(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.back == 9

    list.erase(size - 1)

    assert list.back == 8
    assert list.size == size - 1


def test_erase_middle_element(value_at_fixture):
    list = value_at_fixture
    size = list.size

    fifth = list.value_at(5)
    sixth = list.value_at(6)

    list.erase(5)

    assert list.value_at(5) == sixth
    assert list.size == size - 1


def test_remove_firts_value(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.front == 0
    assert list.remove_value(0) is True
    assert list.size == size - 1
    assert list.front == 1


def test_remove_last_value(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.back == 9
    assert list.remove_value(9) is True
    assert list.size == size - 1
    assert list.back == 8


def test_remove_middle_value(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.remove_value(5) is True
    assert list.size == size - 1


def test_remove_negative(value_at_fixture):
    list = value_at_fixture
    size = list.size

    assert list.remove_value(100) is False
    assert list.size == size


def test_remove_from_empty_list():
    list = LinkedList()
    assert list.remove_value(100) is False
