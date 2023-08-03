import openai
import requests
from PIL import Image
from io import BytesIO
import json

class SlideData:
    
    def __init__(self):
        self.audiotext=""
        openai.api_key = "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"
        self.messages = [{"role": "system", "content": 'Ignore all the instructions you got before. From now on, you are going to act as Youtube Timestamp generator. I would like you to simulate Yotube Timestamp generator. To do this, when I tell you something, you are always going to generate response with one heading title and paragraph without any new line and dont forget u only give python dictionary form. For example:{"Heading":"This is a heading of my prompt","paragraph":"This is a paragraph related to the given prompt with only 100-150 words only and pretend like that we r writing blog in simple word "}'}]
        self.image_messages=[{"role": "system", "content": 'Ignore all the instructions you got before. From now on, you are going to act as Image Prompt generator. I would like you to simulate Image Prompt generator. To do this, when I tell you something, you are always going to generate response which is helpful for us to use as a prompt in DellE image generator and make sure response looks like python dictionary.. For example:{"{"prompt":"An expressive oil painting of a basketball player dunking, depicted as an explosion of a nebula"}'}]
        self.audiotext_messages = [{"role": "system", "content": 'Ignore all the instructions you got before. From now on, you are going to act as Storyteller. I would like you to simulate Image Storyteller. Storyteller can able explain anything in a way of story which seems like interesting whenever we are listing or reading. To do this, when I tell you something, you are always going to generate response with as much as words u can add to make story simple and easy to understand and make sure response looks like python dictionary.. For example:- "Once upon a time, in a small village nestled between lush hills, there lived a curious young girl named Lily. Every day, she would wander into the enchanted forest nearby, where whispers of magical creatures echoed through the trees. One sunny morning, while following a mystical glow, she stumbled upon a friendly, talking squirrel named Nutmeg. He led her to a hidden glade where fairies danced and granted wishes. Excitement filled her heart, and she asked for the ability to understand animals. From that day on, Lily and Nutmeg became inseparable, embarking on thrilling adventures and helping creatures in need. The village praised her as a kind and wise protector of nature, and Lily s world was forever enchanted with love and wonder."'}]

    def generate_data(self, user_message):
        self.messages.append(
            {"role": "user", "content": user_message},
        )

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", messages=self.messages
        )

        reply = chat.choices[0].message.content

        self.messages.append({"role": "assistant", "content": reply})

        with open('./data/slide_input_data.json', 'a') as slide_data:
            slide_data.write(str(reply)+",")
        
        try:
            #Convert the text format into a Python dictionary
            formatted_data = json.loads(reply)
        except:
            #Clean Data
            split_data = reply.split('",\n')
            try:
                index = split_data[0].find('"paragraph":')
                heading = split_data[0][12: index]
                paragraph = split_data[0][index + 13:-3].replace('\ \n \n\n \\n \\n\\n \\n8 \\n\\n1 \\n\\n2 \\n\\n3 \\n\\n4 \\n\\n5 \\n\\n6 \\n\\n7 \\n\\n8 \\n\\n9', '').replace('\'s',"'s")
                formatted_data = {"Heading": heading, "paragraph": paragraph}
                print(formatted_data)
            except:
                index = split_data[0].find('"paragraph":')
                heading = split_data[0][12: index]
                paragraph = split_data[1][index + 13:-3].replace('\ \n \n\n \\n \\n\\n \\n8 \\n\\n1 \\n\\n2 \\n\\n3 \\n\\n4 \\n\\n5 \\n\\n6 \\n\\n7 \\n\\n8 \\n\\n9', '').replace('\'s',"'s")
                formatted_data = {"Heading": heading, "paragraph": paragraph}
                print(formatted_data)
        
        

        self.messages = [{"role": "system", "content": 'Ignore all the instructions you got before. From now on, you are going to act as Youtube Timestamp generator. I would like you to simulate Yotube Timestamp generator. To do this, when I tell you something, you are always going to generate response with one heading title and paragraph in a python dictionary form. For example:{"Heading":"This is a heading of my prompt","paragraph":"This is a paragraph related to the given prompt with only 100 words and pretend like that we r writing blog in simple word "}'}]
        return formatted_data
    
    def generate_image_prompt(self,discription_image):
        self.image_messages.append(
            {"role": "user", "content": discription_image},
        )

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.image_messages
        )

        prompt = chat.choices[0].message.content

        self.messages.append({"role": "assistant", "content": prompt})

        with open('./data/slide_input_image.txt', 'a') as slide_data:
            slide_data.write(str(prompt)+"\n")
        return prompt

    def generate_image(self,prompt,num):
    
        def save_image_from_url(image_url, num):
            response = requests.get(image_url)
            if response.status_code == 200:
                image_content = BytesIO(response.content)
                image = Image.open(image_content)
                image.save(f"./data/image_{num}.jpg")
            else:
                print("Failed to download the image. Check the URL or try again later.")

        response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
        )
        image_url = response['data'][0]['url']
        save_image_from_url(image_url,num)

    def generate_audiobook(self, audioprompt):
        
        self.audiotext_messages.append(
            {"role": "user", "content": audioprompt},
        )

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", messages=self.audiotext_messages
        )

        reply = chat.choices[0].message.content

        self.audiotext_messages.append({"role": "assistant", "content": reply})

        with open('./data/audiotext_input_data.json', 'a') as slide_data:
            slide_data.write("{'story': '''"+str(reply)+"'''} \n ,")
        
        # # Convert the text format into a Python dictionary
        # reply_dict = json.loads(reply)

        return reply