from config.database import DataBase


def test_conect():
    db = DataBase()
    assert db.connect() is not None


def test_get_cursor():
    db = DataBase()
    assert db.get_cursor() is not None


def test_close():
    db = DataBase()
    assert db.close() is None
