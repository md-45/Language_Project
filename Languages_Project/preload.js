const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("python", {
    run: () => ipcRenderer.send("run-python", "run-python-time")
});