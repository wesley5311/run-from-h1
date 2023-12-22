'''
Created on Nov 28, 2023

@author: Wesley
'''

import tkinter as tk
import sys
#from HTTPREAD import target_url
#from HTTPREAD import htmlr



#the box
root = tk.Tk()
root.title("Remote Console")
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="white")


#the output
console_output = tk.Text(height=30, width=50, fg="black", bg="white")
console_output.pack(pady=5)

original_stdout = sys.stdout
#give it a mouth
def stdout(message):
    console_output.insert(tk.END, message + '\n')
    console_output.see(tk.END)

sys.stdout.write = stdout

#let it speak
#stdout(f'Fetching {target_url}...')
#stdout(htmlr())



#root.mainloop()


