# Requirements:
```commandline
pip install -r requirements.txt 
```

# How to Use
1. Download or clone this repository.
3. Open Terminal and cd to the seo-bot-python respository downloaded in step 
4. Run: pip install -r requirements.txt  
5. Run: python main.py


# How seobot works
1. Sets up a default proxy at local host.
2. Initialises SSL. 
3. Takes a target URL from user input.
4. Opens Tor Browser, waits to load.
5. Opens target URL in new tab, waits to load.
6. Changes identity every 50 seconds through port 9151, previously initialised in steps 1 and 2.
7. Returns read and write bytes generated after each switch.

