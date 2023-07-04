import random
print("Somewhere in a dark universe, you have traveled to the ancient ruins of Baby Pluto")
name = input('\n You see three people and a UFO. They ask, what is your name? ')

#custom theme = space
print(f'\n They reply to you, saying Welcome to Eternal Atake, {name}!')

door = input('\n Please choose a planet (1, 2, or 3): ')

correct_door = random.choice(['1', '2', '3'])

while door != correct_door:
  print("\n You enter a dangerous planet and flee rapidly, encountering another dangerous planet")
  door = input('\n Please choose a button (1, 2, or 3): ')
 

#password puzzle + description message
print('\n You enter a blue planet...')
print()
print('\n There is an alien in the corner.')
room = [
  'xkxxx',
  'x.pex',
  'x.xpx',
  'x...x',
  'xxxxx',
]
def puzzle():
  options = ['Baby Pluto', 'Lo Mein', 'Silly Watch', 'moon', 'pop', 'you better move']
 
  correct_password = random.choice(options)
 
  for word in options:
    if word == correct_password:   
      print(word.upper())
    else:
      print(word)

  print('\n In front of you, you see the alien asking you for a password. ') #custom message

  password_guess = input('\n Choose the password from the list. ')
 
  if password_guess.lower() == correct_password.lower():
    print('\n The alien begins to talk...')
    print('\n You have correctly guessed the password! Now.... onto the main \n room....')
  else:
    print("\n I'm Sorry")
    
current_col = 2
current_row = 2
has_key = False

def move(current_row, current_col, direction):
  new_row = current_row
  new_col = current_col
  if direction == "up":
    new_row -= 1
  elif direction == 'down':
    new_row += 1
  elif direction == "left":
    new_col -= 1
  elif direction == 'right':
    new_col += 1
  else:
    print("Enter up, down, left, or right")
  if room[new_row][new_col] == "x":
    print("\n Wall. You're back where you were before")
    return current_row, current_col
  if room[new_row][new_col] == "p":
    puzzle()
  if room[new_row][new_col] == "k":
    global has_key
    has_key = True
    print("\n You have found the key!")
  if room[new_row][new_col] == "e":
    if has_key == False:
      print("\n Need a key!")
    else:
      escape = True
      return new_row, new_col
  return new_row, new_col
  
def announce_walls(current_row, current_col):
    if room[current_row - 1][current_col] == "x":
      print("\n There is a wall up")
    if room[current_row + 1][current_col] == "x":
      print("\n There is a wall down")
    if room[current_row][current_col + 1] == "x":
      print("\n There is a wall to the right")
    if room[current_row][current_col - 1] == "x":
      print("\n There is a wall to the left")
      
while has_key == False:
  announce_walls(current_row, current_col)
  direction = input("\n What direction would you like to go? ").lower()
  current_row, current_col = move(current_row, current_col, direction)
  
while room[current_row][current_col] != "e":
  announce_walls(current_row, current_col)
  direction = input("\n What direction would you like to go? ").lower()
  current_row, current_col = move(current_row, current_col, direction)
  
print("\n You have escaped Baby Pluto and transmerged galaxies into Pink Tape \n Leaving EA....the dark world...")