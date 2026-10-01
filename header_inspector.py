import requests
import json


urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://httpbin.org/get"
]


for url in urls:
    response = requests.get(url)

    print("\n" + "=" * 60)
    print(f"URL: {url}")
    print("=" * 60)

    content_type = response.headers.get("Content-Type", "Not specified")
    content_length = response.headers.get("Content-Length", "Not specified")

    print(f"Content-Type: {content_type}")
    print(f"Content-Length: {content_length}")

    cache_headers = [
        "Cache-Control",
        "Expires",
        "ETag",
        "Last-Modified"
    ]

    cache_found = False

    print("\nCaching Headers:")
    for header in cache_headers:
        if header in response.headers:
            print(f"  {header}: {response.headers[header]}")
            cache_found = True

    if not cache_found:
        print("  None")

    rate_limit_headers = [
        "X-RateLimit-Limit",
        "X-RateLimit-Remaining",
        "X-RateLimit-Reset"
    ]

    rate_found = False

    print("\nRate-Limit Headers:")
    for header in rate_limit_headers:
        if header in response.headers:
            print(f"  {header}: {response.headers[header]}")
            rate_found = True

    if not rate_found:
        print("  None")

    print(f"\nTotal Response Headers: {len(response.headers)}")


data = {
    "message": "Testing custom headers"
}

custom_headers = {
    "X-Student-Name": "Bilal"
}

response = requests.post(
    "https://httpbin.org/post",
    json=data,
    headers=custom_headers
)

print("\n" + "=" * 60)
print("POST TO HTTPBIN")
print("=" * 60)

print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))