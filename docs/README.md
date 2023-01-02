# `rarity.json` file structure
- This is a very important file, where you will define the probabilities of each NFT.
  If you would like to change the probabilities and etc. you will need to change this file.
- The structure of this file is very simple, you will have a list of dictionaries, 
  where each dictionary will have the following structure:
```json
  {
  "Background": {
    "Light Brown": 100,
    "Cyan": 200,
    "Dark Brown": 300,
    "Deep Purple": 350,
    "Emerald": 50
  },
  "Skin": {
    "Golden": 50,
    "White": 500,
    "Red": 150,
    "Standard": 250,
    "Dark": 50
  },
  ...
  "Expression": {
    "Reckless": 100,
    "Crazy": 50,
    "Angry": 200,
    "Shocked": 350,
    "Sad": 300
  }
}
```
- The keys of the dictionary will be the trait categories, and the values will be 
  dictionaries, where the keys will be the trait names and the values will be the 
  probabilities of each trait. The higher the values the higher the probability of 
  that trait to be generated. These are not exact number of traits to be generated, 
  but the final number of outputs will be very close to the probabilities.
- It is not a must that the sum of the probabilities of each trait category is equal 
  to the number of total number of NFTs, but it is recommended to keep it that way 
  for better understanding and readability.
- The folder names in the `app/images` folder should be the same as the trait category 
  names in the `rarity.json` file. For example, if you have a trait category named as 
  `Background` or `Skin` etc. in `rarity.json`, you should have a `Background`, `Skin` 
  folders in the `app/images` folder accordingly.
```diff
+ "Background": {
    "Light Brown": 100,
    "Cyan": 200,
    "Dark Brown": 300,
    "Deep Purple": 350,
    "Emerald": 50
  }
```
- The images in the folders should be named the same as the trait names in the 
  `rarity.json` file. For example, if you have a trait named as `Golden` in the 
  `rarity.json` file, you should have a `Golden.png` image in the trait folders. Any 
  name mismatch will cause the script to fail.
```diff
+ "Golden": 50
...
+ "White": 500,
+ "Dark": 50
```
