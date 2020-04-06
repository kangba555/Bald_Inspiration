from max_list_func import max_list_sum
def test_max_list_sum1():
    assert max_list_sum([-20,11,-4,13,-5,-2],6)==20
def test_max_list_sum2():
    assert max_list_sum([-5,12,-5,-7,2,6],6)==12
def test_max_list_sum3():
    assert max_list_sum([6,2,-7,-5,12,-5],6)==12
