import pytest
from quicksort import quicksort

@pytest.mark.parametrize(
    "input_arr, expected_arr",
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([5, 2, 8, 2, 5], [2, 2, 5, 5, 8]),
        ([4, 3, 7, 2, 5, 1], [1, 2, 3, 4, 5, 7]),
        ([-4, 3, -7, 2, -5, 1], [-7, -5, -4, 1, 2, 3]),
    ],
)
def test_quicksort(input_arr, expected_arr):
    quicksort(0, len(input_arr) - 1, input_arr)
    assert input_arr == expected_arr
