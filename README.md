# Yt-recommendation-bot

# YouTube Video Recommender and Browser

This project consists of two main components:
1. A crawler script to fetch similar YouTube videos based on a given video ID.
2. A bot script to browse and watch these videos for a specified amount of time.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yt-recommender.git
    cd yt-recommender
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the ChromeDriver executable that matches your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory.

## Usage

### 1. Fetch Similar Videos

Run the `crawler.py` script to fetch similar videos based on a given video ID and export the video details to a CSV file.

```bash
python3 crawler.py "video_id_here"
