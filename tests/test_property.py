from app.models.property import Property

def test_find_all():
    properties = Property().find_all()
    assert properties is not None