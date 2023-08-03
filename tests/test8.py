# import re

# string_data = '''{"Heading":"Hey Everyone! In Today's Video, We Are...",
# "paragraph":"going to talk about the latest trends in fashion. Fashion is constantly evolving, and it's important to stay up-to-date with the latest styles and designs. In this video, we will be discussing some of the hottest fashion trends for this season.

# First, let's talk about colors. Pastels are making a comeback this year, with soft pinks, lilacs, and mints being the go-to shades. These light and airy colors are perfect for the warmer months and can be incorporated into your wardrobe through tops, dresses, and accessories.

# Next, let's discuss patterns. Animal prints are still going strong, particularly leopard and snake prints. These bold and eye-catching patterns can be worn in the form of skirts, shirts, or even shoes to add a touch of fierceness to your outfit.

# When it comes to clothing styles, oversized blazers are a must-have item. This versatile piece can be worn with jeans for a casual look or paired with a dress for a more formal occasion. The oversized fit adds a trendy and relaxed vibe to any outfit.

# Accessories also play a big role in completing a fashion-forward look. Statement earrings are making a huge comeback, with bold and colorful designs stealing the spotlight. These earrings can instantly elevate any outfit and add a pop of personality.

# Lastly, let's not forget about footwear. Chunky sneakers are still in style, and they are perfect for adding a sporty touch to your outfits. Whether you pair them with jeans or a dress, chunky sneakers are comfortable and stylish.

# So that's it for today's video. I hope you enjoyed learning about the latest fashion trends. Make sure to like this video, subscribe to our channel, and leave a comment below letting us know your favorite trend. See you in the next video!"}'''

# split_data = string_data.split('",\n')
# heading = split_data[0][12:]
# index = split_data[1].find('"paragraph":')
# paragraph = split_data[1][index + 13:-3]
# formatted_data = {"Heading": heading, "paragraph": paragraph}
# print(formatted_data)
# paragraph = split_data[1][13:-2]

# # Create the desired dictionary format
# formatted_data = {"Heading": heading, "paragraph": paragraph}
# print(formatted_data)
# with open("./txxt.txt","w") as file:
#     file.write(formatted_data)
# # Use regular expressions to find "Heading" and "paragraph" values
# heading_match = re.search(r'"Heading":"(.*?)",', string_data)
# paragraph_match = re.search(r'"paragraph":"(.*?)"}', string_data)

# if heading_match and paragraph_match:
#     heading = heading_match.group(1)
#     paragraph = paragraph_match.group(1)

#     # Create the desired dictionary format
#     formatted_data = {"Heading": heading, "paragraph": paragraph}
#     print(formatted_data)
# else:
#     print("Data format error: Heading and/or paragraph not found.")