Creating a Windows setup installer with Electron-builder
=========

There are a number of ways to create a Windows setup installer for an Electron app.
 
* Grunt-Electron-Installer
* Electron-installer-squirrel-windows
* electron-packager
* electron-builder
 
## using npm module electron-builder
electron-builder takes care of building your Electron app for multiple platforms, 
it also handles some platform-specific issues:

    * Packaging your app to support applying app updates
    * Being able to sign the code as a security measure for Mac and Windows app stores
    * Managing versioned builds of the app
    * Compiling native modules for each OS platform

## install electron-builder 

install electron-builder as a global npm module.
```
npm install -g electron-builder
cd path-to-app && npm i electron –save-dev
```

create a version of the app that has a Windows installer.
electron-builder relies on build configuration information being present in the app’s package.json file
electron-builder requires that the following fields are present in the package.json file:

* Name
* Description
* Version
* AuthorCreating a setup installer for your Windows app
* path to icon to be used
* script commands to run using npm run on the command line.

Here’s an example of what those fields should look like:
```
{
"name": "hello-world",
"description":"An Electron application",
"version": "1.0.0",
"author" : "Electrong <Electrong@electrong.com>",
"build": {"iconUrl":" https://github.com/paulbjensen/lorikeet/raw/master/icon.ico" },
"scripts": { "pack": "build", "dist": "build" }
}
```

If you were to run npm run pack at the command-line prompt, 
you’d see that the app executables are packaged in the newly created dist folder.

When you browse the dist
folder, you’ll see that the Electron app has been turned into .exe files for different
processor architectures (ia32 and x86-64).

At this point, electron-builder then wraps another npm module that handles
building the Electron app as a Windows installer. 

This is a module called [electron-windows-installer](https://github.com/electronjs/windows-installer#usage).

If you rename the name field of the package.json file to hello and run 
```
npm run dist
```
electron-builder creates the following Windows-based installer items for the app:

* A nupkg file for installing the app via the NuGet package manager
* A .exe file
* A Microsoft Setup Installer (.msi) file named setup.msi
 
With these files, you can install the app on other computers via a single file.
That covers creating a Windows setup installer for Electron. 
