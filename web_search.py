import requests

def web_search(query):

    url = "https://api.duckduckgo.com/"

    params = {
        "q": query,
        "format": "json"
    }

    response = requests.get(url, params=params)

    data = response.json()

    text = ""

    if data.get("Abstract"):
        text += data["Abstract"]

    if data.get("Heading"):
        text += " " + data["Heading"]

    if text == "":
        text = f"General information about {query}."

    return text[:400]