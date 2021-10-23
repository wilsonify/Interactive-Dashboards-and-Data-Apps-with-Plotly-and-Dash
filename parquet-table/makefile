
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
	cd build && unzip electron-v15.2.0-linux-x64.zip -d electron-v15.2.0-linux-x64

build/electron-v15.2.0-linux-x64/resources/parquet-table.asar: build/electron-v15.2.0-linux-x64
	asar pack main.js

/web/node_modules:
	cd web && npm install

build/electron-v15.2.0-linux-x64/resources/parquet-table.asar: app.asar
	cp app.asar build/electron-v15.2.0-linux-x64/resources

__main__.spec:
	pyinstaller \
--noconfirm \
--onedir \
--console \
--workpath build \
--distpath dist \
parquet_table/__main__.py

dist/__main__/__main__:
	pyinstaller \
--noconfirm \
--onedir \
--console \
--workpath build \
--distpath dist \
__main__.spec

run: dist/__main__/__main__
	cd dist/__main__ && ./__main__

web/__main__/__main__: dist/__main__/__main__
	cp -r dist/__main__ web

app.asar: /web/node_modules web/__main__/__main__
	asar pack web app.asar
