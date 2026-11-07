from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class RecipeBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=150
    )

    description: Optional[str] = None

    ingredients: str = Field(
        min_length=2
    )

    instructions: str = Field(
        min_length=2
    )

    cuisine: str = Field(
        min_length=2
    )

    difficulty: str = Field(
        min_length=2
    )

    category_id: Optional[int] = None


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=150
    )

    description: Optional[str] = None
    ingredients: Optional[str] = None
    instructions: Optional[str] = None
    cuisine: Optional[str] = None
    difficulty: Optional[str] = None
    category_id: Optional[int] = None


class RecipeOut(RecipeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)