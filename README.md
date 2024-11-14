# Vim Tutorial Game

An interactive game to learn Vim commands through practical exercises.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shahinabdi/vim-tutorial-game.git
cd vim-tutorial-game
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (if any): 
```bash
pip install -r requirements.txt # No dependencies for now
```

## Usage

Run the game:
```bash
python main.py
```

## Features

- Interactive Vim command learning
- Multiple lessons:
  - Basic movement (hjkl)
  - Insert mode
  - Delete operations
- Real-time feedback
- Progress tracking

## Development

1. Create a feature branch from develop:
```bash
git checkout develop
git checkout -b feature/feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "feat: Add your feature"
```

3. Push your feature branch:
```bash
git push origin feature/feature-name
```

4. Create a pull request to develop branch

## Branch Structure

- `main`: Production-ready code
- `develop`: Development branch
- `feature/*`: New features
- `hotfix/*`: Critical bug fixes
- `release/*`: Release preparation

## Version Tags

- v1.0.0: Initial release
  - Basic movement lesson
  - Insert mode lesson
  - Delete command lesson

## License

MIT License - See LICENSE file for details