# from youtube_timestamper.core import YoutubeTimestamper

# yt_ts = YoutubeTimestamper("https://www.youtube.com/watch?v=QGCvycOXs2M")

# text=yt_ts.suggest_question_timestamps(next_q_thresh=20)

# print(text)

import requests

def get_youtube_timestamp(api_key, video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=contentDetails&key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # if 'items' in data and len(data['items']) > 0:
    #     content_details = data['items'][0]['contentDetails']
    #     duration = content_details['duration']
    #     return duration
    
    return data

# Replace 'YOUR_API_KEY' with your actual YouTube Data API key
api_key = "AIzaSyC4bmiRwvqo9WzVp_ZmExNdW7aspM-pbJ0"
video_id = 'D56_Cx36oGY'

timestamp = get_youtube_timestamp(api_key, video_id)
if timestamp:
    print(f"The duration of the video (ID: {video_id}) is {timestamp}.")
else:
    print("Unable to retrieve the timestamp for the video.")
