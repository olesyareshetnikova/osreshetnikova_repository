import os
import time

from functions import read, minimum, maximum, prod_of_numbers, summation


def test_read():
    assert read('test1/1.txt') == "Incorrect"
    assert read('test1/2.txt') == [88, 999, 8, 9, 890, -89, 88]
    assert read('test1/3.txt') == [5, 999, 7.8, 9.8, 6, 9.88888]
    assert read('test1/4.txt') == "Incorrect"


def test_minimum():
    assert minimum(read('test2/1.txt')) == "Incorrect"
    assert minimum(read('test2/2.txt')) == min([88, 999, 8, 9, 890, -89, 88])
    assert minimum(read('test2/3.txt')) == min([5, 999, 7.8, 9.8, 6, 9.88888])
    assert minimum(read('test2/4.txt')) == "Incorrect"


def test_maximum():
    assert maximum(read('test3/1.txt')) == "Incorrect"
    assert maximum(read('test3/2.txt')) == max([88, 999, 8, 9, 890, -89, 88])
    assert maximum(read('test3/3.txt')) == max([5, 999, 7.8, 9.8, 6, 9.88888])
    assert maximum(read('test3/4.txt')) == "Incorrect"


def test_summation():
    assert summation(read('test4/1.txt')) == "Incorrect"
    assert summation(read('test4/2.txt')) == sum([88, 999, 8, 9, 890, -89, 88])
    assert summation(read('test4/3.txt')) == sum([5, 999, 7.8, 9.8, 6, 9.88888])
    assert summation(read('test4/4.txt')) == "Incorrect"


def test_prod_of_numbers():
    assert prod_of_numbers(read('test5/1.txt')) == "Incorrect"
    assert prod_of_numbers(read('test5/2.txt')) == 88 * 999 * 8 * 9 * 890 * -89 * 88
    assert prod_of_numbers(read('test5/3.txt')) == 5 * 999 * 7.8 * 9.8 * 6 * 9.88888
    assert prod_of_numbers(read('test5/4.txt')) == "Incorrect"


def test_speed():
    tests = ['test6/1.txt', 'test6/2.txt', 'test6/3.txt', 'test6/4.txt']
    print('\n')
    print('Поиск max\n')
    for test in tests:
        t0 = time.time()
        maximum(read(test))
        print('время работы программы:', time.time() - t0, 'размер файла:', os.path.getsize(test))
    print('\n')
    print('Поиск min\n')
    for test in tests:
        t0 = time.time()
        minimum(read(test))
        print('время работы программы:', time.time() - t0, 'размер файла:', os.path.getsize(test))
    print('\n')
    print('Вычисление sum\n')
    for test in tests:
        t0 = time.time()
        summation(read(test))
        print('время работы программы:', time.time() - t0, 'размер файла:', os.path.getsize(test))
    print('\n')
    print('Вычисление prod\n')
    for test in tests:
        t0 = time.time()
        prod_of_numbers(read(test))
        print('время работы программы:', time.time() - t0, 'размер файла:', os.path.getsize(test))
