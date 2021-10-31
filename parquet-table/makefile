
build_deps:
	npm install -g electron-builder
	npm install -g asar

build_dir:
	mkdir -p build

dist_dir:
	mkdir -p dist

clean:
	rm -rf build
	rm -rf dist

electron-v15.2.0-linux-x64.zip:
	wget https://github.com/electron/electron/releases/download/v15.2.0/electron-v15.2.0-linux-x64.zip

build/electron-v15.2.0-linux-x64.zip: build_dir electron-v15.2.0-linux-x64.zip
	cp electron-v15.2.0-linux-x64.zip build

build/electron-v15.2.0-linux-x64: build_dir build/electron-v15.2.0-linux-x64.zip
	cd build && unzip -u electron-v15.2.0-linux-x64.zip -d electron-v15.2.0-linux-x64

build/web:
	cp -r web build

build/web/node_modules: build/web
	cd build/web && npm install

__main__.spec: build_dir dist_dir
	pyinstaller \
--noconfirm \
--onedir \
--console \
--workpath build \
--distpath dist \
parquet_table/__main__.py

dist/__main__/__main__: build_dir dist_dir
	pyinstaller \
--noconfirm \
--onedir \
--console \
--workpath build \
--distpath dist \
__main__.spec

serve: dist/__main__/__main__
	cd dist/__main__ && ./__main__

build/web/__main__/__main__: build/web dist/__main__/__main__
	cp -r dist/__main__ build/web

build/app.asar: build/web/node_modules build/web/__main__/__main__
	cd build && asar pack web app.asar

build/electron-v15.2.0-linux-x64/resources/app.asar: build/electron-v15.2.0-linux-x64 build/app.asar
	cp build/app.asar build/electron-v15.2.0-linux-x64/resources

dist/app.asar: build/app.asar
	cp build/app.asar dist

run: build/electron-v15.2.0-linux-x64/resources/app.asar
	cd build/electron-v15.2.0-linux-x64 && ./electron

build/web/dist/parquet-table-desktop-0.1.0.AppImage: build/app.asar
	cd build/web && sudo electron-builder

dist/parquet-table-desktop-0.1.0.AppImage: build/web/dist/parquet-table-desktop-0.1.0.AppImage
	cp build/web/dist/parquet-table-desktop-0.1.0.AppImage dist
