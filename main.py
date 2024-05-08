# COPYRIGHT Sapphire code 2024
import pyperclip
import hashlib
import pyfiglet
from colorama import Fore, Back, Style

print(pyfiglet.figlet_format("Hash-Zen"))
print(f"Unsure? Type {Fore.GREEN}help{Style.RESET_ALL}")

def sha256():
  userInput = input("Convert to SHA-256 hashed text: ")
  hashedOutput = hashlib.sha256(userInput.encode('ascii')).hexdigest()
  print(f'\n{Fore.GREEN}SHA-256 Output{Style.RESET_ALL}: {hashedOutput}\n')
  clipboardQuestion = input("Copy to clipboard? (y/n)?: ")

  if clipboardQuestion.lower() == "y":
    try:
      pyperclip.copy(hashedOutput)
      CheckString = input("Paste the copied text here: ")
      if CheckString == hashedOutput:
        print(f"{Fore.GREEN}The text has been copied correctly :){Style.RESET_ALL}")
      
      else:
        print(f"{Fore.RED}The text wasn't copied to your clipboard correctly. Please try again :({Style.RESET_ALL}")
    except Exception as error:
      print(error)

  if clipboardQuestion.lower() == "n":
    print(f"{Fore.RED}Text has not been copied{Style.RESET_ALL}")


def md5():
  userInput = input("Convert to MD5 hashed text: ")
  hashedOutput = hashlib.md5(userInput.encode('ascii')).hexdigest()
  print(f'\n{Fore.GREEN}MD5 Output{Style.RESET_ALL}: {hashedOutput}\n')
  clipboardQuestion = input("Copy to clipboard? (y/n)?: ")

  if clipboardQuestion.lower() == "y":
    try:  
      pyperclip.copy(hashedOutput)
      CheckString = input("Paste the copied text here: ")
      if CheckString == hashedOutput:
        print(f"{Fore.GREEN}The text has been copied correctly :){Style.RESET_ALL}")

      else:
        print(f"{Fore.RED}The text wasn't copied to your clipboard correctly. Please try again :({Style.RESET_ALL}")
    except Exception as error:
       print(error)

  if clipboardQuestion.lower() == "n":
    print(f"{Fore.RED}Text has not been copied{Style.RESET_ALL}")
  


while True:
  userInput = input("Select your Hasher: ")
  match userInput.lower():
    case "help": print(f"""\nType {Fore.GREEN}sha256{Style.RESET_ALL} to convert text to SHA-256 hash\nType {Fore.GREEN}md5{Style.RESET_ALL} to convert text to MD5 hash\nType {Fore.RED}exit{Style.RESET_ALL} to exit this program
                                """)
    case "sha256": sha256()
    case "md5": md5()
    case "exit": exit()