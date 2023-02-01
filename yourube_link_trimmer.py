# Welcome message
print("Hello, I am very useful program. ")
print("I can remove \"music.\" and '&feature=share' from YouTube music links. ")
print("Find a link and follow the next prompt!")

function_dictionary = {
  "remove_music": lambda x: x.replace("music.", ""),
  "trim_link": lambda x: x.replace("&feature=share", "")
}

# Taking user input
original_youtube_link = input("Paste your YouTube Music link here: ")

# This string replace function removes "music." from the YouTube link
removed_music = function_dictionary["remove_music"](original_youtube_link)
# it does the same thing as:
# remove_music = original_youtube_link.replace("music.", "")

# This function removes the final part of the link: "&feature=share"
trimmed_link = function_dictionary["trim_link"](removed_music)
# same functionality as:
# trimmed_link = remove_music.replace("&feature=share", "")

# printing the trimmed link
print("Here is your trimmed link:")
print(trimmed_link)
