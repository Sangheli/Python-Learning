import pytube

url = 'https://www.youtube.com/watch?v=CDhQsqqu0ds'

yt = pytube.YouTube(
	url=url,
	use_oauth=True,
	allow_oauth_cache=True
)

yt.streams.order_by('resolution').desc().first().download("Video")