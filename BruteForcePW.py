import string
pw = input("Insert Password: \n")
def BruteForce(pw=str):
	print("[+][+] Starting BruteForce...")
	charset = list(string.ascii_letters + string.digits + string.punctuation)
	result = ""
	x = 0
	while x <= len(pw)-1:
		for char in charset:
			pchar = pw[x]
			if char == pchar:
				print("[+] Trying...", char)
				print("[+][+] Matched (",char, ")")
				result += char
				print("[+][+] Current:",result)
				x += 1
				break
			else:
				print("[+] Trying...",char)
	print("[+][+] Matching Done - Password Found:", result)
bf = BruteForce
 
bf(pw) 
#PW MaxLenght is : about 10
