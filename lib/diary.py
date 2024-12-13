class Diary:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.word_count = 0
    
    def count_words(self):
        if isinstance(self.content, str):
            listed_content = self.content.split()
            return len(listed_content)
        else:
            return "Content type not supported"
        