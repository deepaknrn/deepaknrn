import random

word_list= ['abruptly', 'absurd', 'abyss', 'affix', 
'askew', 'avenue', 'awkward', 'axiom', 
'azure', 'bagpipes', 'bandwagon', 
'banjo', 'bayou', 'beekeeper', 
'bikini', 'blitz', 'blizzard', 'boggle', 
'bookworm', 'boxcar', 'boxful', 'buckaroo', 
'buffalo', 'buffoon', 'buxom', 'buzzard', 
'buzzing', 'buzzwords', 'caliph', 'cobweb', 
'cockiness', 'croquet', 'crypt', 'curacao', 
'cycle', 'daiquiri', 'dirndl', 'disavow', 
'dizzying', 'duplex', 'dwarves', 'embezzle', 
'equip', 'espionage', 'euouae', 'exodus', 
'faking', 'fishhook', 'fixable', 'fjord', 
'flapjack', 'flopping', 'fluffiness', 'flyby', 
'foxglove', 'frazzled', 'frizzled', 'fuchsia', 
'funny', 'gabby', 'galaxy', 'galvanize', 
'gazebo', 'giaour', 'gizmo', 'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                

print('''| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

#word_list = ["aardvark", "baboon", "camel"]

word_choice=random.choice(word_list)
word_choice_len=len(word_choice)
word_choice_list=[]
word_choice_blanks_list=[]

for i in range(0,word_choice_len,1):
  word_choice_list.append(word_choice[i])

for i in range(0,word_choice_len,1):
  word_choice_blanks_list.append('_')

winning_answer_list=word_choice_list
#print(word_choice_list)
print(word_choice_blanks_list)
j=0
lives=7

while word_choice_list!=word_choice_blanks_list:
  print("\n Guess a letter : ")
  letter=input("")

  j=0

  if letter not in word_choice_list:
    lives=lives-1
    print(stages[lives])
    if lives==0:
      print("You Loose!")
      word_choice_list=word_choice_blanks_list 
      print(winning_answer_list)
      
  for letter1 in word_choice_list:
   if letter==letter1:
     index_pos=(word_choice_list.index(letter,j))+1
     j=index_pos #loop through if the word is appearing twice
     word_choice_blanks_list[index_pos-1]=letter
     print(word_choice_blanks_list)
     if word_choice_list==word_choice_blanks_list:
       print("Congratulations, You have Won")
   
