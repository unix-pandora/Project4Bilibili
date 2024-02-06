import os

import get_shell_content
import get_sources_dir
import moving_file
import get_info_by_pattern
import arguments_set as argset


# 处理无声版
def process_silent():
    paths_set = get_sources_dir.get_dirs(argset.origin_directory)

    for i in paths_set:
        info_res = get_info_by_pattern.get_info(i)
        old_video_path = info_res.media.video_file
        new_file_name = info_res.file_name

        print("old_video:", old_video_path)
        print("New_file:", argset.finally_directory + str(os.sep) + new_file_name)
        moving_file.move_m4s(argset.finally_directory, new_file_name, old_video_path)


# 处理有声版
def process_audible():
    paths_set = get_sources_dir.get_dirs(argset.origin_directory)
    get_shell_content.run_script(paths_set, argset.finally_directory)


# process_audible()
# process_silent()
