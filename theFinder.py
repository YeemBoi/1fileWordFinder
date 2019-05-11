"""
Hello!
I was very determined to use only one file, so the readme is inside of the code now.

This program is basically a super simple Python script for finding all the English words that can be spelled with certain letters.
For example, you can type in "hello" and it will output words like hole, hell, he, oh, etc.
It uses mielestronk.com's Corncob list of English words as it's word list for finding words.
To exit the session, enter *quit.
I have a much more user-friendly word finder with a ton of options at yeemboi.pythonanywhere.com if you're interested.
Hope you enjoy!
"""
import urllib.request
print("Loading...")
wordList = str(urllib.request.urlopen("http://www.mieliestronk.com/corncob_lowercase.txt").read())[2 : -5].split("\\r\\n")
print("Ready.")
inputText = input().lower()
while not "*quit" in inputText:
	baseLength = len(inputText)
	for word in wordList:
		if len(word) > baseLength: continue
		success = True
		for char in word:
			if word.count(char) > inputText.count(char):
				success = False
				break
		if success: print(word)
	inputText = input().lower()
