
# adjust these
min_lat = 35
max_lat = 38
min_lon = -111
max_lon = -108
group_size = 1

"""
Scraper for https://www.ioverlander.com/.

Steps to use:
1) Define the min/max latitude and longitude you would like to query data from.
2) Adjust your group size.
3) Run the script. Data will be stored in data/iOverlander.csv. Make sure you have
a /data directory wherever you are running this or else it will not work.

Things to note:

latitude range = [-90, 90]
longitude range = [-180, 180]
        
group_size -> If you read the code below, you'll see that the URL that hits the API
    takes in two parameters:
    - searchboxmin = min_lat, min_lon
    - searchboxmax= max_lat, max_lon

    If we would like to query for a large area of land, say the entire world
    (min_lat = -90, max_lat = 90, min_lon=-180, max_lon=180), then we're asking
    the API for a very large amount of data.

    Since there are 100,000+ campsites on iOverlander, this call can lead to
    several problems:
    1) Will take a LONG time
    2) Could be flagged as suspicious
    3) Likely will time out

    Instead of fetching all this data with one massive call, we would like to break this
    call up into several smaller calls.

    You COULD make this happen by incrementing one of the four numbers by 1 until you hit
    all possible combinations of min_lat, max_lat, min_lon, max_lon, but since there are
    hundreds of thousands of possible combinations, this will also take a long time.
    i.e.
        Call 1: min_lat = -90, max_lat = 90, min_lon=-180, max_lon=180
        Call 2: min_lat = -89, max_lat = 90, min_lon=-180, max_lon=180
        Call 2: min_lat = -88, max_lat = 90, min_lon=-180, max_lon=180
        ...

    This will take forever!

    A better solution is to break these up into groupings. The group_size variable
    determines the size of these groupings.

    For example:
        group_size = 20
        lats = array([-90, -70, -50, -30, -10,  10,  30,  50,  70,  90])
        lons = array([-180, -160, -140, -120, -100,  -80,  -60,  -40,  -20,    0,   20,
             40,   60,   80,  100,  120,  140,  160,  180])

    Instead of incrementing by 1 (default), we now increment by the group_size (20).
    This reduces our number of API calls from hundreds of thousands to only 3,240.
    Much more manageable!

    If you are scraping data for the whole world, we recommend a group_size of 20.
    If you are scraping smaller areas, such as specific cities or states, we recommend
    setting the group_size to either 1 or a number that's about 20% of the difference
    between your min/max values.

    For example:
        min_lat = 50, max_lat = 70, min_lon=80, max_lon=100
        group_size = 20% of (70-50) = 4
"""

import numpy as np
import pandas as pd
import requests

lats = np.arange(min_lat, max_lat + group_size, group_size)
lons = np.arange(min_lon, max_lon + group_size, group_size)

all_data = []

for i in range(len(lats) - 1):
    for j in range(len(lons) - 1):
        print(lats[i], lats[i + 1], lons[j], lons[j + 1])

        url = f"https://www.ioverlander.com/places/search.json?searchboxmin={lats[i]}," \
              f"{lons[j]}&searchboxmax={lats[i+1]},{lons[j+1]}" # lat, lon

        payload = {}
        headers = {
            'authority': 'www.ioverlander.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-csrf-token':
                'CvDvIsL/4ux2JMgVyuP623OrMjZ7z8wAEeZxchhiYzumbLqS6dcLF5BsVjGTGEpRiPdjz/szHraWVRQ6R1ntnw==',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.ioverlander.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '_ga=GA1.2.1608494460.1640055767; _gid=GA1.2.670767212.1640055767; '
                      '_iOverlanderOnRails_session=l69Zyil4Negz93ySPU1NHXEgk4xV8zWDp1adIhIb9sFArNpx%2FHOPB26aCYL%2Ba0a5'
                      'QN88M%2BJj5%2BdcihcepZU6OIL1rIz6%2Fr%2B9HoIya678fe5M%2BfkcgGXBkDEymhjFql97sDd1iMwVbdlsfZM5Yfap%2'
                      'FsQGFH6SwZwJDbbg05PaZVA%2F6TcA3rtODuKJFJ2cFnDxXyN4gXcJHk5ZVzlFKAWvtsqvSt3C4ap%2FK%2F0j7wy%2FWeO5'
                      'A60psgWdtJsveUGQzXGDzoriLXcBlTc83YUxHg7tYq51mNFIh%2BT1BRchu3OpZj%2F6hWaRlQbnX2zdHgu%2BODJk6MkVNq'
                      'Qgx9t%2FIKMnUIWhqpf5X37fPveXlrCexsafL5qBFStbRNp1jhUQKnQOzxPCMEjG--%2B9Y5k1USOm35orj3--mgHvYl9Mq3'
                      'zGE0Yys68zOg%3D%3D'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = response.json()
        if json_data != None:
            all_data += json_data

data = pd.DataFrame(all_data)
data.to_csv("data/ioverlander.csv")
