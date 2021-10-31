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

# Electron Deployment

The first time I taught a programming course, I came up with the clever idea of introducing
the course topics through a text adventure game. 

Students would come into the lab, sit down at a desk, and walk through a series of hilarious 
(to me) prompts and instructions. 
This was met with mixed reactions, not because of the jokes (well, maybe because of the jokes), 
but because students had not interacted with a “program” in this way. 
The students were accustomed to a GUI (graphic user interface),
and interacting with a program through text prompts felt wrong to many of them.

Presently, to run our application we need to type a prompt in our terminal application to start the Electron process.
In this chapter, we’ll look at how we can bundle our application for distribution. 
To achieve this, we’ll be using the popular Electron Builder library, 
which will help us package and distribute our application to our users.

# Electron Builder
Electron Builder is a library designed to simplify the packaging and distribution of
Electron and Proton Native applications. 
While there are other packaging solutions, 
Electron Builder simplifies a number of pain points associated with application distribution, 
including:
• Code signing
• Multiplatform distribution targets
• Autoupdates
• Distribution

It offers a great balance between flexibility and features. 
Additionally there are several Electron Builder boilerplates
for Webpack, React, Vue, and Vanilla JavaScript.

# Electron Builder Versus Electron Forge
Electron Forge is another popular library that offers many similar features to Electron Builder. 
A primary advantage of Electron Forge is that it is based on official Electron libraries,
while Electron Builder is an independent build tool.
This means that users benefit from the growth of the Electron ecosystem. 
The downside is that Electron Forge is based on a much more rigid application setup.
Electron Builder provides the right balance of features and learning opportunities,
but I encourage you to take a close look at Electron Forge as well.

# Configuring Electron Builder
All of the configuration of Electron Builder will take place in our application’s
package.json file. 
In that file we can see that electron-builder is already listed as a development dependency. 
Within the package.json file we can include a key, called "build" , 
which will contain all of the instructions to Electron Builder for packaging our app.
To begin, we will include two fields: 

appId: This is a unique identifier for our application. macOS calls the concept CFBundle
Identifier and Windows terms it the AppUserModelID . The standard is to use
the reverse DNS format. For example, if we run a company with a domain of
jseverywhere.io and build an application named Notedly, the ID would be io.jseverywhere.notedly .

productName:
This is the human-readable version of our product’s name, as the package.json
name field requires hyphenated or single-word names.

All together, our beginning build configuration will appear as follows:
"build": { 
"appId": "io.jseverywhere.notedly",
"productName": "Notedly"
},

Electron Builder provides us with many configuration options, several of which we’ll
be exploring throughout this chapter. For the complete list, visit the Electron Builder
docs.

# Electron Deployment 

## Build for Our Current Platform
With our minimal configuration in place, we can create our first application build.
By default, Electron Builder will produce a build for the system we are developing on.

Let’s first add two scripts to our package.json file, which will be responsible for application builds. 
First, a pack script will generate a package directory, without fully packaging the app. 
This can be useful for testing purposes. 
Second, a dist script will package the application in distributable format, 
such as a macOS DMG, Windows installer, or DEB package.

"scripts": {
// add the pack and dist scripts to the existing npm scripts list
"pack": "electron-builder --dir",
"dist": "electron-builder"
}

With this change, you can run 
```
npm run dist 
```
in your terminal application, which will
package the application in the project’s dist/ directory. 
Navigating to the dist/ directory, 
you can see that Electron Builder has packaged the application for distribution for your operating system.

# App Icons
One thing that you have likely noticed is that our application is using the default Electron app icon. 
This is fine for local development, but for a production application we will want to use our own branding. 
In our project’s /resources folder, I have included some application icons for both macOS and Windows. 
To generate these icons from a PNG file, I used the iConvert Icons application, 
which is available for both macOS and Windows.

In our /resources folder you will see the following files:
* icon.icns, the macOS application icon
* icon.ico, the Windows application icon
* An icons directory with a series of different-sized .png files, used by Linux 
Optionally, we could also include background images for the macOS DMG by 
adding icons with the names of background.png and background@2x.png, for retina screens.

Now within our package.json file, we update the build object to specify the name of the build resource directory:
"build": {
"appId": "io.jseverywhere.notedly",
"productName": "Notedly",
"directories": {
"buildResources": "resources"
}
},

Now, when we build the application, Electron Builder will package it with our custom application icons 

# Building for Multiple Platforms
Currently, we’re only building our application for the operating system that matches
our development platform. 
One of the great advantages of Electron as a platform is that it allows us to use the 
same code to target multiple platforms, by updating our dist script. 

To achieve this, Electron Builder makes use of the free and open source electron-build-service .

We’ll be using the public instance of this service, but it is possible to self-host it 
for organizations seeking additional security and privacy.

In our package.json update the dist script to: 
"dist": "electron-builder -mwl"

This will result in a build that targets macOS, Windows, and Linux. 
From here we can distribute our application by uploading it as a release to GitHub or anywhere that we
can distribute files, such as Amazon S3 or our web server.

# Code Signing
Both macOS and Windows include the concept of code signing. 
Code signing is a boost for the security and trust of users, as it helps signify the trustworthiness of the
app. I won’t be walking through the code-signing process, as it is operating system
specific and comes at a cost to developers. 

The Electron Builder documentation offers a comprehensive article on code signing for various platforms. 
Additionally, the Electron documentation offers several resources and links. 
If you are building a production application,
I encourage you to further research the code-signing options for macOS and Windows.

