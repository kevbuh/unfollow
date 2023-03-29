import json
import zipfile

# put your zip file name here 
# for example: dir_name = 'kevinbuhlerr_20230215.zip'
zip_file_path = 'kevinbuhlerr_20230328.zip'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('data')

following = open("./data/followers_and_following/following.json","r")
followers = open("./data/followers_and_following/followers_1.json","r")

following_json = json.load(following)
followers_json = json.load(followers)

def parse_following(json_file):
    curr_set = set()
    for user in json_file['relationships_following']:
      curr_set.add(user['string_list_data'][0]['value'])
      # pass
      # print(user['string_list_data'][0]['value'])
    return curr_set

def parse_followers(json_file):
    json_file = json_file
    curr_set = set()
    for user in json_file:
      # print
      # print(user['string_list_data'][0])
      curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

following_set = parse_following(following_json)
followers_set = parse_followers(followers_json)

not_following = following_set - followers_set

print("")
print("")
print(f"{len(not_following)} people are not following you back!")
print("")
print("")

print(f"Not Following:")
print(f"----------------------------------------")


for i,user_not_following in enumerate(not_following):
  print(f"{i+1}.", user_not_following)

print("")
print("")
