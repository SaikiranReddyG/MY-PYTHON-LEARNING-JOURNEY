my_dict = {'age' : '27', 'job' : 'youtuber', 'my_key' : 'like,share,subscribe,comment'}
if 'my_ke' in my_dict.keys():
   for k,v in my_dict.items():
       if k == 'my_ke':
           print('sucess: k = {}, v = {}'.format(k,v))
           break
else : print('error')