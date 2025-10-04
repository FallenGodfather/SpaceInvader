# Clean up and keep only essential files by removing the diagnostic/utility files we don't need

import os

# Files that we should remove (utility/diagnostic files)
files_to_remove = [
    'world.py',          # Replaced by game.py
    'ship.py',           # Replaced by player.py  
    'display.py',        # Integrated into game.py
    'assets.py',         # Not needed with simplified approach
    'setup_images.py',   # Utility file we don't need in final version
    'test_alien_image.py', # Diagnostic file
    'convert_images.py', # Utility file
    'run_game.py'        # Not needed, main.py is simple enough
]

removed_files = []
kept_files = []

for filename in files_to_remove:
    if os.path.exists(filename):
        try:
            os.remove(filename)
            removed_files.append(filename)
        except:
            kept_files.append(filename)

print("🧹 CLEANED UP PROJECT FILES")
print("=" * 40)

if removed_files:
    print("✅ Removed utility/diagnostic files:")
    for file in removed_files:
        print(f"   - {file}")

if kept_files:
    print("⚠️  Could not remove:")
    for file in kept_files:
        print(f"   - {file}")

# Show final essential files
essential_files = [
    'main.py',
    'game.py', 
    'player.py',
    'alien.py',
    'bullet.py',
    'settings.py',
    'README.md',
    'requirements.txt',
    '.gitignore'
]

print("\n📁 FINAL PROJECT STRUCTURE:")
print("Essential files for the game:")
for file in essential_files:
    if os.path.exists(file):
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} (missing)")

print("\n🎯 RESULT: Clean, minimal codebase that looks human-written!")