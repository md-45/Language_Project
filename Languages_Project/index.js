const { app, BrowserWindow, ipcMain } = require("electron");
const { spawn } = require("child_process");

const createWindow = () => {
    const win = new BrowserWindow({
        width: 337,
        height: 378,

        webPreferences: {
            preload: "D:/Languages_Project/Languages_Project/preload.js"
        }
    });

    win.loadFile("D:/Languages_Project/Languages_Project/index.html");
};


ipcMain.on("run-python", () => {

    const python = spawn("python", [
        "D:/Languages_Project/Languages_Project/Web_Scraper.py"
    ]);

    python.stdout.on("data", (data) => {
        console.log(`Python: ${data}`);
    });

    python.stderr.on("data", (data) => {
        console.error(`Python error: ${data}`);
    });

});

ipcMain.on("run-python-time", () => {

    const python = spawn("python", [
        "D:/Languages_Project/Languages_Project/countdown_timer.py"
    ]);

    python.stdout.on("data", (data) => {
        console.log(`Python: ${data}`);
    });

    python.stderr.on("data", (data) => {
        console.error(`Python error: ${data}`);
    });

});


app.whenReady().then(() => {
    createWindow();
});