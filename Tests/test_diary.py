from lib.diary import *

def test_add_a_title():
    title = "Wednesday, December 11th"
    content = "This is my content"
    diary = Diary(title, content)
    assert diary.title == ("Wednesday, December 11th")

def test_add_content():
    title = "Wednesday, December 11th"
    content = "This is my content"
    diary = Diary(title, content)
    assert diary.content == ("This is my content")
    
def test_word_count():
    diary = Diary("Wednesday, December 11th", "This entry has five words")
    result = diary.count_words()
    assert result == 5

def test_word_count_non_string():
    diary = Diary("Wednesday, December 11th", 5)
    result = diary.count_words()
    assert result == "Content type not supported"
