import os
import argparse
import csv
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_video_details(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    if 'items' in video_response and video_response['items']:
        video = video_response['items'][0]
        tags = video['snippet'].get('tags', [])
        return tags
    return []

def search_videos_by_tags(tags, max_results=10):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    search_response = youtube.search().list(
        q=' '.join(tags),
        part='id,snippet',
        maxResults=max_results,
        type='video'
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append({
                'title': search_result['snippet']['title'],
                'description': search_result['snippet']['description'],
                'videoId': search_result['id']['videoId']
            })

    return videos

def save_videos_to_csv(videos, filename='similar_videos.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description', 'Video ID'])
        for video in videos:
            writer.writerow([video['title'], video['description'], video['videoId']])

def get_similar_videos(video_id):
    tags = get_video_details(video_id)
    if tags:
        similar_videos = search_videos_by_tags(tags)
        return similar_videos
    return []

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Find Similar YouTube Videos')
    parser.add_argument('video_id', help='YouTube Video ID')
    args = parser.parse_args()

    video_id = args.video_id
    similar_videos = get_similar_videos(video_id)

    if similar_videos:
        print("Similar Videos:")
        for video in similar_videos:
            print(f"Title: {video['title']}")
            print(f"Description: {video['description']}")
            print(f"Video ID: {video['videoId']}")
            print('---')

        save_videos_to_csv(similar_videos)
        print("Similar videos saved to similar_videos.csv")
    else:
        print(f"No similar videos found for video {video_id}")
