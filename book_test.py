import pytest
from lib.book import Book

def test_has_title():
    book = Book("And Then There Were None", 272)
    assert book.title == "And Then There Were None"

def test_has_page_count():
    book = Book("And Then There Were None", 272)
    assert book.page_count == 272

def test_page_count_must_be_integer():
    book = Book("And Then There Were None", 272)
    with pytest.raises(Exception):
        book.page_count = "not an integer"

def test_turn_page_output(capsys):
    book = Book("The World According to Garp", 69)
    book.turn_page()
    captured = capsys.readouterr()
    assert captured.out == "Flipping the page...wow, you read fast!\n"