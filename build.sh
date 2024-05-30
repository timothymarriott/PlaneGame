#bin/bash
rm -r ./dist/1942.app/
pyinstaller --windowed --onedir -n 1942 -i ./icon-windowed.icns -F ./PlaneGame.py
cp -R ./assets ./dist/1942.app/Contents/Resources/assets/
rm -R ./build
rm ./dist/1942.app/
rm ./dist/1942
cd ./dist
zip -r 1942-Build-$(date +%d-%M-%Y) 1942.app
cd ..
open ./dist