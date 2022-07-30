import pytube
import moviepy.editor as mpe
import os
import ffmpeg

_folder = "Video"
_video = "_video.mp4"
_audio = "_audio.mp4"

urls = ['https://www.youtube.com/watch?v=mFMnsRx6nhk',
       'https://www.youtube.com/watch?v=SQj7Ed-Z9Lk',
       'https://www.youtube.com/watch?v=qExxvF8QS5U',
        'https://www.youtube.com/watch?v=nlnMDttgTbk']

urls = ['https://www.youtube.com/watch?v=2RcuLxhMnDA','https://www.youtube.com/watch?v=nu-acTFiYkI']

def combine_audio(vidname, audname, outname, fps=25):
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

def merge_video_audio(vidname, audname,outname):
	video = ffmpeg.input(vidname).video
	audio = ffmpeg.input(audname).audio
	ffmpeg.output(
		video,
		audio,
		outname,
		vcodec='copy',
		acodec='copy',
	).run()

def download_youtube(url,first,remove,verbose):
	yt = pytube.YouTube(
		url=url,
		use_oauth=True,
		allow_oauth_cache=True
	)

	title =  yt.title.encode("ascii", "ignore").decode().replace("/","_")
	_subVideo = title+_video
	_subAudio = title+_audio

	print("start download:",title)

	stream = yt.streams.filter(only_audio=True, file_extension = "mp4").order_by('abr').desc()
	stream.first().download(_folder,_subAudio)
	# res = "1080p",
	stream = yt.streams.filter(only_video=True, file_extension = "mp4", progressive=True).order_by('resolution').desc()
	# stream = yt.streams.filter(file_extension = "mp4", progressive=True).order_by('resolution').desc()
	if verbose:
		for x in stream: print(x)
	#
	# stream.first().download(_folder,_subVideo)
	# return

	if first: stream.first().download(_folder,_subVideo)
	else: stream.last().download(_folder, _subVideo)

	print("downloaded:",title)
	merge_video_audio(_folder+"/"+_subVideo,_folder+"/"+_subAudio,_folder+"/"+title+".mp4")

	if remove:
		os.remove(_folder+"/"+_subVideo)
		os.remove(_folder+"/"+_subAudio)

	print("finished:",title)

for x in urls:
	download_youtube(x, first = True, remove = True, verbose = True)

print("all finished")