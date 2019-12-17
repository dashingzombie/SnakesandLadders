import random

position=[0,0]

names=[]

def players():
  for i in range(0,2):
    print('player', i+1, 'input your name')
    name=input("\n")
    print('welcome',name)
    names.append(name)
  print('\nplayers:')
  for i in names:
    print(i)

  print('\n')

player_place={}

def diceroll():
  d1=(random.randint(1,6))
  return d1

snakes={16:8,45:21,58:40,70:5,85:50,92:4,96:41,99:31}
ladders={5:9,11:25,25:40,32:50,45:32,57:30,66:15,75:16}

def assign():
  for i in names:
    x=names.index(i)
    player_place[i]=position[x]
print('Press enter to roll a dices')
def move():
  q=0 #flag
  while q<1:
    for i in names:
      e=diceroll()
      g=position[names.index(i)]
      input()
      print('\n')
      print(i ,'is  on', g)
      input()
      print(i, 'got a', e)
      p=e+g
      position[names.index(i)]=p
      print(i, 'is on ',p)

      if position[names.index(i)]>100:
        q+=2
        print(i,'wins')
      elif position[names.index(i)]==100:
        q+=2
        print(i,'wins')
      if q>1:
        break

      for a in snakes:
        if a == position[names.index(i)]:
          print('Damn , you hit a snake')
          print('you go down', snakes[a], 'places')
          position[names.index(i)]-=snakes[a]
          print('you are currently on', position[names.index(i)])
      for a in ladders:
        if a ==position[names.index(i)]:
          print("Cool , you got a ladder")
          print('you go up', ladders[a], 'places')
          position[names.index(i)]+=ladders[a]
          print('you are currently on', position[names.index(i)])


players()
assign()
move()
