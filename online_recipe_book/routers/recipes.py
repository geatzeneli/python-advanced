import sqlite3

from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)

from database import get_db

from models.recipe import (
    RecipeCreate,
    RecipeUpdate,
    RecipeOut
)


router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)


# CREATE RECIPE

@router.post("/", response_model=RecipeOut)
def create_recipe(
    recipe: RecipeCreate,
    db: sqlite3.Connection = Depends(get_db)
):
    try:
        cursor = db.execute(
            """
            INSERT INTO recipes (
                name,
                description,
                ingredients,
                instructions,
                cuisine,
                difficulty,
                category_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                recipe.name.strip(),
                recipe.description,
                recipe.ingredients,
                recipe.instructions,
                recipe.cuisine.strip(),
                recipe.difficulty,
                recipe.category_id
            )
        )

        db.commit()

        return {
            "id": cursor.lastrowid,
            **recipe.model_dump()
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Invalid category ID"
        )


# GET ALL RECIPES AND FILTER

@router.get("/", response_model=list[RecipeOut])
def get_recipes(
    search: str = Query(default=""),
    cuisine: str = Query(default=""),
    difficulty: str = Query(default=""),
    category_id: Optional[int] = None,
    db: sqlite3.Connection = Depends(get_db)
):
    query = "SELECT * FROM recipes WHERE 1=1"

    parameters = []

    if search:
        query += " AND name LIKE ?"
        parameters.append(f"%{search}%")

    if cuisine:
        query += " AND cuisine LIKE ?"
        parameters.append(f"%{cuisine}%")

    if difficulty:
        query += " AND difficulty = ?"
        parameters.append(difficulty)

    if category_id is not None:
        query += " AND category_id = ?"
        parameters.append(category_id)

    query += " ORDER BY id DESC"

    rows = db.execute(
        query,
        parameters
    ).fetchall()

    return [dict(row) for row in rows]


# GET ONE RECIPE

@router.get("/{recipe_id}", response_model=RecipeOut)
def get_recipe(
    recipe_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
    row = db.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    ).fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )

    return dict(row)


# UPDATE RECIPE

@router.put("/{recipe_id}", response_model=RecipeOut)
def update_recipe(
    recipe_id: int,
    recipe: RecipeUpdate,
    db: sqlite3.Connection = Depends(get_db)
):
    existing = db.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    ).fetchone()

    if existing is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )

    updates = recipe.model_dump(exclude_unset=True)

    if not updates:
        return dict(existing)

    for field, value in updates.items():
        if field != "description" and value is not None:
            if isinstance(value, str) and not value.strip():
                raise HTTPException(
                    status_code=422,
                    detail=f"{field} cannot be empty"
                )

    fields = list(updates.keys())

    assignments = ", ".join(
        f"{field} = ?" for field in fields
    )

    values = list(updates.values())

    values.append(recipe_id)

    try:
        db.execute(
            f"""
            UPDATE recipes
            SET {assignments}
            WHERE id = ?
            """,
            values
        )

        db.commit()

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Invalid category ID"
        )

    updated = db.execute(
        "SELECT * FROM recipes WHERE id = ?",
        (recipe_id,)
    ).fetchone()

    return dict(updated)


# DELETE RECIPE

@router.delete("/{recipe_id}")
def delete_recipe(
    recipe_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.execute(
        "DELETE FROM recipes WHERE id = ?",
        (recipe_id,)
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )

    db.commit()

    return {
        "message": "Recipe deleted successfully"
    }