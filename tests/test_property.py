from models.property import Property
from services.property_service import PropertyService


def test_find_all():
    properties = Property().find_all()
    assert properties is not None


def test_find_filter():
    properties = Property().filter({"status": "en_venta", "city": "bogota"})
    assert properties is not None


def test_service_find_all():
    properties = PropertyService().get_all()
    assert properties is not None


def test_service_find_filter():
    properties = PropertyService().filter({"status": "en_venta", "city": "bogota"})
    assert properties is not None
