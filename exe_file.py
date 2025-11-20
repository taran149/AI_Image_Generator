import os
import subprocess
import sys

# --------- CONFIG ---------
# Path to your main Python script
main_script = "pollination_image.py"  # <-- your script filename
# Optional: icon for EXE
icon_file = ""  # leave empty if you don't have an icon

# --------- CREATE EXE ---------
# Check if file exists
if not os.path.exists(main_script):
    print(f"❌ File '{main_script}' not found in current directory!")
    sys.exit(1)

# Build PyInstaller command
cmd = [
    "pyinstaller",
    "--onefile",
    "--noconsole",  # remove if you want console window
]

if icon_file and os.path.exists(icon_file):
    cmd.append(f"--icon={icon_file}")

cmd.append(main_script)

# Run PyInstaller
print("🚀 Creating EXE...")
subprocess.run(cmd)

# Success message
print("\n✅ Done! Check the 'dist' folder for your EXE.")
