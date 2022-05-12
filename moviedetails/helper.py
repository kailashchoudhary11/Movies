import requests
from dotenv import load_dotenv
from django.shortcuts import render
import os 
load_dotenv()

def get_movie_data(name):
    API_KEY = os.getenv("API_KEY")
    url = f"https://www.omdbapi.com/?t={name}&apikey={API_KEY}"
    data = requests.get(url)
    # print(data.json())
    return data.json()


def apology(request, message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render(request, "moviedetails/apology.html", {"top" : code, "bottom":escape(message)})
