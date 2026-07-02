var fso = new ActiveXObject("Scripting.FileSystemObject");
var f = fso.OpenTextFile("c:\\Users\\BMTF\\.antigravity\\testpaper\\data.js", 1);
var content = f.ReadAll();
f.Close();

try {
    eval(content);
    WScript.Echo("Syntax OK");
} catch(e) {
    WScript.Echo("Syntax Error:");
    WScript.Echo(e.name + ": " + e.message);
    WScript.Echo("Line: " + (e.line || "unknown"));
}
