import requests;
from dotenv import load_dotenv;
import os;

load_dotenv();

API_URL = os.getenv("API_URL");
if API_URL is None:
    raise ValueError("API_URL environment variable not set");

def getRandomQuote():
    response = requests.get(API_URL);
    data = response.json();
    if data["statusCode"] == 200:
        return data["data"]["data"];
    else:
        return None;

def main() :
    data = getRandomQuote();
    # print(data);
    print(type(data));
    # print(data[0]["author"]);
    for mp in data:
        print(mp["content"]);
        print(mp["author"]);
        print("\n");

if __name__ == "__main__":
    main();