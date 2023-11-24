import get_new_name
import get_m4s_obj
import information

def get_info(source_dir):
  json_pattern = r'.*entry.*.*json.*'  
  m4s_pattern = r'.*.m4s.*'  
  
  new_file_name = get_new_name.build_new_name(source_dir,json_pattern)
  m4s_object = get_m4s_obj.get_media_obj(source_dir,m4s_pattern)
  
  res_data = information.Infor(new_file_name,m4s_object)
  return res_data