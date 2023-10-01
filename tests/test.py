API_KEY="YJdGAsBHOb63G6am1NPnSwtt"

from resemble import Resemble
  
Resemble.api_key(API_KEY)

project_uuid = '<project_uuid>'
voice_uuid = '<voice_uuid>'
callback_uri = 'https://example.com/callback/resemble-clip'
body = 'This is an async test'
  
response = Resemble.v2.clips.create_async(
  project_uuid,
  voice_uuid,
  callback_uri,
  body,
  title=None,
  sample_rate=None,
  output_format=None,
  precision=None,
  include_timestamps=None,
  is_public=None,
  is_archived=None
)
clip = response['item']

