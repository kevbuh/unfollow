# insta_unfollow

Tiny jupyter notebook to see who doesn't follow you (it's a lot easier than you think)

Main function to look for: get_non_followers()
- Near the bottom of the notebook

```python
def get_non_followers(follower_json, following_json):
  """
  Input the your own JSON object into follower_json and following_json.
  Then run the cell to see result of who doesn't follow you back!
  
  Uses two sets and finds the difference between them 
  
  O(N) time-complexity.
  """
  following=set()
  followers=set()

  for thing in following_json['relationships_following']:
    following.add(thing['string_list_data'][0]['value'])
  for thing in follower_json['relationships_followers']:
    followers.add(thing['string_list_data'][0]['value'])
    # print(data['relationships_followers'][0]['string_list_data'][0]['value'])

  return following-followers
````

## How to download your instagram data
Go to you instagram account -> settings -> privacy and security -> download account info
Instagram will then proceed to send you an email with your account's data.

## See who doesn't follow you back
1. Unzip, and then go to ./login_and_account_creation/followers_and_following.
2. Then, go into followers.json and following.json and get the JSON objects from there. 
3. Finally, put your objects into the notebook and run every cell to see who doesn't follow you back.


### Next steps
* Get JSON object automatically
* Clean up notebook
