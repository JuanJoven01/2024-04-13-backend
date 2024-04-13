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

    brand: Mapped["Brands"] = relationship(back_populates="candidates", cascade="all, delete-orphan")
    office: Mapped["Brands"] = relationship(back_populates="candidates", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"

class Brands(Base): 
    __tablename__ = "brands"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    candidates: Mapped[List["Candidates"]] = relationship(back_populates="brand", cascade="all, delete-orphan",)
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
    
class Offices(Base):
    __tablename__ = "offices"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    candidates: Mapped[List["Candidates"]] = relationship(back_populates="office", cascade="all, delete-orphan",)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
    
