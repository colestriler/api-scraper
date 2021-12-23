# API Scraper

### What
A repo full of scripts that scrape public APIs.

### Why
There are many ways to collect data from the web. One way is to use a HTML scraper such as [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/). The problem with scraping directly from a site's page, however, is that often times your scraper will need to be redesigned after every major change to the site's HTML or CSS.

A more sophisticated approach to scraping data from the web is to tap into the API directly -- the source of where the data is coming from. In general, HTML scrapers should only be used if the site's API isn't accessible or doesn't give you the data you need.

### How to run
1. Clone the repo. Note: If you don't clone the repo and decide to run the Python script directly, make sure to create a `data/` folder in the same directory as the Python script.
2. Adjust any values inside the script.
2. Run `python <SCRIPT_NAME>.py` and your output will be created in the `data/` directory.
