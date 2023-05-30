import requests


home_page_endpoint = "http://127.0.0.1:8000/api/"

# response = requests.get(home_page_endppoint)

TWO_POST_DATA = {
    "title":"Blog Post 3",
    "content":"Blog Post Content",
    "author":"ina",
    "source":"channels"
}
new_post = requests.post(home_page_endpoint, data=TWO_POST_DATA)
print(new_post.json())