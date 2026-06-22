import random
import string 
print("==== Password Generator ===")
length = int(input("Enter the desired password length: "))
caracteres = string.ascii_letters + string.digits + string.punctuation    
password = ''.join(random.choice(caracteres) for i in range(length))
print(f"Generated Password: {password}")          