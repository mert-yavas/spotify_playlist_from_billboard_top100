# Creating Spotify Playlist from Billboard 100
## Overview
Hi, I'm Mert, and today is Day 46 of my "100 Days of Python" challenge. In this project, I've developed a Python script named 'main.py' that creates a Spotify playlist based on the Billboard Hot 100 chart for a specified date.

## Project Description
The script utilizes the BeautifulSoup library for web scraping to extract song titles from the Billboard Hot 100 chart for a given date. It then authenticates with Spotify, searches for the songs, and creates a private playlist on the user's Spotify account. The goal is to automate the process of generating a playlist from the top songs on the Billboard chart.

## How to Run
To use the script and create a Spotify playlist, follow these steps:

* Open the Python script: main.py
```bash
   python main.py
```
* Input the desired date in the format YYYY-MM-DD when prompted.
* Ensure you have the necessary libraries installed (requests, beautifulsoup4, spotipy).
* Run the script to authenticate with Spotify, fetch songs from Billboard, and create a private playlist.
* Make sure Python is installed on your system.
## Project Files
* main.py: Main Python script for web scraping Billboard 100 and creating a Spotify playlist.
Customization
Feel free to explore and modify the script according to your preferences. You can customize the CLIENT_ID, CLIENT_SECRET, and adjust the scope or cache_path for Spotify authentication. Additionally, adapt the script for different web pages if you want to scrape other charts.

## Dependencies
The project relies on the following Python libraries:

* requests: For making HTTP requests to scrape Billboard 100.
* BeautifulSoup: For parsing HTML and extracting song titles.
* spotipy: For authenticating with Spotify and managing playlists.
## Educational Insights
Through this project, you can gain insights into the following:

* Web Scraping: Learn the basics of web scraping using BeautifulSoup.
* Spotify API Integration: Understand how to authenticate and interact with the Spotify API using spotipy.
* Data Extraction: Explore methods to extract relevant information from a web page.
* Playlist Management: Learn how to create and add tracks to a Spotify playlist using Python.
## Conclusion
I hope you find the Spotify Playlist Creator script helpful for automating the process of generating playlists based on the Billboard Hot 100 chart. Feel free to explore, modify, and adapt the script to suit your specific needs. Happy coding!

Note: Be respectful when scraping websites and always check the website's terms of service.
