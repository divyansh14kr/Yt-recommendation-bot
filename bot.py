import time
import argparse
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def read_video_ids_from_csv(filename='similar_videos.csv'):
    video_ids = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            video_ids.append(row['Video ID'])
    return video_ids

def browse_videos(video_ids, watch_time):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Connect to the running chromedriver instance
    driver = webdriver.Remote(command_executor='http://localhost:53768', options=chrome_options)

    # Browse and watch videos
    for i, video_id in enumerate(video_ids):
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"Watching video {i+1}/{len(video_ids)}: {video_url}")
        driver.get(video_url)̀
        time.sleep(watch_time)  # Watch the video for the specified time

    # Close the WebDriver
    driver.quit()

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='YouTube Video Browsing Bot')
    parser.add_argument('watch_time', type=int, help='Time to watch each video (in seconds)')
    args = parser.parse_args()

    watch_time = args.watch_time
    video_ids = read_video_ids_from_csv()

    if video_ids:
        browse_videos(video_ids, watch_time)
    else:
        print("No video IDs found in the CSV file.")
