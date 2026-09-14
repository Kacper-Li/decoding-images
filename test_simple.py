import pytest
from simple import count_consecutives

def test_consecutive_valid():
    input_arr = [0,0,0,0,0,1,1,1,1]
    output_arr = count_consecutives(input_arr)
    correct = [5,4]
    assert output_arr == correct
    
def test_consecutive_valid_larger():
    input_arr = [0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
    output_arr = count_consecutives(input_arr)
    correct = [5,4,3,2,1,1,4,12]
    assert output_arr == correct
    
def test_consecutive_valid_1():
    input_arr = [0]
    output_arr = count_consecutives(input_arr)
    correct = [1]
    assert output_arr == correct
    
def test_consecutive_valid_single():
    input_arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    output_arr = count_consecutives(input_arr)
    correct = [23]
    assert output_arr == correct
    
def test_consecutive_valid_multiple_singles():
    input_arr = [0,1,0,1,0,1,0,1,0,1,0,1,0]
    output_arr = count_consecutives(input_arr)
    correct = [1,1,1,1,1,1,1,1,1,1,1,1,1]
    assert output_arr == correct


"""Error tests for robustness (not needed for now)"""
def test_consecutive_invalid():
    input_arr = []
    with pytest.raises(IndexError):
        output_arr = count_consecutives(input_arr)