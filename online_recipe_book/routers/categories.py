import sqlite3

from fastapi import APIRouter, Depends, HTTPException

from database import get_db
from models.category import CategoryCreate, CategoryOut


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post("/", response_model=CategoryOut)
def create_category(
    category: CategoryCreate,
    db: sqlite3.Connection = Depends(get_db)
):
    try:
        cursor = db.execute(
            "INSERT INTO categories (name) VALUES (?)",
            (category.name.strip(),)
        )

        db.commit()

        return {
            "id": cursor.lastrowid,
            "name": category.name.strip()
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )


@router.get("/", response_model=list[CategoryOut])
def get_categories(
    db: sqlite3.Connection = Depends(get_db)
):
    rows = db.execute(
        "SELECT id, name FROM categories ORDER BY name"
    ).fetchall()

    return [dict(row) for row in rows]


@router.get("/{category_id}", response_model=CategoryOut)
def get_category(
    category_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
    row = db.execute(
        "SELECT id, name FROM categories WHERE id = ?",
        (category_id,)
    ).fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return dict(row)


@router.put("/{category_id}", response_model=CategoryOut)
def update_category(
    category_id: int,
    category: CategoryCreate,
    db: sqlite3.Connection = Depends(get_db)
):
    try:
        cursor = db.execute(
            "UPDATE categories SET name = ? WHERE id = ?",
            (category.name.strip(), category_id)
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        db.commit()

        return {
            "id": category_id,
            "name": category.name.strip()
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Category name already exists"
        )


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.execute(
        "DELETE FROM categories WHERE id = ?",
        (category_id,)
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    db.commit()

    return {
        "message": "Category deleted successfully"
    }