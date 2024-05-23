#bin/bash
rm -R ./dist
pyinstaller --windowed --onedir -n 1942 -i ./icon-windowed.icns -F ./PlaneGame.py
cp -R ./assets ./dist/1942.app/Contents/Resources/assets/