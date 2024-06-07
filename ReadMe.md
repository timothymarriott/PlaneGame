# 1942 REMAKE
This is a remake of the 1984 arcade game 1942 by Capcom. It is a vertically scrolling shooter.

## How To Run
If the available build works on your Mac just open that.
Otherwise, Clone the repository and in the root directory run.
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
The remake has been made in about five weeks. In a team of three, Timothy Marriott, Sebastion Strano and Dane Ebey. The engine uses pygame as the backend and a custom written framework for asset and object management.
## Build Info
A rudimentary build system has been implemented but it is inconsistent and may not work on certain devices due to altered configuration this will cause it to fail to open on certain devices. The build system is only available for apple silicon MacOS devices, tested on M1 Macbook Air and Pro.

### Build Instructions
In the root directory of the project run.
```bash
./build.sh
```