# Mumbai Restaurant Data Scraper

This repository contains a Python script designed to fetch restaurant data from Swiggy's API for the city of Mumbai. The script collects various details about restaurants and saves them into a CSV file named `mumbai1.csv`.

## Project Overview

### Purpose
The purpose of this script is to scrape restaurant data, including information like name, location, average rating, cuisines, delivery time, and more, from Swiggy's platform for the city of Mumbai.

### Features
- **Data Collection**: Fetches restaurant data from Swiggy's API.
- **Data Storage**: Saves the collected data into a CSV file.
- **Multi-Page Support**: Handles multiple pages of restaurant listings.
- **Detailed Information**: Captures various attributes of each restaurant, such as type, id, name, city, area, average rating, total ratings, cuisines, cost for two, delivery time, address, and more.

## CSV File Format

The script saves the restaurant data in the following CSV format:


### Example of Data Captured

- **Type**: Type of restaurant.
- **ID**: Unique identifier for the restaurant.
- **Name**: Name of the restaurant.
- **UUID**: Universally unique identifier for the restaurant.
- **City**: City where the restaurant is located.
- **Area**: Area within the city.
- **Average Rating**: Average rating of the restaurant.
- **Total Ratings**: Total number of ratings.
- **Cuisines**: Cuisines offered by the restaurant.
- **Tags**: Additional tags or labels for the restaurant.
- **Cost for Two**: Estimated cost for two people.
- **Delivery Time**: Estimated delivery time.
- **Address**: Full address of the restaurant.
- **Locality**: Locality or neighborhood.
- **Unserviceable**: Indicates if the restaurant is currently unserviceable.
- **Veg**: Indicates if the restaurant offers vegetarian options.

## How to Run the Script

### Prerequisites

- Python 3.x
- Required libraries: `requests`, `json`, `io`

### Steps

1. Clone the repository.
2. Install the required Python libraries using pip:
   ```bash
   pip install requests
3. Run the Script
python swiggy.py

The data will be saved in the mumbai1.csv file.

Author
Aniruddha - Initial work - The script was developed by Aniruddha.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This `README.md` file provides an overview of the project, details the CSV file format, and gives instructions on how to run the script. It also includes information about the author and the license.
