name = input('Enter your name: ')
gender= input('Enter your gender: ').lower()
adjective = input('adjective: ')
color= input('What is your best color: ').upper()
hobby= input('What are your hobbies: ').upper()
dreams = input('What is your dream Job: ').upper()
mood = input('Mood right now?: ')
#all = name,gender,adjective,color,hobby,dreams,mood

if gender == "male" :
    sentence = f'hello {adjective} {name}, how are you doing today?, oh! you are feeling {mood} \
that is okay, color {color} is cool. being a/an {dreams} is a good thing never give up on your dreams \
and i can see you like {hobby}, you are quite interesting!'
elif gender == 'female':
    sentence = f'hello {adjective} {name}, how are you doing today?, oh! you are feeling {mood} \
that is okay, color {color} is cool. being a/an {dreams} is a good thing never give up on your dreams \
and i can see you like {hobby}, you are quite interesting!'
else:
    sentence = f'hello to this wonderful being, how are you doing today? \
I can see you dont feel like talking about anything, go take a nap or talk to your love ones'
print(sentence)





