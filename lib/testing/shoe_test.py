import pytest
from lib.shoe import Shoe

def test_has_brand():
    shoe = Shoe("Nike", 10, "Leather")
    assert shoe.brand == "Nike"

def test_has_size():
    shoe = Shoe("Nike", 10, "Leather")
    assert shoe.size == 10

def test_size_must_be_integer():
    shoe = Shoe("Nike", 10, "Leather")
    with pytest.raises(Exception):
        shoe.size = "not an integer"

def test_has_material():
    shoe = Shoe("Nike", 10, "Leather")
    assert shoe.material == "Leather"

def test_has_default_condition():
    shoe = Shoe("Nike", 10, "Leather")
    assert shoe.condition == "Used"

def test_cobble_makes_new():
    shoe = Shoe("Nike", 10, "Leather")
    shoe.cobble()
    assert shoe.condition == "New"

def test_cobble_output(capsys):
    shoe = Shoe("Nike", 10, "Leather")
    shoe.cobble()
    captured = capsys.readouterr()
    assert captured.out == "Your shoe is as good as new!\n"
        
        
   
