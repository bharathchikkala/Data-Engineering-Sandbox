#here is the main thing data from website by using its API
import requests
parameters = {
    "amount": 10,
    "category": 9,
    "difficulty": "medium",
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
# print(response.json()["results"])
question_data = response.json()["results"] 
