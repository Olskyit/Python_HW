from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Species(Base):
    __tablename__ = "species"

    species_id = Column(
        Integer,
        primary_key=True
    )

    type_id = Column(Integer)

    species_name = Column(String)

    species_amount = Column(Integer)

    date_start = Column(Date)

    species_status = Column(String(100))
