from os import walk

import Executer


def main():
    executor = Executer.Executer(getFilePaths())
    executor.executeFiles()


def getFilePaths():
    names = []
    filepaths = []
    final_path = Executer.os.path.join(Executer.os.path.dirname(__file__), '..', '..', 'input')
    w = walk(final_path)
    for (dirPath, dirNames, fileNames) in w:
        for fileName in fileNames:
            if fileName.endswith(".java"):
                names.append(fileName)
                filepaths.append(dirPath)
    return names, filepaths


if __name__ == "__main__":
    main()
