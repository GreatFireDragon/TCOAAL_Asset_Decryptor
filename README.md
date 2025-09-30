# The Coffin of Andy and Leyley - Asset Decryptor (.exe)

This is a user-friendly, standalone executable for Windows that decrypts the game files for *The Coffin of Andy and Leyley*. It is designed for game versions 3.0.0 and higher (tested on v3.0.2).

The tool will automatically find and process all encrypted `.png`, `.json`, and `.ogg` files and save the decrypted versions to a new folder, making them accessible for viewing or modding.

**You must provide your own legitimate copy of the game.**

### How to Use

This tool is designed to be as simple as possible. No command line or Python installation is required.

1.  **Download** the `.exe` file.
- From [Releases](https://github.com/GreatFireDragon/TCOAAL_Asset_Decryptor/releases)
- Directly [TCOAAL.Asset.Decryptor.exe](https://github.com/GreatFireDragon/TCOAAL_Asset_Decryptor/releases/download/All/TCOAAL.Asset.Decryptor.exe)
2.  **Run the tool using one of the following methods:**
    *   **Automaticly (Recommended):** Simply place the `.exe` anywhere on your computer and double-click it. The program will automatically search your drives for the official Steam installation of the game.
    *   **Manualy:** If the game is installed in a non-standard location or is not from Steam, place the `.exe` file directly inside the game's main folder (the one containing the `Game.exe` and the `www` folder). Then, double-click the `.exe` to run it.
    Usually location is C:\Program Files (x86)\Steam\steamapps\common\The Coffin of Andy and Leyley
3.  **Find your files.** A new folder named `decrypted TCOAAL assets` will be created in the same directory where you ran the `.exe`. This folder contains all the decrypted game files, organized in their original structure.


### Credits

This tool was made possible by the work of several people in the community.

*   **Original Python Script:** Created by **AlternativeOne**. You can find the original project here: [github.com/AlternativeOne/tcoaal_decryptor](https://github.com/AlternativeOne/tcoaal_decryptor)
*   **Influential Work:** This tool is highly influenced by the work of **Basil & Phoni** on their TCOAAL tools, especially [Grimoire](https://codeberg.org/basil/grimoire).
*   **Executable Packaging:** Packaged into a standalone `.exe` by me (**GreatFireDragon**).
