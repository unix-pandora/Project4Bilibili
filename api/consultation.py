import os    
  
def traverse_files(path):  
    # 初始化一个空集合  
    file_set = set()  
    # 遍历指定路径下的全部文件（包括文件夹）  
    for root, dirs, files in os.walk(path):  
        for name in files:  
            file_set.add(os.path.join(root, name))  
        for name in dirs:  
            file_set.add(os.path.join(root, name))  
                
    return file_set  
  
 
