pyinstaller --windowed --onedir -n 1942 -i ./icon-windowed.icns -F ./PlaneGame.py
cp -R ./assets ./dist/1942.app/Contents/Resources/assets/
rm -R ./build
rm ./dist/1942
cd ./dist
zip -r 1942-Build-$(date +%Y%m%d_%H%M%S%Z) 1942.app
open ./dist