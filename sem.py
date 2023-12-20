import emoji
def convert_emoji_to_text(user_input):
# Use emoji.demojize to convert emojis to text
text_representation = emoji.demojize(user_input)
return text_representation
def count_emojis(user_input):
# Use emoji.emoji_count to count the number of emojis
emoji_count = emoji.emoji_count(user_input)
return emoji_count
def list_emojis(user_input):
# Use emoji.emoji_list to get a list of emojis
emojis_list = [emoji['emoji'] for emoji in emoji.emoji_list(user_input)]
return emojis_list
def check_specific_emoji(user_input, specific_emoji):
# Check if a specific emoji is present in the input
return specific_emoji in user_input
while True:
# Take user input
user_input = input("Enter a text with emojis (type 'exit' to end): ")
# Check if the user wants to exit
if user_input.lower() == 'exit':
break
# Convert emojis to text
result = convert_emoji_to_text(user_input)
# Count emojis
emoji_count = count_emojis(user_input)
print("Number of emojis:", emoji_count)
# List emojis
emojis_list = list_emojis(user_input)
print("Emojis in the text:", emojis_list)
# Check for specific emojis
specific_emoji = input("Enter a specific emoji to check for: ")
has_specific_emoji = check_specific_emoji(user_input, specific_emoji)
print(f"Does the text contain {specific_emoji}? {has_specific_emoji}")
# Display the result
print("Converted text:", result)
print("\n" + "="*30 + "\n") # Separating each iteration with a line
print("Exiting the program.")