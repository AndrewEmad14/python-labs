import webbrowser
import random

list = [
  "https://kitten.academy/",
  "https://en.wikipedia.org/wiki/World_War_III",
  "https://store.steampowered.com/",
  "https://colorhunt.co/",
  "https://google.com/",
  "https://github.com/",
  "https://chatgpt.com/",
  "https://roadmap.sh/"
]
lucky = random.choice(list)
webbrowser.open(lucky)

