import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    number_of_directories, number_of_files = 0, 0
    for dirpath, dirnames, filenames in os.walk(directory):
        number_of_directories += len(dirnames)
        number_of_files += len(filenames)
    return((number_of_directories, number_of_files))
