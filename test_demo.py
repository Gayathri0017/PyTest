import pytest
import sys
@pytest.mark.smoke
def test_asample1():
    a=1
    print(a)
@pytest.mark.reg
@pytest.mark.smoke
def test_csample2():
    b=2
    print(b)
    assert b<4
# @pytest.mark.skip(reason="Demo Skip")
# @pytest.mark.skipif(sys.version_info < (1, 10),reason="demo")
@pytest.mark.xfail(reason="expected to pass")
def test_bsample3():
    c=3
    print(c)
    assert 1+3==2
# def test_result():
#     test_sample1()
#     test_sample2()
#     test_sample3()

@pytest.mark.parametrize("test_inputs,Expected ",[(1,2),(2,3),(3,4)])
def inputs_test(test_inputs,expected):
    assert test_inputs+2==expected