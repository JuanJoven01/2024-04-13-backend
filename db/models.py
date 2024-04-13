from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .config import Base

class Candidates(Base):
    __tablename__ = "candidates"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))
    office_id: Mapped[int] = mapped_column(ForeignKey("offices.id"))

    brand: Mapped["Brands"] = relationship(back_populates="candidates")
    office: Mapped["Offices"] = relationship(back_populates="candidates")
    
    def __repr__(self) -> str:
        return f"Candidates(id={self.id!r}, name={self.name!r}, brand_id={self.brand_id!r}, office_id={self.office_id!r})"

class Brands(Base): 
    __tablename__ = "brands"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    candidates: Mapped[List["Candidates"]] = relationship(back_populates="brand", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"Brands(id={self.id!r}, name={self.name!r})"
    
class Offices(Base):
    __tablename__ = "offices"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    candidates: Mapped[List["Candidates"]] = relationship(back_populates="office", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Offices(id={self.id!r}, name={self.name!r})"
    
