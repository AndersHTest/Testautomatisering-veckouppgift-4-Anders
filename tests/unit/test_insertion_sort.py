import pytest
from src.insertion_sort.insertion_sort import insertion_sort
from src.main import generate_list


@pytest.mark.unit
def test_insertion_sort():
    list_1 = []
    list_2 = [10]
    list_3 = [10, 8, 6, 4, 2, 0]

    result_1 = insertion_sort(list_1)
    result_2 = insertion_sort(list_2)
    result_3 = insertion_sort(list_3)

    sorted_1 = []
    sorted_2 = [10]
    sorted_3 = [0, 2, 4, 6, 8, 10]

    assert result_1 == sorted_1
    assert result_2 == sorted_2
    assert result_3 == sorted_3


@pytest.mark.performance
def test_insertion_sort__insertion_1(benchmark):
    a = generate_list(10000)

    benchmark(insertion_sort, a)


@pytest.mark.performance
def test_insertion_sort__insertion_2(benchmark):
    a = generate_list(12500)

    benchmark(insertion_sort, a)
