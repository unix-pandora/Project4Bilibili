import re  
  
def find_by_pattern(sets, pattern):  
    items_set = set() 
    for item in sets:  
        if re.search(pattern, item):  
            items_set.add(item)    
    logging(items_set)        
    return items_set  
  
  
def logging(results):        
    if results is not None:  
      print('\nmatching_logging: '+str(results))
    else:  
      print('Not found')