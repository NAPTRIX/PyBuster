import sys
import requests
from tqdm import tqdm

# ▼ Inputs, args and variables ▼ 

# The usage of the script
help_message = '''
🤖 PYBUSTER 🤖
USAGE > python3 PyBuster.py -u [URL] -w [WORDLIST PATH] -e [EXTENSION (Optional)]
EXAMPLE > python3 Pybuster.py -u https://www.example.com/ -w /home/user/Desktop/wordlists/dict.txt -e php

▼ ARGS ▼
-h || --help       > Shows the usage of the script
-u || --url        > The URL to send requests to
-w || --wordlist   > Path to your wordlist
-e || --extension  > File extension to append to URLs (Optional)
'''

# The arguments
args = sys.argv

# ▼ Functions ▼

'''
This function makes the requests and checks the status code of them.
If the status code equals 200, 301, or 403, it prints the method, URL, and status code.
'''
def make_request(url, wordlist, ext):
    try:
        with open(wordlist, 'r') as w:
            dirs = w.readlines()
            total = len(dirs)  # Total number of entries in the wordlist
            
            # Use tqdm to create a progress bar
            for d in tqdm(dirs, total=total, desc="Processing", unit="word"):
                d = d.strip()  # Remove newlines and extra spaces
                full_url = f"{url.rstrip('/')}/{d}"
                if ext:
                    full_url += f".{ext}"
                
                # Make GET and POST requests
                r_get = requests.get(full_url)
                r_post = requests.post(full_url)

                # Check and print successful or interesting responses
                if r_get.status_code in [200, 301, 403]:
                    print(f'\nGET - {full_url} - {r_get.status_code}')
                if r_post.status_code in [200, 301, 403]:
                    print(f'\nPOST - {full_url} - {r_post.status_code}')

    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist}' not found.")
    except Exception as e:
        print(f"Error: {e}")


# parse arguments and invoke the request function
def main():
    if len(args) == 1:
        print(help_message)
        return

    if args[1] in ['-h', '--help']:
        print(help_message)
        return

    try:
        # Parsing the URL
        if args[1] in ['-u', '--url']:
            url = args[2]
        else:
            raise ValueError("URL is required. Use -h for help.")

        # Parsing the wordlist
        if args[3] in ['-w', '--wordlist']:
            wordlist = args[4]
        else:
            raise ValueError("Wordlist is required. Use -h for help.")

        # Parsing the optional extension
        ext = ''
        if len(args) > 5 and args[5] in ['-e', '--extension']:
            ext = args[6]

        # If URL and wordlist are provided, start the requests
        make_request(url, wordlist, ext)

    except IndexError:
        print(f"{help_message}Error: Missing required arguments!")
    except ValueError as ve:
        print(f"{help_message}Error: {ve}")
    except Exception as e:
        print(f"{help_message}Error: {e}")

# ▼ Main Execution ▼
if __name__ == "__main__":
    main()
