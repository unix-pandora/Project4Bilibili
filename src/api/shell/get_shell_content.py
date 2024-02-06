import get_command
import get_info_by_pattern
import execute_shell

def separate_cmd(source_dir,output_dir):  
  res = get_info_by_pattern.get_info(source_dir)
  new_file_name = res.file_name
  m4s_obj = res.media
  
  cmd_line = get_command.build_command_line(new_file_name,m4s_obj,output_dir)
  return cmd_line

def run_script(dirs_set,output_dir):
  for i in iter(dirs_set):
    command_line = separate_cmd(i,output_dir)
    print('\ncommand_line: '+command_line)
    execute_shell.execute(command_line)