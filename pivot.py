import os
import sys
sys.path.append('./api')
sys.path.append('./api/media')
sys.path.append('./api/shell')
sys.path.append('./api/entity')

import get_shell_content
import get_sources_dir
import moving_file
import get_info_by_pattern

input_path = "F:\\Label\\folder\\download"
output_dir = "F:\\Label\\folder"

# 处理无声版
def process_silent():
  paths_set =get_sources_dir.get_dirs(input_path)
  
  for i in paths_set:
    info_res = get_info_by_pattern.get_info(i)
    old_video_path=info_res.media.video_file
    new_file_name=info_res.file_name
  
    print('\nold_video_path: '+old_video_path)
    print('New_file_path: '+output_dir+str(os.sep)+new_file_name)
    moving_file.move_m4s(output_dir,new_file_name,old_video_path)

# process_silent()

# 处理有声版
def process_audible():
  paths_set =get_sources_dir.get_dirs(input_path)
  get_shell_content.run_script(paths_set,output_dir)
    
process_audible()  
