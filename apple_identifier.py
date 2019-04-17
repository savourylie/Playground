def apple_identifier(x):
    # 是不是紅色
    if (x.color == 'red') and \
       # 是不是圓的
       (x.shape == 'round') and  \
       # 有沒有葉子
       (x.has_leaf == True) and \
       # 葉子是不是綠的
       (x.leaf_color == 'green'):
    
        return True
        
    else: 
        return False

