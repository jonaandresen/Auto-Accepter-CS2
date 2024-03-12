# Auto-Accepter-CS2
Simple tool to automatically accept an upcoming game.

# How does it work?
- Start the autoaccept.exe in the releases folder
- Open CS2 (main monitor)
- If the "accept" button appears on the screen, the program will click it
- If no "accept" button appears on the screen, the program will check every 2 seconds.

# How does the magic work?
The "magic" is a Python tool that looks for the green colour in the "Accept" button.
When the green image appears on the screen, the tool collects its coordinates and clicks in the middle.

# Can I use if for other games?
Sure, but you have to take a screenshot of the accept button and replace the "accept.png".
Then compile with:
```python -m PyInstaller --onefile --icon=app.ico --add-data "accept.png:." .\autoaccept.py```
