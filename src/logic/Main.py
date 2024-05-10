import os

from Extractor import Extractor


def get_file_paths():
    names = []
    filepaths = []
    final_path = os.path.join(os.path.dirname(__file__), '..', '..', 'input')
    w = os.walk(final_path)
    for (dirPath, dirNames, fileNames) in w:
        for fileName in fileNames:
            if fileName.endswith(".java"):
                names.append(fileName)
                filepaths.append(dirPath)
    return names, filepaths


if __name__ == "__main__":
    executor = Extractor(get_file_paths())
    executor.extract()
