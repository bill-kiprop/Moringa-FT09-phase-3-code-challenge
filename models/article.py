from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author, magazine):
        
        self._title = title
        self._content = content
        self._author = author
        self._magazine = magazine
        self._id = id

        
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''
                    INSERT INTO articles (title, content, author_id, magazine_id) 
                    VALUES (?, ?, ?, ?)
                ''', 
        (title, content, author.id, magazine.id))
        conn.commit()
        self._id = c.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title attribute is read-only")

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Content must be a non-empty string")
        self._content = value
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('UPDATE articles SET content = ? WHERE id = ?', (value, self._id))
        conn.commit()
        conn.close()

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine