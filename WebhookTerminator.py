import tkinter as tk
import requests
from tkinter import messagebox

def delete_webhooks():
    if not url_entry.get("1.0", tk.END).strip():
        messagebox.showwarning("No Webhooks", "Add the webhooks, dumbass!")
        return
    
    urls = url_entry.get("1.0", tk.END).split('\n')
    for url in urls:
        response = requests.delete(url.strip())
        if response.status_code == 204:
            output_box.insert(tk.END, f"LIGMABALLZ TERMINATED THIS WEBHOOK: {url} ;)\n", "success")
        else:
            output_box.insert(tk.END, f"Failed to terminate {url}. Status code: {response.status_code}\n", "error")

root = tk.Tk()
root.title("Webhook Terminator")
title_label = tk.Label(root, text="WEBHOOK TERMINATOR", font=("Helvetica", 16, "bold"), fg="red")
title_label.pack(pady=10)
url_label = tk.Label(root, text="Enter the URLs of the nigga webhooks (one per line):")
url_label.pack()
url_entry = tk.Text(root, width=50, height=5)
url_entry.pack()
delete_button = tk.Button(root, text="Terminate Webhooks", command=delete_webhooks)
delete_button.pack(pady=10)
output_box = tk.Text(root, width=60, height=10)
output_box.pack()
output_box.tag_config("success", foreground="green")
output_box.tag_config("error", foreground="red")

root.mainloop()
