# PyBuster
PyBuster is a lightweight and user-friendly directory and file discovery tool built in Python. It sends HTTP GET and POST requests to discover hidden directories, files, or endpoints on a target URL using a wordlist. You can optionally specify file extensions to append to the wordlist entries.

# Features
- 🗂️ Wordlist-based directory scanning.
- 🔄 Sends both GET and POST requests to detect hidden resources.
- 🏷️ Optionally append file extensions to wordlist entries (e.g., .php, .html).
- 📈 Displays progress through the wordlist with real-time updates.
- 🔧 Simple command-line interface with help flags and usage examples.

# Install the required libraries
```bash
pip install requests tqdm
```
# Usage
## Running the Tool
Just run the script, and it will prompt you for the necessary inputs. Set the following parameters:

- **URL**: The target URL you want to scan.
- **WORDLIST PATH**: The path to your wordlist file.
- **OPTIONAL EXTENSION**: The file extension to append to wordlist entries (e.g., php).

 Run the following command:
```bash
 python3 PyBuster.py -u [URL] -w [WORDLIST PATH] -e [OPTIONAL EXTENSION]
```

# Example: 
```bash
python3 PyBuster.py -u https://www.example.com/ -w /path/to/wordlist.txt -e php
``` 
