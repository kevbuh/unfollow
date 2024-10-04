import json
import zipfile
import shutil

def parse_following(json_file):
    curr_set = set()
    for user in json_file['relationships_following']:
        curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

def parse_followers(json_file):
    curr_set = set()
    for user in json_file:
        curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

def main():
    # Get zip file path
    zip_file_path = input("Enter your zip path here, e.g instagram-username-date-random.zip -->")

    # Extract zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('./connections')

    # Load JSON data
    following = open(f"connections/connections/followers_and_following/following.json", "r")
    followers = open(f"connections/connections/followers_and_following/followers_1.json", "r")
    following_json = json.load(following)
    followers_json = json.load(followers)
    following_set = parse_following(following_json)
    followers_set = parse_followers(followers_json)

    # Find people who are not following back
    not_following = following_set - followers_set

    # Print results
    print("")
    print("")
    print(f"{len(not_following)} people are not following you back!")
    print("")
    print("")
    print(f"Not Following:")
    print(f"----------------------------------------")

    for i, user_not_following in enumerate(not_following):
        print(f"{i+1}.", user_not_following)
    
    print(f"----------------------------------------")
    print("")
    print("")

    following.close()
    followers.close()
    shutil.rmtree('./connections')

if __name__ == "__main__":
    main()