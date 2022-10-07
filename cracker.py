from urllib.request import urlopen
import hashlib

def getlist(url): # Takes a URL and splits it line by line into a variable array.
	list = urlopen(url).read().decode("UTF-8") # Takes all data from site in UTF-8 format and stores it in list.
	ind_lines = list.split() # Takes list variable and splits the data from individual lines into a ind_lines[] variable.
	return ind_lines # Returns this newly made variable.

def hash(password): # Takes a password and then encodes it into a md5 hexadecimal hash.
	passwordhash = hashlib.md5(password.encode()) # Encodes the password into md5.
	passhexhash = passwordhash.hexdigest() # Takes md5 and writes it as hexadecimal.
	return passhexhash # Returns this password hash in hexadecimal.

def bruteforce(list, passwordhash): # Bruteforces based off of a list of passwords in an array and a hexadecimal hash.
	for guess in list: # Takes each password from the password array and then...
		guesshash = hash(guess) # ...Hashes it and returns a password hash in hexadecimal
		if guesshash == passwordhash: # Checks the password hashes against eachother.
			print(f"Hey! your password is: {guess}") # Print the found password.
			break

def main():
	list = getlist("https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt?raw=true")
	password = input("What is your password? ") # This can be blocked off if you have a hash and no password. Switch the blocking of text below if so.
	passhash = hash(password) # OR passhash = "5f4dcc3b5aa765d61d8327deb882cf99"
	print(f"Password Hash is: {passhash}")
	bruteforce(list, passhash)
	pass

main()