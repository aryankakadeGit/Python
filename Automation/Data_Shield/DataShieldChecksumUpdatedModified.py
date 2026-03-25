# Commandline Input Code
import sys
import os
import time
import shutil
import schedule
import hashlib

def CalculateChecksum(path):
    hobj = hashlib.md5()          # FIX: md5() object

    fobj = open(path, "rb")
    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()                  # FIX: proper close
    return hobj.hexdigest()


def BackupFiles(Source, Destination):
    copied_Files = []

    print("Creating a backup folder for backup processes")
    os.makedirs(Destination, exist_ok=True)

    for root, Dirs, Files in os.walk(Source):
        for file in Files:
            src_path = os.path.join(root, file)

            # Maintain directory structure
            relative_path = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative_path)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # FIX: correct function name
            print(CalculateChecksum(src_path))

            if ((not os.path.exists(dest_path)) or
                (CalculateChecksum(src_path) != CalculateChecksum(dest_path))):
                shutil.copy2(src_path, dest_path)
                copied_Files.append(relative_path)

    return copied_Files


def MarvellousDataShieldStart(Source="Data"):
    BackupName = "MarvellousBackup"
    print("Backup process started at :", time.ctime())

    Files = BackupFiles(Source, BackupName)

    print("Report about the backup")
    for name in Files:
        print(name)


def main():
    Border = "-" * 50
    print(Border)
    print("------ Marvellous Data Shield System ------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to :")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new updated files")
            print("3 : Create an archive of backup periodically")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as:")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : Time in minutes")
            print("SourceDirectory : Directory to backup")

        else:
            print("Unable to proceed, no such option")
            print("Use --h or --u")

    elif len(sys.argv) == 3:
        print("Inside Project Logic")
        print("Time Interval :", sys.argv[1])
        print("Directory Name :", sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(
            MarvellousDataShieldStart, sys.argv[2]
        )

        print("Data Shield System started successfully")
        print("Press CTRL + C to stop execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")

    print(Border)
    print("---------- Thank you for using our script ----------")
    print(Border)


if __name__ == "__main__":
    main()
