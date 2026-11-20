# Folder Organizer

A small Python script that sorts the files in a folder into subfolders
(Images, Documents, Videos, Other) based on their extension(category type).

## Features

- Shows a clear message if folder does not exist
- Shows a clear message if the entered path is not for a folder
- Contains a dry run mode for a preview of what will be the output of the program on the chosen folder without actually moving any file
- Creates subfolders named after files categories
- Moves files based on categories to the subfolders
- Logs dry and actual runs in "organizer_log.txt"
- Skips files already exist in the destination, so nothing is overwritten 
- Counts the number of moved files and the skipped ones 

## How to run
1. Run:

```
python organizer.py
```
2. Type the folder path when asked, for example `D:\New folder\test_folder`

3. Type y for a dry run (preview only), or n to actually move the files.

## Sample output

Dry run mode:
```
Enter folder path. D:\New folder\test_folder
Dry run? (y/n): y
would move labala.pptx to D:\New folder\test_folder\Other\labala.pptx
would move letters.txt to D:\New folder\test_folder\Documents\letters.txt
Done, 2 would be moved, 0 would be skipped
```

Action mode:
```
Enter folder path. D:\New folder\test_folder
Dry run? (y/n): N
moved labala.pptx to D:\New folder\test_folder\Other\labala.pptx
moved letters.txt to D:\New folder\test_folder\Documents\letters.txt
Done, 2 moved, 0 skipped
```

If the written path is not for a folder:

```
Enter folder path. D:\New folder\test_folder\labala.pptx
Not a folder
```

If the folder is missing:

```
Enter folder path. labobo
Folder not found
```

## Categories

| Folder    | Extensions                |
|-----------|---------------------------|
| Images    | .jpg, .jpeg, .png, .gif   |
| Documents | .txt, .pdf, .docx         |
| Videos    | .mp4, .avi, .mkv          |
| Other     | everything else           |

## Notes

- The script moves actual files, so try the dry run first.
- Only the top level of the folder is processed (no subfolders).
- `organizer.py` and `organizer_log.txt` are never moved.
- If a file can't be moved (for example, it is open in another program), the script prints the reason, logs it as `failed`, and counts it as skipped.
- Skipped files are recorded only in the log, not printed on the screen.
- `organizer_log.txt` is created in the folder you run the script from.
hi iam here, have fun