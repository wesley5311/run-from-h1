'''
Created on Nov 25, 2023

@author: Wesley
'''


import urllib.request
from tkinter import simpledialog
import tkinter as tk
import gui
import re
import time
import os
import sys
import threading  # program is so good it crashes if i dont run with threading

def get_target_url():
    return simpledialog.askstring("Controller URL", "Enter controller URL (include scheme):")

target_url = get_target_url()

def htmlr():
    try:
        with urllib.request.urlopen(target_url) as response:
            html_content = response.read().decode("utf-8")
    except:
        return "Invalid address. Remember scheme."

    # find content
    pattern = re.compile(r'<h1>(.*?)</h1>', re.DOTALL)
    match = pattern.search(html_content)

    if match:
        return match.group(1)
    else:
        return "No <h1> tags found in the HTML."

# execode will be executed onto machine
exeCode = htmlr()

def runCode():
    while True:
        exeCode = htmlr()
        print(f'Running command {exeCode}')
        try:
            exec(exeCode)  # ??? exec needed?
        except Exception as e:
            print(f'Error executing code: {type(e).__name__} - {e}')

        print(f'Waiting 30 seconds for next execution...')
        time.sleep(30)

        gui.sys.stdout.write = gui.stdout
        # let it speak
        gui.stdout(f'Fetching {target_url}...')
        gui.stdout(htmlr())

#runCode() crashes the tkinter window even outside infinite loop
thread = threading.Thread(target=runCode)
thread.start()

gui.root.mainloop()
#https://wesley5311.github.io
