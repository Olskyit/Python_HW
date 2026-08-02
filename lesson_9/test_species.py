from datetime import date

from models import Species


def test_add_species(session):
    species = Species(
        type_id=1,
        species_name="Test animal",
        species_amount=10,
        date_start=date(2026, 1, 1),
        species_status="active"
    )

    session.add(species)
    session.commit()

    species_id = species.species_id

    created_species = (
        session.query(Species)
        .filter_by(species_id=species_id)
        .first()
    )

    try:
        assert created_species is not None
        assert created_species.species_amount == 10

    finally:
        session.delete(species)
        session.commit()


def test_update_species(session):
    species = Species(
        type_id=1,
        species_name="Update animal",
        species_amount=5,
        date_start=date(2026, 1, 1),
        species_status="active"
    )

    session.add(species)
    session.commit()

    species.species_amount = 20
    session.commit()

    updated_species = (
        session.query(Species)
        .filter_by(species_id=species.species_id)
        .first()
    )

    try:
        assert updated_species.species_amount == 20

    finally:
        session.delete(species)
        session.commit()


def test_delete_species(session):
    species = Species(
        type_id=1,
        species_name="Delete animal",
        species_amount=15,
        date_start=date(2026, 1, 1),
        species_status="active"
    )

    session.add(species)
    session.commit()

    species_id = species.species_id

    session.delete(species)
    session.commit()

    deleted_species = (
        session.query(Species)
        .filter_by(species_id=species_id)
        .first()
    )

    assert deleted_species is None
