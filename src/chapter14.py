# src/chapter14.py

"""
Chapter 14 – JSON, XML & HTTP Requests
Author: Luca Bocaletto
Description:
    Demonstrate Python's handling of JSON, XML parsing with ElementTree,
    and making HTTP GET/POST requests using the requests library.
"""

import json
import xml.etree.ElementTree as ET
import requests

def demo_json():
    print("== JSON Demo ==")
    data = {
        "user": "alice",
        "active": True,
        "roles": ["admin", "user"],
        "settings": {"theme": "dark", "notifications": False}
    }
    # Serialize to JSON text
    text = json.dumps(data, indent=2)
    print("Serialized JSON:\n", text, sep="")
    # Deserialize back to Python object
    obj = json.loads(text)
    print("Deserialized object:", obj)
    print("Roles:", obj["roles"])
    print()

def demo_xml():
    print("== XML Demo ==")
    xml_string = """
    <root>
      <item id="1">Foo</item>
      <item id="2">Bar</item>
      <config>
        <option name="debug">true</option>
      </config>
    </root>
    """
    root = ET.fromstring(xml_string)
    print("Items found:")
    for item in root.findall("item"):
        print(f"  id={item.get('id')} → {item.text}")
    cfg = root.find("config/option")
    if cfg is not None:
        print(f"Config '{cfg.get('name')}' = {cfg.text}")
    print()

def demo_http():
    print("== HTTP Requests Demo ==")
    # 1) Simple GET with query parameters
    try:
        resp = requests.get(
            "https://httpbin.org/get",
            params={"q": "python", "page": 1},
            timeout=5
        )
        print("GET status:", resp.status_code)
        print("GET response JSON:", resp.json())
    except requests.RequestException as e:
        print("GET request failed:", e)
    print()

    # 2) POST JSON body
    payload = {"name": "bob", "age": 30}
    headers = {"Content-Type": "application/json"}
    try:
        resp = requests.post(
            "https://httpbin.org/post",
            json=payload,
            headers=headers,
            timeout=5
        )
        print("POST status:", resp.status_code)
        # httpbin returns JSON including our payload
        data = resp.json().get("json")
        print("POST echoed JSON:", data)
    except requests.RequestException as e:
        print("POST request failed:", e)
    print()

def main():
    print("\n=== Chapter 14: JSON, XML & HTTP Requests Demo ===\n")
    demo_json()
    demo_xml()
    demo_http()
    print("=== End of Chapter 14 ===\n")

if __name__ == "__main__":
    main()
