from pathlib import Path

search = input("Enter folder path. ")
folder = Path(search)
transfer_counter = 0
skipped_counter = 0 

if not folder.exists():
    print("Folder not found")
elif not folder.is_dir():
    print("Not a folder")
else:
    dry_run = input("Dry run? (y/n): ")
    while dry_run not in ["y", "Y", "n", "N"]:
        print("Please answer with only y, n, Y, N")
        dry_run = input("Dry run? (y/n): ")
    if dry_run in ["N", "n"]:
        for name in ["Images", "Documents", "Videos", "Other"]:
            (folder / name).mkdir(exist_ok=True)
    with open("organizer_log.txt", "a") as file:
        for files in folder.iterdir():
            suffix = files.suffix.lower()
            if not files.is_file():
                continue
            if files.name in [ "organizer.py", "organizer_log.txt"]:
                continue
            elif suffix in [".jpg", ".jpeg", ".png", ".gif"]:
                destination = folder / "Images" / files.name
            elif suffix in [".txt", ".pdf", ".docx"]:
                destination = folder / "Documents" / files.name
            elif suffix in [".mp4", ".avi", ".mkv"]:
                destination = folder / "Videos" / files.name
            else:
                destination = folder / "Other" / files.name

            if dry_run in ["Y", "y"]:
                if destination.exists():
                    file.write("DRY skipped " + files.name + "\n")
                    skipped_counter = skipped_counter + 1
                else:
                    file.write("DRY would move " + files.name + " to " + str(destination) + "\n")
                    print("would move " + files.name + " to " + str(destination))
                    transfer_counter = transfer_counter + 1
            else:
                if destination.exists():
                    file.write("skipped " + files.name + "\n")
                    skipped_counter = skipped_counter + 1
                else:
                    try:
                        files.rename(destination)
                        transfer_counter = transfer_counter + 1
                        file.write("moved " + files.name + " to " + str(destination) + "\n")
                        print("moved " + files.name + " to " + str(destination))
                    except OSError as error:
                        file.write("failed " + files.name + ": " + str(error) + "\n")
                        skipped_counter = skipped_counter + 1
                        print(files.name+" move process was unsuccessful "+"\n Reason: "+ str(error))
        if dry_run in ["Y", "y"]:
            print("Done,", transfer_counter, "would be moved,", skipped_counter, "would be skipped")
        else:   
            print("Done,", transfer_counter, "moved,", skipped_counter, "skipped")
