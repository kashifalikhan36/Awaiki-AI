# from googleapiclient.discovery import build
# API_KEY="AIzaSyC4bmiRwvqo9WzVp_ZmExNdW7aspM-pbJ0"
# channel_id='codeRECODE'

# api_service_name = "youtube"
# api_version = "v3"

# #Getting Channel Data
# youtube=build(api_service_name,api_version,developerKey=API_KEY)

# def get_channel_stats():
#     request = youtube.channels().list(part="snippet,contentDetails,statistics",forUsername=channel_id)
#     response = request.execute()
#     print(response)
# get_channel_stats()


# Must be a single transcript.
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
transcript = YouTubeTranscriptApi.get_transcript("eMOA1pPVUc4")



# .format_transcript(transcript) turns the transcript into a JSON string.
# txt_formatted = formatter.format_transcript(transcript)
print(transcript)
# Now we can write it out to a file.
# with open('C:\\Users\\Kashif\\Documents\\hackathon_proj\\your_filename.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(txt_formatted)