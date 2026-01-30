# we could run this via...

# this will execute the script without enter in shell
# pipenv run python .\emoji_example.py

# this will force us to enter to shell first
# pipenv shell
# python  .\emoji_example.py

import emoji

print(emoji.emojize("Python is :fire: :snake:"))