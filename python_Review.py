def create_youtube_video(title, description):
	youtubevideo = {"Title": title, "Description": description, "Dislikes": 0, "Comments": {}, "Likes":0}
	return youtubevideo 

def like(youtubevideo):
	if "Likes" in youtubevideo:
		youtubevideo["Likes"]+=1
	return youtubevideo

def dislike(youtubevideo):
	if "Dislikes" in youtubevideo:
		youtubevideo["Dislikes"]+=1
	return youtubevideo

def add_comment(youtube_vid, username, comment_text):
		youtube_vid["Comments"][username]=comment_text
		return youtube_vid

video= create_youtube_video("hi", "hello")
add_comment(video, "Sama", "Soooooooooo awesome!!!")



for i in range(495):
	like(video)
	dislike(video)

print(video)



