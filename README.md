# What is this project?
This is setup I made and used to make games for Pico-8 with Visual Studio Code, instead of their default editor.

# What is Pico 8?
>PICO-8 is a fantasy console for making, sharing and playing tiny games and other computer programs. It feels like a regular console, but runs on Windows / Mac / Linux. When you turn it on, the machine greets you with a commandline, a suite of cartridge creation tools, and an online cartridge browser called SPLORE.

# How to use
You'll need to use the picotools library: https://github.com/dansanderson/picotool

Setup:
1. Place compiler.py, export.py, pico8label.py, config.json and cproj.txt in a single folder.
2. Open config.json and enter all the necessary information. More info in the "Configuration" paragraph.

Create a new project:
1. Create a new folder in your projects directory. The name of the folder will be the name of your project.
2. Each .lua file you create in this directory will be added to the compiled cartrige.
3. To compile this new project, either run compiler.py with the parameter `-n {project name}`, or change cproj.txt to contain the name of your project. Use `-r` if you wish to run the cart after compiling.
4. After you run compiler.py for the first time, assets.p8 and final.p8 files will be created.
5. You can add a label.png to this project, and it would be added to cart while compiling.

# About the files
compiler.py - combines the assets from assets.p8 and the code in the given project to a single cart names "final.p8".
export.py - compiles a given project and exports it to HTML and JS.
pico8label.py - adds a custom label to a given cartrige file. if the project contains a label.png it uses it, otherwise uses the default label (from the config).
config.json - a JSON file that contains the paths for all the necessary folders and files.
cproj.txt - contains the name of the current project. compiler.py and export.py use it if no parameter is given.

# Configuration
Parameter | Description
--- | ---
project_path | Path to the folder that contains your projects (folders).
blank_cart_path | Path to a blank .p8 cartrige. I have provided one with this project. (If you want each new project to start with pre-made music, sprites, etc.. you cant change this blank cart). This should be a path to the file, not to a folder.
default_label_path | Path to the default label you want to give your projects. This should be a path to the file, not to a folder.
picotools_path | Path to the picotools folder.
pico_path | Path to the app's folder. Should be C:\Program Files (x86)\PICO-8\.
