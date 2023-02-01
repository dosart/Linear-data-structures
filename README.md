# Linear-data-structures
[![Maintainability](https://api.codeclimate.com/v1/badges/a6ed21af264535d62746/maintainability)](https://codeclimate.com/github/dosart/Linear-data-structures/maintainability)
![CitHub_CI](https://github.com/dosart/Linear-data-structures/workflows/CitHub_CI/badge.svg)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Implementation of classic linear data structures:
* stack:
  * [imperative style](https://github.com/dosart/Linear-data-structures/blob/main/data_structure/stack/imperative_stack.py)
  * [oop style](https://github.com/dosart/Linear-data-structures/blob/main/data_structure/stack/oop_stack.py)
* queue:
  * [oop style](https://github.com/dosart/Linear-data-structures/blob/main/data_structure/queue/oop_queue.py)
  * [using two stacks](https://github.com/dosart/Linear-data-structures/blob/main/data_structure/queue/two_stacks_queue.py)
* linked list
  *  [oop style](https://github.com/dosart/Linear-data-structures/blob/main/data_structure/linked_list/linked_list.py)

The project was made as part of the [Coding Interview University](https://github.com/Ilyushin/google-interview-university) course.
### Stack implementation:
- [x] push(value) - adds item at storage
- [x] pop() - returns value and removes element
- [x] empty() - bool returns true if empty


### Queue implementation:
- [x] enqueue(value) - adds item at end of available storage
- [x] dequeue() - returns value and removes least recently added element
- [x] empty()

### Linked list implementation:
- [x] size() - returns number of data elements in list
- [x] empty() - bool returns true if empty
- [x] value_at(index) - returns the value of the nth item (starting at 0 for first)
- [x] push_front(value) - adds an item to the front of the list
- [x] pop_front() - remove front item and return its value
- [x] push_back(value) - adds an item at the end
- [x] pop_back() - removes end item and returns its value
- [x] front() - get value of front item
- [x] back() - get value of end item
- [x] insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
- [x] erase(index) - removes node at given index
- [ ] value_n_from_end(n) - returns the value of the node at nth position from the end of the list
- [ ] reverse() - reverses the list
- [x] remove_value(value) - removes the first item in the list with this value

### Calculations:
- [x] implementation of the shunting station algorithm
- [x] implementation of postfix expression calculations
