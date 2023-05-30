import requests

endpoint = "https://newsdata.io/api/1/news?country=ng&apikey=pub_23722bbbb170b2305f23bfeaa264033d4dd32"

response = requests.get(endpoint)
news_dict = dict(response.json())
print(type(news_dict))


for i in range(0, 5):
    api_news_title = news_dict['results'][i]['title']
    api_news_creator = news_dict["results"][i]["creator"]
    api_news_full_description = news_dict["results"][i]["description"]
    api_news_full_source_id = news_dict["results"][i]["source_id"]

    import requests

    endpoint = "http://127.0.0.1:8000/api/"

    response = requests.post(endpoint, data={"title":api_news_title, 
    "content":api_news_full_description, 
    "author":api_news_creator, 
    "source":api_news_full_source_id})




# print(response.json())
# mystatus = "title"
# input = new_dict.get(mystatus)

# if input:
#     print(f"the {mystatus} is {input}")
# else:
#     print('Wornggggggggggggg')
