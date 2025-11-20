import os
import requests
import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import io
from urllib.parse import quote

# -------------------------------
# Settings
# -------------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

history_images = []
history_buttons = []

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# -------------------------------
# Image Generation
# -------------------------------
def generate_image():
    prompt = prompt_entry.get()
    size_option = size_var.get()

    if prompt.strip() == "":
        status_label.configure(text="⚠️ Enter a prompt!", text_color="#FF5555")
        return

    generate_btn.configure(state="disabled", text="⏳ Generating...")
    status_label.configure(text="")

    threading.Thread(target=generate_image_thread, args=(prompt, size_option)).start()

def generate_image_thread(prompt, size_option):
    try:
        width, height = map(int, size_option.split("x"))
        encoded_prompt = quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux"

        response = requests.get(url, timeout=60)
        image = Image.open(io.BytesIO(response.content))
        image.save(f"output/generated_{len(history_images)+1}.png")

        # Resize for main display
        display_img = image.resize((350, 350))
        img_tk = ImageTk.PhotoImage(display_img)

        image_label.configure(image=img_tk)
        image_label.image = img_tk

        # Add to history
        add_to_history(display_img)

        status_label.configure(text="✅ Image generated!", text_color="#00FFFF")

    except Exception as e:
        status_label.configure(text=f"❌ Error: {e}", text_color="#FF5555")

    finally:
        generate_btn.configure(state="normal", text="🚀 Generate Image")

# -------------------------------
# History Thumbnails
# -------------------------------
def add_to_history(pil_img):
    img_thumb = pil_img.resize((80, 80))
    img_tk = ImageTk.PhotoImage(img_thumb)
    history_images.append(img_tk)

    btn = ctk.CTkButton(history_canvas, image=img_tk, text="", width=80, height=80,
                         fg_color="#2A2A2A", hover_color="#444444",
                         command=lambda i=len(history_images)-1: show_history(i))
    btn.pack(side="left", padx=5, pady=5)
    history_canvas.update_idletasks()

def show_history(index):
    img = history_images[index]
    image_label.configure(image=img)
    image_label.image = img

# -------------------------------
# GUI Setup
# -------------------------------
root = ctk.CTk()
root.title("🎨 AI Image Generator — Pollinations")
root.geometry("600x800")
root.resizable(False, False)

# Title
ctk.CTkLabel(root, text="🎨 AI Image Generator", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=15)

# Prompt Entry
ctk.CTkLabel(root, text="Enter Prompt:", font=ctk.CTkFont(size=14)).pack()
prompt_entry = ctk.CTkEntry(root, width=500, font=ctk.CTkFont(size=14))
prompt_entry.pack(pady=5)

# Size Dropdown
ctk.CTkLabel(root, text="Select Image Size:", font=ctk.CTkFont(size=14)).pack(pady=(5,0))
size_var = ctk.StringVar(value="512x512")
size_dropdown = ctk.CTkComboBox(root, variable=size_var, values=["512x512", "768x768", "1024x1024"], width=150, dropdown_font=ctk.CTkFont(size=12))
size_dropdown.pack(pady=5)

# Generate Button
generate_btn = ctk.CTkButton(root, text="🚀 Generate Image", width=220, height=50,
                             font=ctk.CTkFont(size=14, weight="bold"),
                             fg_color="#222222", hover_color="#5555FF", text_color="#00FFFF",
                             command=generate_image)
generate_btn.pack(pady=15)

# Status Label
status_label = ctk.CTkLabel(root, text="", font=ctk.CTkFont(size=12))
status_label.pack(pady=5)

# Main Image Display
image_frame = ctk.CTkFrame(root, width=370, height=370, corner_radius=15)
image_frame.pack(pady=20)
image_label = ctk.CTkLabel(image_frame, text="")
image_label.pack(expand=True, fill="both", padx=5, pady=5)

# History Scrollable Frame
history_label = ctk.CTkLabel(root, text="🖼 Image History", font=ctk.CTkFont(size=14))
history_label.pack(pady=(10,0))

history_canvas = ctk.CTkScrollableFrame(root, width=550, height=120, corner_radius=10)
history_canvas.pack(pady=5)

root.mainloop()
