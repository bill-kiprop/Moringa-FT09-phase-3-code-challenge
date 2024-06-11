from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category=""):
        self._id = id
        self._name = name
        self._category = category

        
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        conn.commit()
        self._id = c.lastrowid
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
            
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('UPDATE magazines SET name = ? WHERE id = ?', (value, self._id))
            conn.commit()
            conn.close()
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
            
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('UPDATE magazines SET category = ? WHERE id = ?', (value, self._id))
            conn.commit()
            conn.close()
        else:
            raise ValueError("Category must be a non-empty string")