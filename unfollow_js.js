const fs = require('fs');
const path = require('path');
const unzipper = require('unzipper');

const zipFilePath = 'file_name.zip'; // ===========  put your zip file name here !!!!!!!!!!!!!!!!!!!! =================================
const extractPath = './data';

fs.createReadStream(zipFilePath)
  .pipe(unzipper.Extract({ path: extractPath }))
  .on('close', () => {
    const followingFilePath = path.join(extractPath, 'followers_and_following', 'following.json');
    const followersFilePath = path.join(extractPath, 'followers_and_following', 'followers_1.json');
    const followingData = fs.readFileSync(followingFilePath, 'utf8');
    const followersData = fs.readFileSync(followersFilePath, 'utf8');
    const followingJson = JSON.parse(followingData);
    const followersJson = JSON.parse(followersData);

    function parseFollowing(jsonFile) {
      const currSet = new Set();
      for (const user of jsonFile.relationships_following) {
        currSet.add(user.string_list_data[0].value);
      }
      return currSet;
    }

    function parseFollowers(jsonFile) {
      const currSet = new Set();
      for (const user of jsonFile) {
        currSet.add(user.string_list_data[0].value);
      }
      return currSet;
    }

    const followingSet = parseFollowing(followingJson);
    const followersSet = parseFollowers(followersJson);

    const notFollowing = new Set([...followingSet].filter(x => !followersSet.has(x)));

    console.log('\n\n' + notFollowing.size + ' people are not following you back!\n\n');
    console.log('Not Following:');
    console.log('----------------------------------------');

    let i = 1;
    for (const userNotFollowing of notFollowing) {
      console.log(i + '.', userNotFollowing);
      i++;
    }

    console.log('\n\n');
  });
