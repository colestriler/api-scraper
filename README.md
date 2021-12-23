# API Scraper

### What
A repo full of scripts that scrape public APIs.

### Why
There are many ways to collect data from the web. One way is to use a HTML scraper such as [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/). The problem with scraping directly from a site's page, however, is that often times your scraper will need to be redesigned after every major change to the site's HTML or CSS.

A more sophisticated approach to scraping data from the web is to tap into the API directly -- the source of where the data is coming from. APIs are less likely to change as often as a site's HTML or CSS and will load the data much cleaner and faster. Collecting data from the API directly is a much cleaner approach. HTML scrapers should only be used if the site's API isn't public or accessible.
