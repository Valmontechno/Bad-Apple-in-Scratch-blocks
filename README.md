# Bad Apple but in Scratch blocks

[Scratch](https://scratch.mit.edu/projects/1205532741/) is a high-level, block-based visual programming language.
This project displays the [Bad Apple](https://youtu.be/FtutLA63Cp8) video not with scratch language but in the scratch code editor.

[See on Youtube](https://youtu.be/itOdqbtWkas)

<img height="300" src="https://github.com/user-attachments/assets/27ac9814-4197-4a1c-8532-291447202681" />

### Instructions

This project cannot be run directly with Scratch, but with TurboWarp which is an optimized version. <br>
https://turbowarp.org/1205532741/editor

Maximise the code editor with the button above the scene and zoom out the view as far as possible. Press space to start.

For better rendering, switch the editor to dark mode and set the block color to black in the [addon settings](https://turbowarp.org/addons#editor-theme3).

### Functioning

When a scratch block is running it appears highlighted, this project uses this phenomenon to display a video on a row of blocks that constitute the pixels. A scratch script read the video frames stored in a list and take care of calling and deactivating each pixel block.

The [converter.py](converter.py) script takes the original video, extracts the pixels to be displayed, and stores them in a file that can be imported as a list into scratch.

The [edit scratch json.js](edit%20scratch%20json.js) script allow to edit the sb3 scratch save file to place all the pixel blocs.
