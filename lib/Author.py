import Article


class Author:
    all_authors = []



# initializiers 
    def __init__(self, name):
        self._name = name
        self.all_authors.append(self)

    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all_articles if article.author() == self]

    def magazines(self):
        return list(set(article.magazine() for article in self.articles()))
    # Returns a list of unique magazines that the author has contributed to

    

# writers  allows you to add a new article 
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article
    

    def topic_areas(self):
        return list(set(magazine.category() for magazine in self.magazines()))
    

    # Returns a list of unique topic areas/categories of the magazines the author has contributed to
