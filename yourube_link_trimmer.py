# Welcome message
print("Hello, I am very useful program. ")
print("I can remove \"music.\" and '&feature=share' from YouTube music links. ")
print("Find a link and follow the next prompt!")

# Taking user input
original_youtube_link = input("Paste your YouTube Music link here: ")

# This string replace function removes "music." from the YouTube link
remove_music = original_youtube_link.replace("music.", "")

# This function removes the final part of the link: "&feature=share"
trimmed_link = remove_music.replace("&feature=share", "")

# printing the trimmed link
print("Here is your trimmed link:")
print(trimmed_link)
