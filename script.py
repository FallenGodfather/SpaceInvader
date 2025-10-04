new_readme = '''# Space Invaders (Pygame)

This is a simple Space Invaders game built with Python using the Pygame library. It’s actually the **second video game I've ever created in Pygame**, but I’m sharing it here now.

## How to play
- Use **Arrow Keys** or **WASD** to move your ship
- Press **Spacebar** to shoot
- Defeat all aliens and try to get the highest score!

## About
- Made as a personal learning project
- Inspired by the classic arcade game

## Author & Publisher
**Created and published by:** FallenGodfather (Hassan Ali)

---
Have fun and enjoy!'''

with open('README.md', 'w') as f:
    f.write(new_readme)

print('✅ Created new, concise, personal README.md')