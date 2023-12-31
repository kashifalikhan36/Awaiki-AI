from ytinfo import YtInfo
from data import SlideData
from ebook import Ebook
from audiobook import AudioBook

info=YtInfo()

ebook=Ebook()
audioBook=AudioBook()

#Generating Content
def generate_content(script,num):
    reply=slidedata.generate_data(script)  
    print(reply)
    #Generating Slide Data Image Prompt
    image_prompt=slidedata.generate_image_prompt(str(dict(reply)["Heading"]))

    #Generating Image
    slidedata.generate_image(image_prompt,str(num))

    #Genetraing ebook
    pdf_path = "./ebook_and_audiobook/input.pdf"
    heading = str(dict(reply)["Heading"])
    paragraph=str(dict(reply)["paragraph"])
    image_path = f"./data/image_{num}.jpg"
    if int(num)==0:
        make_content(pdf_path, heading, image_path, paragraph)
    else:
        add_content(pdf_path, pdf_path, heading, image_path, paragraph)
    
    return reply

#This will make first page of pdf with content
def make_content(output_path, heading, image_path, paragraph):
    ebook.create_pdf(output_path, heading, image_path, paragraph)

# this will add further contents
def add_content(input_pdf_path, output_pdf_path, heading, image_path, paragraph):
    ebook.append_pdf(input_pdf_path, output_pdf_path, heading, image_path, paragraph)

def analyze_and_convert(video_link,API_KEY):
    global slidedata
    slidedata=SlideData(API_KEY)
    #Ebook Generator
    audio_story=""
    script=""
    num=0
    caption_timestamp=info.subtitle_info(video_link)
    end_of_length=len(caption_timestamp)
    print(int(caption_timestamp[2]['start']))
    for i in range(0,int(end_of_length)-1):
        script=str(script)+" "+str(caption_timestamp[num]['text'])
        print(script)
        if int(caption_timestamp[num]['start']) % 21 == 0:
            story=generate_content(script,num)
            audio_story+=str(dict(story)["paragraph"])+"\n"
            script=""
            
        num+=1

    #Audiobook Generator
    desired_text = slidedata.generate_audiobook(audio_story)
    audioBook.text_to_speech(desired_text)



#Get Youtube Channel Info
# info.channel_info_by_id('https://www.youtube.com/channel/UCL4-nC0SGWbAYk8iX2oJt-g')
# info.channel_info_by_username('https://www.youtube.com/@codeRECODE')
