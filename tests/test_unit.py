import pytest

from pydantic import ValidationError
from src.models import Apartment
from src.models import Tenant

def test_apartment_fields():
    data = Apartment(
        key="apart-test",
        name="Test Apartment",
        location="Test Location",
        area_m2=50.0,
        rooms={
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    )
    assert data.key == "apart-test"
    assert data.name == "Test Apartment"
    assert data.location == "Test Location"
    assert data.area_m2 == 50.0
    assert len(data.rooms) == 2, f"Oczekiwano 3 mieszkań, ale znaleziono {len(data.rooms)}"


def test_apartment_from_dict():
    data = {
        "key": "apart-test",
        "name": "Test Apartment",
        "location": "Test Location",
        "area_m2": 50.0,
        "rooms": {
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    }
    apartment = Apartment(**data)
    assert apartment.key == data["key"]
    assert apartment.name == data["name"]
    assert apartment.location == data["location"]
    assert apartment.area_m2 == data["area_m2"]
    assert len(apartment.rooms) == len(data["rooms"])

    data['area_m2'] = "25m2" # Invalid field
    with pytest.raises(ValidationError):
        wrong_apartment = Apartment(**data)

def test_all_box_filled():
    data = Tenant(
        name="tenant-test",
        apartment="test apartment tenant",
        room="test tenant room",
        rent_pln=200,
        deposit_pln=100,
        date_agreement_from="test tenant agreement from",
        date_agreement_to="test tenant agreement to"
    )
    assert data.name == "tenant-test"
    assert data.apartment == "test apartment tenant"
    assert data.room == "test tenant room"
    assert data.rent_pln == 200
    assert data.deposit_pln == 100
    assert data.date_agreement_from == "test tenant agreement from"
    assert data.date_agreement_to == "test tenant agreement to"
