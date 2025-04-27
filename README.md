# Oblivion-like Game Engine

A Python-based game engine using ModernGL and Pyglet, inspired by The Elder Scrolls IV: Oblivion.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
game_engine/
├── src/                    # Source code
│   ├── core/              # Core engine systems
│   ├── graphics/          # Graphics and rendering
│   ├── input/             # Input handling
│   └── utils/             # Utility functions
├── assets/                # Game assets
│   ├── models/           # 3D models
│   ├── textures/         # Textures
│   └── shaders/          # GLSL shaders
├── tests/                # Test files
└── config/              # Configuration files
```

## Running the Project

To run the basic engine:
```bash
python src/main.py
```

## Development

This project follows the roadmap outlined in `roadmap.md`. Development is broken down into phases, with each phase focusing on specific components of the game engine.

## License

MIT License 