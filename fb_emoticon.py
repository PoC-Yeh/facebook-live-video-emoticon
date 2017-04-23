import facebook
import time
import progressbar


def get_emoji(token, id_num, second_count):
    emoji_time = {}
    graph = facebook.GraphAPI(access_token = token, version = 2.7)
    post = graph.get_object(id='{}?fields=video_insights'.format(id_num))
    emoji_value = post['video_insights']['data'][-1]['values'][0]['value']
    emoji_time[second_count] = emoji_value
    emoji_list.append(emoji_time)


def get_video_status(id_num):
    graph = facebook.GraphAPI(access_token = token, version = 2.7)
    post = graph.get_object(id='{}?fields=live_status'.format(id_num))
    live_status = post['live_status']
    return(live_status)


bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
token = "123456789"  #your token
id_num = "123456789" #your video id
emoji_list = []
count = 1
second_count = 1


while True:
    get_emoji(token, id_num, second_count)
    get_video_status(id_num)
    if get_video_status(id_num) != "LIVE":   #break the loop when your video isn't "live-video" anymore
        break
    bar.update(second_count)
    second_count += 1
    time.sleep(1)    
    
    
for value in emoji_list:
    print(value)    
