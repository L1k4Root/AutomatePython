import requests


def get_api_key():
    """Read the API key from a file."""
    with open("00-API-Key.txt", "r") as file:
        api_key = file.read().strip()
    return api_key

url = f"https://newsapi.org/v2/everything?q=Apple&from=2025-07-31&sortBy=popularity&apiKey={get_api_key()}"
response = requests.get(url)
content = response.json() 
print("=== Response Object ===")
# print(response)

print("\n=== Status Code ===")
print(response.status_code)

print("\n=== JSON Response ===")
# print(content)

print("\n=== Articles ===")
# print(content['articles'])