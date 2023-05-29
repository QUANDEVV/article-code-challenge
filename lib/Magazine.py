import Article  # Import the Article module

class Magazine:
    all_magazines = []  # Class variable to store all Magazine instances

    def __init__(self, name, category):
        self._name = name  # Assign the provided name to the instance variable _name
        self._category = category  # Assign the provided category to the instance variable _category
        self.all_magazines.append(self)
        # Add the current magazine instance to the list of all Magazine instances

    def name(self):
        return self._name
        # Returns the name of this magazine

    def category(self):
        return self._category
        # Returns the category of this magazine

    @classmethod
    def all(cls):
        return cls.all_magazines
        # Returns a list of all Magazine instances

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.name() == name:
                return magazine
        # Iterates over all Magazine instances and returns the first magazine object that matches the given name

    @classmethod
    def article_titles(cls):
        return [article.title() for article in Article.all_articles if article.magazine() == cls]
        # Returns a list of titles of all articles written for magazines of the current class (Magazine)

    def contributing_authors(self):
        authors = [article.author() for article in Article.all_articles if article.magazine() == self]
        # Retrieves a list of authors who have written articles for the current magazine instance
        return [author for author in authors if authors.count(author) > 2]
        # Returns a list of authors who have written more than 2 articles for the current magazine instance
