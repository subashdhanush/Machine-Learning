import emoji

def emoji_to_text(input_string):
    return emoji.demojize(input_string)

# Test the function
input_string = "I love Python! 😍🐍"
converted_text = emoji_to_text(input_string)

print("Original:", input_string)
print("Converted:", converted_text)
