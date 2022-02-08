print("CREATED BY G-ONE")
import os
c=1
while True :
    os.system('espeak -a 150 -s 140 -p 65 -g 11  "Enter Password" -ven+f4')
    pw=input(f'[{c}] Enter Password: ')
    print()
    if pw == 'hacker':
        os.system('espeak -a 150 -s 140 -p 65 -g 11  "Access Granted" -ven+f4')
        print('Access Granted')
        break
    c+=1
    if c == 500000 :
        print('you have reached the max number of attempts !!')
        break
    os.system('espeak -a 150 -s 140 -p 65 -g 11  "Access Denied" -ven+f4')
    print (f'Access Denied!')

import random
dic={'a':['Ambitious','Audacious','Adorable','Angry'],'b':['Brave','Brilliant','Boring','Busy'],'c':['Compassionate','Caring','clever'],'d':['Driven','Daring','Dedicated','Dreamer'],'e':['Encouraging','Enchanting','Energetic','Efficient'],'f':['Fearless','Fair','Flexible','Friendly'],'g':['Generous','Gentle','Graceful','Greedy'],'h':['Honest','Helpful','Honorable','Heroic'],'i':['Inspirational','Independent','Industrious','Intelligent'],'j':['Just'],'k':['Kind','Knowedgeable'],'l':['Loyal','Lazy','Loving'],'m':['Magnanimous','Mature','Mean','Moody'],'n':['Nobel','Naughty','Neat'],'o':['Optimistic','Obidient','Outspoken'],'p':['Perseverent','Patient','Perfect','Polite'],'q':['Quiet'],'r':['Resilient','Responsible','Rude','Respectful'],'s':['Stalwart','Sensitive','Studious','Smart','Sweet'],'t':['Talented','Talkative','Trustworthy'],'u':['Undaunted','Understanding'],'v':['Visionary','Valuable'],'w':['Wise'],'x':['Xfactor'],'y':['Youthful'],'z':['Zealous'],' ':' '}
strg=""
name=input("Enter your name:\n")
nm=name.lower()
for i in nm:
    strg=strg+i.upper()+":"+random.choice(dic[i])+" "+"\n"
print(strg)
    
