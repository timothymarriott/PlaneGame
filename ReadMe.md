# 1942 REMAKE
This is a remake of the 1984 arcade game by Capcom: 1942.\
It is a vertically scrolling shooter.

## How To Run
You will require python to be installed to open the build available, it will automatically install pygame, in the case it fails to open use the below instructions.\
Otherwise, Clone the repository install pygame with pip, then in the project directory run.
```bash
python3 PlaneGame.py
```

## Controls

### Menu
Space to navigate menu.\
Enter to select.
### Game
W,A,S,D To move plane.\
Space to shoot.\
V to use Bomb powerup.\
Escape to return to menu.
### Cheats
Z for debug menu.\
I for god mode. (Will invalidate score)\
Infinite Bomb Powerup when in godmode.\
Full Stop to go to next wave.\
Comma to go to previous wave.\
C gives regular powerup.

## Technical Info
The remake has been made in about five weeks. In a team of three, Timothy Marriott, Sebastian Strano and Dane Ebey. The engine uses pygame as the backend and a custom written framework for asset and object management.

### Build Instructions
In the root directory of the project run.
```bash
./build.sh
```