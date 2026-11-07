import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Online Recipe Book",
    page_icon="🍳",
    layout="wide"
)

st.title("🍳 Online Recipe Book")
st.write("Discover, create and manage your favorite recipes!")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "View Recipes",
        "Add Recipe",
        "Manage Categories"
    ]
)


def api_get(endpoint, params=None):
    try:
        response = requests.get(
            f"{API_URL}{endpoint}",
            params=params,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        st.error("Cannot connect to the API. Is FastAPI running?")
        return None


def api_post(endpoint, data):
    try:
        response = requests.post(
            f"{API_URL}{endpoint}",
            json=data,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        st.error(f"Request failed: {error}")
        return None


def api_delete(endpoint):
    try:
        response = requests.delete(
            f"{API_URL}{endpoint}",
            timeout=5
        )
        response.raise_for_status()
        return True
    except requests.RequestException as error:
        st.error(f"Request failed: {error}")
        return False


# HOME PAGE

if menu == "Home":

    st.header("Welcome to your digital cookbook!")

    recipes = api_get("/recipes/")
    categories = api_get("/categories/")

    if recipes is not None:
        col1, col2 = st.columns(2)

        col1.metric("Total Recipes", len(recipes))
        col2.metric(
            "Total Categories",
            len(categories or [])
        )

        st.subheader("Recently available recipes")

        for recipe in recipes[:5]:
            with st.expander(recipe["name"]):
                st.write(recipe["description"])
                st.write("Cuisine:", recipe["cuisine"])
                st.write("Difficulty:", recipe["difficulty"])


# VIEW RECIPES

elif menu == "View Recipes":

    st.header("📖 Browse Recipes")

    search = st.text_input("Search by recipe name")

    cuisine = st.text_input("Filter by cuisine")

    difficulty = st.selectbox(
        "Difficulty",
        ["All", "Easy", "Medium", "Hard"]
    )

    params = {
        "search": search,
        "cuisine": cuisine
    }

    if difficulty != "All":
        params["difficulty"] = difficulty

    recipes = api_get("/recipes/", params)

    if recipes is not None:
        if not recipes:
            st.info("No recipes found.")

        for recipe in recipes:

            with st.expander(f"🍽️ {recipe['name']}"):

                st.write(recipe["description"])

                st.write("**Cuisine:**", recipe["cuisine"])
                st.write("**Difficulty:**", recipe["difficulty"])

                st.subheader("Ingredients")
                st.write(recipe["ingredients"])

                st.subheader("Instructions")
                st.write(recipe["instructions"])

                if st.button(
                    "Delete Recipe",
                    key=f"delete_{recipe['id']}"
                ):
                    if api_delete(
                        f"/recipes/{recipe['id']}"
                    ):
                        st.success("Recipe deleted!")
                        st.rerun()


# ADD RECIPE

elif menu == "Add Recipe":

    st.header("➕ Add a New Recipe")

    categories = api_get("/categories/") or []

    with st.form("recipe_form"):

        name = st.text_input("Recipe Name")

        description = st.text_area("Description")

        ingredients = st.text_area(
            "Ingredients (one per line)"
        )

        instructions = st.text_area(
            "Preparation Instructions"
        )

        cuisine = st.text_input("Cuisine")

        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"]
        )

        category_options = {
            "No category": None
        }

        category_options.update({
            category["name"]: category["id"]
            for category in categories
        })

        category_name = st.selectbox(
            "Category",
            list(category_options.keys())
        )

        submitted = st.form_submit_button(
            "Save Recipe"
        )

        if submitted:

            if not all([
                name.strip(),
                ingredients.strip(),
                instructions.strip(),
                cuisine.strip()
            ]):
                st.error("Please complete all required fields.")

            else:

                data = {
                    "name": name,
                    "description": description or None,
                    "ingredients": ingredients,
                    "instructions": instructions,
                    "cuisine": cuisine,
                    "difficulty": difficulty,
                    "category_id": category_options[category_name]
                }

                result = api_post("/recipes/", data)

                if result:
                    st.success("Recipe created successfully!")
                    st.rerun()


# MANAGE CATEGORIES

elif menu == "Manage Categories":

    st.header("📂 Manage Recipe Categories")

    with st.form("category_form"):

        category_name = st.text_input(
            "New Category Name"
        )

        submitted = st.form_submit_button(
            "Create Category"
        )

        if submitted:

            if category_name.strip():

                result = api_post(
                    "/categories/",
                    {"name": category_name}
                )

                if result:
                    st.success("Category created!")
                    st.rerun()

            else:
                st.error("Enter a category name.")

    st.divider()

    st.subheader("Existing Categories")

    categories = api_get("/categories/")

    if categories is not None:

        for category in categories:

            col1, col2 = st.columns([4, 1])

            col1.write(category["name"])

            if col2.button(
                "Delete",
                key=f"category_{category['id']}"
            ):

                if api_delete(
                    f"/categories/{category['id']}"
                ):
                    st.success("Category deleted!")
                    st.rerun()