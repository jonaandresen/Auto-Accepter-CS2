# Auto-Accepter-CS2
Simple tool to automatically accept an upcoming game in Counter-Strike 2

# How does it work?
- Start the autoaccept.exe in the releases folder
- Open CS2 (main monitor)
- If the "accept" button appears on the screen, the program will click it
- The program will check every 2 seconds for the button

# How does the magic work?
The "magic" is a Python tool that looks for the green color in the "Accept" button.
When the green image appears on the screen, the tool collects its coordinates and clicks in the middle of it.

# Can I use if for other games?
Sure, but you have to take a screenshot of the accept button and replace the "accept.png".
You don't need the whole Button just a clear characteristic of it.
Then compile with:

```python -m PyInstaller --onefile --icon=app.ico --add-data "accept.png:." .\autoaccept.py```
