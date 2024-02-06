import os


# 有声版
def build_command_line(new_name, m4s_files, output_path):
    video_name = m4s_files.video_file
    audio_name = m4s_files.audio_file
    separator = os.sep

    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
    command_line = [
        "ffmpeg -i ",
        str(video_name),
        " -i ",
        str(audio_name),
        " -c:v copy -c:a aac -strict experimental ",
        output_path,
        str(separator),
        str(new_name),
    ]

    command_line = "".join(command_line)
    print("\n", "build_commmand_line: ", command_line)

    return command_line
