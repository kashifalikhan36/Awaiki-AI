from ytinfo import YtInfo

info=YtInfo()
info.subtitle_info('https://www.youtube.com/watch?v=eMOA1pPVUc4','txt')
info.subtitle_info('https://www.youtube.com/watch?v=eMOA1pPVUc4','json')
info.channel_info_by_id('https://www.youtube.com/channel/UCL4-nC0SGWbAYk8iX2oJt-g')
info.channel_info_by_username('https://www.youtube.com/@codeRECODE')