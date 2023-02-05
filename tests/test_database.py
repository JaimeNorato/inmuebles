from app.config.database import DataBase

def test_conect():
    db = DataBase('3.130.126.210', 3309, 'pruebas', 'VGbt3Day5R', 'habi_db')
    assert db.connect() is not None

def test_get_cursor():
    db = DataBase('3.130.126.210', 3309, 'pruebas', 'VGbt3Day5R', 'habi_db')
    assert db.get_cursor() is not None

def test_close():
    db = DataBase('3.130.126.210', 3309, 'pruebas', 'VGbt3Day5R', 'habi_db')
    assert db.close() is None