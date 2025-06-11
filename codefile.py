
def encryption(text,shift):
	encrypt_txt=""
	for char in text.upper():
		if char.isalpha():
			encrypt_txt += chr((ord(char)-65+shift)%26 + 65)
		else:
			encrypt_txt+=char
	return encrypt_txt

def decryption(text,shift):
	return encryption(text,-shift)


while True :
	print("caeser cipher")
	print("menu : \n1. Encrypt\n2. Decrypt\n3. Exit")


	option = input("Enter your choice : ")

	if option == '1':
		text = input("enter the text for encryption :")
		shift = int(input("enter the shift number :"))
		print("encrypted text:",encryption(text,shift))

	elif option == '2':
		text= input("enter the text for decrypt:")
		shift= int(input("enter the shift number :"))
		print("decrypted text:",decryption(text,shift))

	elif option == '3':
		break
	else:
		print("invalid option is choosen!!!!")
