class Article:
    all_articles = []  # Class variable to store all Article instances

    def __init__(self, author, magazine, title):
        self._author = author  # Assign the provided author to the instance variable _author
        self._magazine = magazine  # Assign the provided magazine to the instance variable _magazine
        self._title = title  # Assign the provided title to the instance variable _title
        self.all_articles.append(self)
        # Add the current article instance to the list of all Article instances

    def title(self):
        return self._title
        # Returns the title of the article

    def author(self):
        return self._author
        # Returns the author of the article

    def magazine(self):
        return self._magazine
        # Returns the magazine associated with the article
