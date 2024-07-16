class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title  
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Title attribute cannot be changed after instantiation")
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters long")


class Author:
    def __init__(self, name):
        self._set_name(name)

    @property
    def name(self):
        return self._name

    def _set_name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Name attribute cannot be changed after instantiation")
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must not be empty")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list(set(magazine.category for magazine in self.magazines()))
        if topic_areas:
            return topic_areas
        else:
            return None
        
from collections import Counter 
      
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters long")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        articles = [article.title for article in self.articles()]
        return articles if articles else None
    
    def contributing_authors(self):
        author_counts = Counter(article.author for article in self.articles())
        return [author for author, count in author_counts.items() if count > 2] or None
