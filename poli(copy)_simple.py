# import requests
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import threading
# import io
# from urllib.parse import quote

# # -------------------------------
# # Image Generation Function
# # -------------------------------

# def generate_image():
#     prompt = prompt_entry.get()
#     size_option = size_var.get()

#     if prompt.strip() == "":
#         status_label.config(text="⚠️ Please enter a prompt first!", foreground="red")
#         return

#     generate_btn.config(state="disabled")
#     status_label.config(text="✨ Generating image... Please wait ⏳", foreground="blue")
#     loading_label.config(text="🔄 Loading...", foreground="purple")

#     thread = threading.Thread(target=generate_image_thread, args=(prompt, size_option))
#     thread.start()

# def generate_image_thread(prompt, size_option):
#     try:
#         width, height = map(int, size_option.split("x"))
#         encoded_prompt = quote(prompt)

#         url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux"

#         response = requests.get(url, timeout=60)
#         image = Image.open(io.BytesIO(response.content))

#         img_tk = ImageTk.PhotoImage(image.resize((350, 350)))
#         image_label.config(image=img_tk)
#         image_label.image = img_tk

#         image.save("output/generated_image.png")
#         status_label.config(text="✅ Image generated successfully! Saved in output/", foreground="green")

#     except Exception as e:
#         status_label.config(text=f"❌ Error: {e}", foreground="red")

#     finally:
#         generate_btn.config(state="normal")
#         loading_label.config(text="")

# # -------------------------------
# # GUI Setup
# # -------------------------------
# root = tk.Tk()
# root.title("AI Image Generator — Pollinations Model")
# root.geometry("500x650")
# root.config(bg="#F0F8FF")

# title_label = tk.Label(root, text="🎨 AI Image Generator", font=("Helvetica", 20, "bold"), bg="#F0F8FF")
# title_label.pack(pady=20)

# prompt_label = tk.Label(root, text="Enter Prompt:", font=("Arial", 12), bg="#F0F8FF")
# prompt_label.pack()
# prompt_entry = tk.Entry(root, width=50, font=("Arial", 12), relief="solid", borderwidth=2)
# prompt_entry.pack(pady=5)

# size_label = tk.Label(root, text="Select Image Size:", font=("Arial", 12), bg="#F0F8FF")
# size_label.pack(pady=(10, 0))
# size_var = tk.StringVar(value="512x512")
# size_dropdown = ttk.Combobox(root, textvariable=size_var, values=["512x512", "768x768", "1024x1024"], state="readonly", width=15)
# size_dropdown.pack(pady=5)

# def on_hover(event):
#     generate_btn.config(bg="#45a049")

# def off_hover(event):
#     generate_btn.config(bg="#4CAF50")

# generate_btn = tk.Button(root, text="🚀 Generate Image", command=generate_image, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20)
# generate_btn.pack(pady=20)

# generate_btn.bind("<Enter>", on_hover)
# generate_btn.bind("<Leave>", off_hover)

# loading_label = tk.Label(root, text="", font=("Arial", 12), bg="#F0F8FF")
# loading_label.pack()

# status_label = tk.Label(root, text="", font=("Arial", 12), bg="#F0F8FF")
# status_label.pack(pady=5)

# image_label = tk.Label(root, bg="#E0E0E0", width=350, height=350, relief="solid", bd=2)
# image_label.pack(pady=20)

# root.mainloop()