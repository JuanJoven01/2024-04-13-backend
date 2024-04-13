from pydantic import BaseModel, Field

class NewCandidate (BaseModel):
    brand: str = Field(min_length=1, max_length=20)
    office: str = Field(min_length=4, max_length=20)
    candidate: str = Field(min_length=4, max_length=30)

    class Config:
            orm_mode = True
            schema_extra = {
                "example": {
                    "brand": "Mazda",
                    "office": "Chapinero",
                    "candidate": "David Sandoval",
                }
            }