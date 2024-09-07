# Fallen Princess Knight CSV Editor for Blender

This project provides a custom Blender script to edit the save game data for the hentai game "Fallen Princess Knight" on Steam. The game stores its save data in a CSV file with no headers, and this script allows players to modify key values such as character stats, inventory, player position, and various game options. The tool uses Blender as the platform for editing due to its accessibility via Steam or the official Blender website.

## About the Game

"Fallen Princess Knight" is a hentai RPG game built in Unity. The game's save data is stored in a CSV file, which keeps track of various player attributes such as character stats, position, encounter rate, and more. The CSV file is updated dynamically as the game progresses, adding new values for enemies, inventory, and other in-game states.

The save data is located at:
C:\Users<your-username>\AppData\LocalLow\mico\FallenPrincessKnight_Steam\savedata.csv

This Blender script simplifies the process of editing the CSV save file.

## Features

- **Waypoint Selection**: Modify the player's location and direction based on pre-defined waypoints.
- **Player Stats**: Edit stamina, armor, cleanliness, and other character stats.
- **Inventory Management**: Adjust the amount of gold and other items.
- **Game Options**: Toggle pregnancy, childbirth, windowed mode, and more.
- **Experience and Stats**: Modify experience-related stats such as imprisonment, battle, and defeat stats.
- **Resolution and Graphics Quality**: Modify graphical settings such as resolution and quality directly from the CSV.

## Requirements

- **Blender**: This script requires Blender to function. Blender can be downloaded from the following sources:
    - [Blender Website](https://www.blender.org/download/)
    - [Blender on Steam](https://store.steampowered.com/app/365670/Blender/)

Once you have Blender installed, follow the instructions below to use the script.

## Installation and Usage

### 1. Install Blender
- If you don’t already have Blender, you can download it either from the [Blender Website](https://www.blender.org/download/) or via [Steam](https://store.steampowered.com/app/365670/Blender/).

### 2. Using the Script Directly in Blender

If you prefer not to install the script as an add-on, you can run the Python code directly from Blender's text editor:

1. Open Blender.
2. In the top menu, go to `Scripting`.
3. In the scripting workspace, click **New** to create a new script.
4. Copy and paste the Python script (`fpk_editor.py`) from this repository into the text editor.
5. Press **Run Script** to load the editor.
6. Switch back to the **3D Viewport**.
7. On the right-hand side, look for a tab named **FallenPrincessKnight** in the UI panel.
8. Click the **Load CSV** button to load your saved game data from the CSV file.
9. Modify the various fields such as player stats, location, or inventory by entering new values or selecting from the dropdown menus.
10. After making your desired changes, click **Save CSV** to write the changes back to the CSV file.

### 3. Installing as an Add-on (Optional)
If you prefer to install the script as an add-on in Blender, follow these steps:

1. Clone or download this repository to your local machine.
   - Click the green **Code** button, then **Download ZIP** or clone using `git`.
2. Open Blender.
3. In the top menu, go to `Edit` -> `Preferences`.
4. In the Preferences window, go to the **Add-ons** tab.
5. Click **Install** and select the Python script (`fpk_editor.py`) from the downloaded repository.
6. Once installed, check the box next to the add-on name to enable it.
7. Access the panel under **FallenPrincessKnight** in the UI panel as described in the previous method.

### 4. Customizing Waypoints and Stats
The script supports pre-defined waypoints such as "Goblin Camp", "Church", and more. When you select a waypoint from the dropdown, the position and direction are automatically updated based on the values defined in the script. You can also modify various player stats, including:
- **Stamina**
- **Armor**
- **Cleanliness**
- **Gold**

### 5. Game Options and Toggles
In addition to stats, you can also modify game options like:
- **Enable Pregnancy**: Toggle pregnancy mode.
- **Enable Child Birth**: Enable childbirth events.
- **Blizzard Effects**: Toggle blizzard visual effects.
- **Windowed Mode**: Switch between full-screen and windowed mode.

You can also change graphical settings such as **Resolution** and **Graphics Quality** directly from the panel.

## Contributing
Feel free to fork the repository and submit pull requests if you'd like to improve or extend the functionality of the script.

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
