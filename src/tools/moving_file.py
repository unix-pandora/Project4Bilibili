import shutil  

def move_m4s(output_dir,new_file_name,old_file_path):
  # 计算新文件的完整路径  
  new_file_path = shutil.os.path.join(output_dir, new_file_name)  
  
  # 使用shutil.move来移动文件  
  shutil.move(old_file_path, new_file_path)
