  
def assemble(json_data):
    avid=json_data['avid'];
    print('\navid: '+str(avid))
    
    title=json_data['title']
    print('title: '+str(title))
    
    page=json_data['page_data']['page']
    print('page: '+str(page))
     
    video_name = str(avid)+ "-" + title+ "-" + str(page)+ ".mp4"
    
    video_name = video_name.replace('【', '')  
    video_name = video_name.replace('】', '')  
    video_name = video_name.replace('《', '')  
    video_name = video_name.replace('》', '')  
    video_name = video_name.replace('|', '')  
    video_name = video_name.replace('｜', '') 
    video_name = video_name.replace('）', '') 
    video_name = video_name.replace('（', '') 
    video_name = video_name.replace('(', '') 
    video_name = video_name.replace(')', '') 
    video_name = video_name.replace('。', '') 
    video_name = video_name.replace('{', '') 
    video_name = video_name.replace('}', '') 
    video_name = video_name.replace('？', '') 
    video_name = video_name.replace('[', '') 
    video_name = video_name.replace(']', '') 
    video_name = video_name.replace(';', '') 
    video_name = video_name.replace('；', '') 
    video_name = video_name.replace('#', '') 
    video_name = video_name.replace('&', '') 
    video_name = video_name.replace('*', '') 
    video_name = video_name.replace('@', '') 
    video_name = video_name.replace('！', '') 
    video_name = video_name.replace('『', '') 
    video_name = video_name.replace('』', '') 
    video_name = video_name.replace('~', '') 
    video_name = video_name.replace('%', '') 
    video_name = video_name.replace('^', '') 
    video_name = video_name.replace('_', '') 
    video_name = video_name.replace('「', '') 
    video_name = video_name.replace('」', '') 
    video_name = video_name.replace('“', '') 
    video_name = video_name.replace('”', '') 
    video_name = video_name.replace(' ', '') 
    video_name = video_name.replace('，', '') 
    video_name = video_name.replace(',', '') 
    print('\nassemble video name: '+video_name)
    
    return video_name