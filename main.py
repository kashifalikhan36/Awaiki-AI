from ytinfo import YtInfo
from data import SlideData

info=YtInfo()
slidedata=SlideData()

#Generating Slide Data Text 
script=""
caption_timestamp=info.subtitle_info('https://www.youtube.com/watch?v=D56_Cx36oGY')
end_of_length=len(caption_timestamp)
for num in range(0,int(end_of_length)-1):
    script=str(script)+" "+str(caption_timestamp[num]['text'])
    if int(caption_timestamp[num]['start']) == 21:
        break
reply=slidedata.generate_data(script)
with open('C:\\Users\\Kashif\\Documents\\GitHub\\UST_d3code\\data\\slide_output_data.json', 'a') as slide_data:
            slide_data.write(str(reply)+",")  
print(dict(reply)["Heading"])

#Generating Slide Data Image Prompt
image_prompt=slidedata.generate_image_prompt(str(dict(reply)["Heading"]))

#Generating Image
slidedata.generate_image(image_prompt,"1")


# info.channel_info_by_id('https://www.youtube.com/channel/UCL4-nC0SGWbAYk8iX2oJt-g')
# info.channel_info_by_username('https://www.youtube.com/@codeRECODE')