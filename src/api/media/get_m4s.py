import consultation
import matching

def find_m4s(dir_path,m4s_pattern):
  files_sets = consultation.traverse_files(dir_path)
  reciprocate =matching.find_by_pattern(files_sets,m4s_pattern)
  return reciprocate