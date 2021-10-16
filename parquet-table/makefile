
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

app.asar: /web/node_modules
	asar pack web app.asar

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

dist/__main__/data:
	cp -r data dist/__main__/data

dist/__main__/site-packages:
	cp -r /home/thom/repos/venvs/plotly-dash/lib/python3.8/site-packages/* dist/__main__