A batch decryption script for the files of The Coffin of Andy and Leyley (for versions 3.0.0 and higher (was tested on v3.0.2)).

It will process all encrypted `.png`, `.json`, and `.ogg` files in the directory and save them to a new folder. It will not attempt to decrypt any files that are not encrypted.

You must provide your own copy of the game.

This tool is highly influenced by [Grimoire](https://codeberg.org/basil/grimoire).

### Usage

Run script from the command line. By default, script will only check the `audio`, `data`, and `img` folders in the `www/` directory. The filenames of all encrypted files must be unchanged.

Python 3.2+ is required.

Arguments:

`inputDirectory`: Specify directory of game.

`outputDirectory`: Specify the output directory. You must pass both arguments at once.

Example:

```
python decryptor_v3.py inputDirectory outputDirectory
```
