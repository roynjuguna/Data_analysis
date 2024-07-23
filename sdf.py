def stutter(word):
	word = input("Enter the word you want stuttered: ")
	print (word[:2] + "... " + word[:2] + "... " + word + "?" )
	
stutter("man")