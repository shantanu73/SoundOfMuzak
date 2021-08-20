import moviepy.editor as mpy
import os, random


pwd = os.getcwd()

load = "input"
save = "output"
mp4 = ".mp4"
vcodec = "libx264"
videoquality = "24"
compression = "slow"
vid_folder = pwd + "\\videos\\"
load_vid = vid_folder + load + mp4
save_vid = vid_folder + save + mp4
time_cut = vid_folder + "time_cuts.txt"
HelloPro = "hbh"

# cuts = [('00:00:00.00', '00:00:02.00'), ('00:01:06.00', '00:01:08.00'), ('00:00:30.00', '00:00:32.00')]


def create_cuts():
    cuts_list = []

    with open(time_cut) as f:
        times_list = f.readlines()

        for times in times_list:
            cuts = times.split("-")
            cuts[1] = cuts[1][:-1]
            cuts_list.append(cuts)

    return cuts_list


def edit_video(input_vid, output, vid_cuts):
    video = mpy.VideoFileClip(input_vid)

    clips = []

    for cut in vid_cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)

    final_clip = mpy.concatenate_videoclips(clips)
    final_clip.write_videofile(output, threads=4, fps=24, codec=vcodec, ffmpeg_params=["-crf", videoquality])

    video.close()


created_cuts = create_cuts()
random.shuffle(created_cuts)
edit_video(load_vid, save_vid, created_cuts)
