# -*- coding: UTF-8 -*-

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
if "jen" in favorite_languages.keys():
    print ("hello world")
friends=['phil',"tim"]
for name in favorite_languages:
    print("\n"+name.title())
    if name in friends:
        print ("hi "+name.title() + " is " +favorite_languages[name])
for friend in friends:
    if friend in favorite_languages.keys():
        print("thanks " + friend)
    else:
        print ("modify "+ friend)