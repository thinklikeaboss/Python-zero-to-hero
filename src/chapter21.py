# src/chapter21.py

"""
Chapter 21 – Web Development with Flask & FastAPI
Author: Luca Bocaletto
Description:
    Demonstrate building and testing simple web apps:
      - Flask app with routes, path parameters and form handling
      - FastAPI app with path & query parameters, Pydantic models
    Uses test clients to simulate HTTP requests and print responses.
"""

from flask import Flask, request, render_template_string
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient as _FastAPITestClient

# --- Flask setup ---
flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return "Hello, Flask!"

@flask_app.route("/greet/<name>")
def greet(name):
    return f"Welcome, {name}!"

# simple inline form & result templates
_FORM_HTML = """
<form method="post">
  <input name="data" placeholder="Enter something"/>
  <button type="submit">Send</button>
</form>
"""

_RESULT_HTML = """
<p>You submitted: <strong>{{ data }}</strong></p>
"""

@flask_app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        data = request.form.get("data", "")
        return render_template_string(_RESULT_HTML, data=data)
    return render_template_string(_FORM_HTML)

def demo_flask():
    print("== Flask Demo ==")
    client = flask_app.test_client()
    # GET /
    resp = client.get("/")
    print("GET / →", resp.data.decode())
    # GET /greet/Alice
    resp = client.get("/greet/Alice")
    print("GET /greet/Alice →", resp.data.decode())
    # GET /submit (form)
    resp = client.get("/submit")
    print("GET /submit →", resp.data.decode().splitlines()[0], "…")
    # POST /submit
    resp = client.post("/submit", data={"data": "Test123"})
    print("POST /submit →", resp.data.decode())
    print()


# --- FastAPI setup ---
fastapi_app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@fastapi_app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@fastapi_app.post("/items/")
def create_item(item: Item):
    return {"message": "Created", "item": item.dict()}

def demo_fastapi():
    print("== FastAPI Demo ==")
    client = _FastAPITestClient(fastapi_app)
    # GET /items/42?q=foo
    resp = client.get("/items/42", params={"q": "foo"})
    print("GET /items/42?q=foo →", resp.json())
    # POST /items/
    payload = {"name": "Widget", "price": 19.99}
    resp = client.post("/items/", json=payload)
    print("POST /items/ →", resp.json())
    print()


def main():
    print("\n=== Chapter 21: Web Development Demo ===\n")
    demo_flask()
    demo_fastapi()
    print("=== End of Chapter 21 ===\n")
    print("To run Flask server: FLASK_APP=chapter21.py flask run")
    print("To run FastAPI server: uvicorn chapter21:fastapi_app --reload\n")


if __name__ == "__main__":
    main()
