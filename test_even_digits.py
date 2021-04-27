import pytest
from even_digits import even_digits

def test_even_digits():
    string = '200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288'
    assert even_digits(200, 400) == string
