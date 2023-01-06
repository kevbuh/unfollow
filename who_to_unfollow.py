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

  # make list of people following
  for thing in following_json['relationships_following']:
    following.add(thing['string_list_data'][0]['value'])
    
  # list of people who follow you back
  for thing in follower_json['relationships_followers']:
    followers.add(thing['string_list_data'][0]['value'])

  return following-followers # set of people who don't follow you back
````
