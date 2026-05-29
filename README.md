# 🐍 Snake Game

A classic **Snake Game implementation in Python**, built using **Pygame** with support for both human gameplay and experimental AI-based approaches.

This project demonstrates fundamental concepts in:
- Game development 🎮
- Event-driven programming ⚙️

---

## 📌 Overview

This repository contains a Python implementation of the traditional Snake game where the player controls a snake that grows by eating food while avoiding collisions with walls and itself.

---

## ✨ Features

- 🐍 Classic Snake game mechanics
- 🎯 Food collection and score tracking
- ⛔ Collision detection (walls)
- 🎮 Keyboard controls

---

## 🧠 How It Works

The game loop continuously performs the following steps:

1. Capture user input (or AI action)
2. Update snake position
3. Check collisions:
   - Wall collision
   - Self collision
4. Generate food if eaten
5. Render updated game state

---

## 🎮 Controls

### Player Mode
- ⬆️ W /I → Move Up  
- ⬇️ S / K → Move Down  
- ⬅️ A / J → Move Left  
- ➡️ D / L → Move Right  


---

## ▶️ Run the Game

```bash
main.py
```

---

## 🧠 Concepts Used

- Game loops and frame updates
- Collision detection algorithms
- Grid-based movement system
- Event handling (keyboard input)

---


## 🛠 Requirements

- Python 3.x
- Pygame

Install Pygame:

```bash
pip install pygame
```
---

## 📜 License

This project is intended for educational purposes and learning game development concepts in Python.
