import os
import get_m4s
import medium


def get_media_obj(dir_path, m4s_pattern):
    m4s_set = get_m4s.find_m4s(dir_path, m4s_pattern)
    print("\nm4s_set: " + str(m4s_set))

    m4s_obj = get_obj_by_regex(m4s_set)

    print("\nget_video_dict video: " + str(m4s_obj.video_file))
    print("get_video_dict audio: " + str(m4s_obj.audio_file))

    return m4s_obj


def get_obj_by_regex(m4s_set):
    video_file = ""
    audio_file = ""
    m4s_list = list(m4s_set)

    folder, file = os.path.split(m4s_list[0])
    print("\nFile: " + str(file))

    if file != "video.m4s":
        audio_file = m4s_list[0]
        video_file = m4s_list[1]
    else:
        audio_file = m4s_list[1]
        video_file = m4s_list[0]

    print("\naudio_file: " + str(audio_file))
    print("video_file: " + str(video_file))

    files_obj = medium.Medium(video_file, audio_file)
    return files_obj
