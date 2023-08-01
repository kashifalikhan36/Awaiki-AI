from googleapiclient.discovery import build
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api import YouTubeTranscriptApi
class YtInfo:
    def __init__(self):
        self.subtitle_result=''

    #Searching Channel Info From Channel Username
    def channel_info_by_username(self,channel_username):

        API_KEY="AIzaSyC4bmiRwvqo9WzVp_ZmExNdW7aspM-pbJ0"
        channel_username=channel_username[25:]

        api_service_name = "youtube"
        api_version = "v3"

        #Getting Channel Data
        youtube=build(api_service_name,api_version,developerKey=API_KEY)

        def get_channel_stats():
            request=youtube.channels().list(part='snippet,contentDetails,statistics',forUsername=channel_username)
            response=request.execute()
            
            #Tried to get channel name in dict...
            # print(response['items'][0]['snippet']['title'])
            
            with open("C:\\Users\\Kashif\\Documents\\hackathon_proj\\channel_info.json",'w') as file:
                file.write(str(response))
            return response
        get_channel_stats()
    
    #Searching Channel Info From Channel Id
    def channel_info_by_id(self,channel_id):

        API_KEY="AIzaSyC4bmiRwvqo9WzVp_ZmExNdW7aspM-pbJ0"
        channel_id=channel_id[32:57]

        api_service_name = "youtube"
        api_version = "v3"

        #Getting Channel Data
        youtube=build(api_service_name,api_version,developerKey=API_KEY)

        def get_channel_stats():
            request=youtube.channels().list(part='snippet,contentDetails,statistics',id=channel_id)
            response=request.execute()
            #Tried to get channel name in dict...
            # print(response['items'][0]['snippet']['title'])
            with open("C:\\Users\\Kashif\\Documents\\hackathon_proj\\channel_info.json",'w') as file:
                file.write(str(response))
            return response
        get_channel_stats()

    #Subtitle Scraping From YT Videos
    def subtitle_info(self,yt_video_link):
        def Get_subtitle(video_code):
            subtitle=YouTubeTranscriptApi.get_transcript(video_code)
            print(subtitle)
            with open("C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\subtitle.txt",'w') as file:
                subtitle_result_text = TextFormatter().format_transcript(subtitle)
                file.write(str(subtitle_result_text))
            with open("C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\subtitle.json",'w') as file:
                file.write(str(subtitle))
        try:
            Get_subtitle(yt_video_link[32:43])
        except:
            Get_subtitle(yt_video_link[17:29])
        return self.subtitle_result
