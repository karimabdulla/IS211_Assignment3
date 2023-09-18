import argparse
import urllib.request
import logging
import csv
import datetime
import re


def downloadData(url):
    """
        Reads data from a URL and returns the data as a string
        :param url:
        :return: the content of the URL
        """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')
    # return the data
    return response


def processData(file_content):

    result_dict = {}
    lines = file_content.split("\n")

    for line in lines:
        try:
            items = line.split(",")
            filepath = int(items[0])
            date_str = items[1]
            datetime = datetime.datetime.strptime(date_str, "'%m/%d/%Y %H:%M:%S")
            browser = items[2]
            status = items[3]
            request_size = items[4]
            result_dict[filepath] = (filepath, datetime, browser, status, request_size)
        except Exception as e:
            print(f"Error processing line: {line}")
            print(e)
    return result_dict

IMAGE_EXTENSIONS = re.compile(r"\.(jpe?g|png|gif)$", re.IGNORECASE)
with open("C:\\Users\\abdul\\Downloads\\weblog.csv", "r") as f:
    reader = csv.reader(f)

    image_hits = 0
    total_hits = 0

    for row in reader:
        filepath = row[0]

        # Check if the file extension is an image file extension
        if IMAGE_EXTENSIONS.match(filepath):
            image_hits += 1

        total_hits += 1
image_hits_percentage = image_hits / total_hits * 100
print(f"Image requests account for {image_hits_percentage:.1f}% of all requests")


FIREFOX_REGEX = re.compile(r"Firefox", re.IGNORECASE)
CHROME_REGEX = re.compile(r"Chrome", re.IGNORECASE)
IE_REGEX = re.compile(r"Internet Explorer", re.IGNORECASE)
SAFARI_REGEX = re.compile(r"Safari", re.IGNORECASE)

with open("C:\\Users\\abdul\\Downloads\\weblog.csv", "r") as f:
    reader = csv.reader(f)

    browser_counts = {
        "Firefox": 0,
        "Chrome": 0,
        "Internet Explorer": 0,
        "Safari": 0,
    }

    for row in reader:
        browser = row[2]

        # Match the browser against the regular expressions
        if FIREFOX_REGEX.match(browser):
            browser_counts["Firefox"] += 1
        elif CHROME_REGEX.match(browser):
            browser_counts["Chrome"] += 1
        elif IE_REGEX.match(browser):
            browser_counts["Internet Explorer"] += 1
        elif SAFARI_REGEX.match(browser):
            browser_counts["Safari"] += 1

hour_counts = {}
with open("C:\\Users\\abdul\\Downloads\\weblog.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        date_str = row[1]
        datetime_accessed = datetime.datetime.strptime(date_str, "'%m/%d/%Y %H:%M:%S")
        # Get the hour of the day
        hour = datetime_accessed.hour

        # Increment the count for the hour
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

sorted_hour_counts = sorted(hour_counts.items(), key=lambda item: item[1], reverse=True)
for hour, count in sorted_hour_counts:
    print(f"Hour {hour} has {count} hits")

def main(url):
    print(f"Running main with URL = {url}...")
    url_data = downloadData(url)
    data_dict = processData(url_data)
if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)


