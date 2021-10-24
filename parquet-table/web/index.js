const { app, BrowserWindow } = require('electron');
const { is, setContentSecurityPolicy } = require('electron-util');
const config = require('./config');
var spawn = require("child_process").spawn;
var exec = require('child_process').execFile;

// to avoid garbage collection, declare the window as a variable
let window;

// specify the details of the browser window
function createWindow() {
  window = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: false
    }
  });

  console.log("start dash app");
  exec( '__main__/__main__', [],
     function(err, data) { console.log(err); console.log(data.toString()); }
  );
  //setTimeout(function(){ console.log("started dash app") }, 500);
  
  // load the URL
  window.loadURL(config.LOCAL_WEB_URL);
  //while(!window.webContents.isLoadingMainFrame()) { console.log("waiting for loading"); }


  // set the CSP in production mode
  // a CSP allows us to limit the domains that our application has permission to load resources from.
  // This helps to limit potential XSS and data injection attacks.
  // Electron provides a built-in API for CSP, but the electron-util library offers a simpler and cleaner syntax.
  if (!is.development) {
    setContentSecurityPolicy(`
    default-src 'none';
    script-src 'self';
    img-src 'self' https://www.gravatar.com;
    style-src 'self' 'unsafe-inline';
    font-src 'self';
    connect-src 'self' ${config.PRODUCTION_API_URL};
    base-uri 'none';
    form-action 'none';
    frame-ancestors 'none';
  `);
  }

  // when the window is closed, dereference the window object
  window.on('closed', () => {
    window = null;
  });
}

// when electron is ready, create the application window
app.on('ready', createWindow);

// quit when all windows are closed.
app.on('window-all-closed', () => {
  // On macOS only quit when a user explicitly quits the application
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // on macOS, re-create the window when the icon is clicked in the dock
  if (window === null) {
    createWindow();
  }
});
