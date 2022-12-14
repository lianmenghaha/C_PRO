from os import sep, listdir, mkdir, makedirs, error, rename, remove
from shutil import copyfile
import logging

class Build:
	
    def createDirIfNotExist(self, dirname, targetdir):
        files_and_dirs = listdir(targetdir)
        if dirname not in files_and_dirs:
            try:
                mkdir(targetdir + sep + dirname)
            #except error, value:
                #print value[1]
            except IOError as e:
                errno, strerror = e.args
                print("I/O error({0}): {1}".format(errno, strerror))
                # e can be printed directly without using .args:
                # print(e)

    def removeSpecialChars(self, text):
        specialChars = ['_', '-', '$', '.', ' ', '*', '']
        for char in specialChars:
            text = text.replace(char, '')
        return text

    def renameFile(self, currentname, newname, dir):
        dir = dir + sep
        if currentname != newname:
            try:
                rename(dir + currentname, dir + newname)
            #except error, value:
                #print value[1]
            except IOError as e:
                errno, strerror = e.args
                print("I/O error({0}): {1}".format(errno, strerror))
                # e can be printed directly without using .args:
                # print(e)

    def normalizeNameOfPdfs(self, pdfNames, toconvertdir):
        for name in pdfNames:
            if '.pdf' in name:
                newname = name.replace('.pdf', '')
                newname = self.removeSpecialChars(newname)
                newname = newname.upper() + '.pdf'
                self.renameFile(name, newname, toconvertdir)

    def cutFiles(self, currentpath, targetpath1, targetpath2):
        currentfiles = listdir(currentpath)
        for file in currentfiles:
            newpdfdir = file.replace('.pdf', '')
            newsvgdir = file.replace('.svg', '')
            oldlocation = currentpath + sep
            newlocation1 = targetpath1 + sep + newpdfdir + sep
            newlocation2 = targetpath2 + sep + newsvgdir + sep
            if '.pdf' in file:
                copyfile(oldlocation + file, newlocation1 + file)
                remove(oldlocation + file)
                logger = logging.getLogger('__main__')
                logger.info('pdf file %s are copied to %s.' % (file, newlocation1))

            if '.svg' in file:
                copyfile(oldlocation + file, newlocation2 + file)
                remove(oldlocation + file)
                logger = logging.getLogger('__main__')
                logger.info('svg file %s are copied to %s.' % (file, newlocation2))

    def createDirStructure(self, dirstructure):
        try:
            makedirs(dirstructure)
        #except error, value:
            #value[1]
        except IOError as e:
            errno, strerror = e.args
            print("I/O error({0}): {1}".format(errno, strerror))
            # e can be printed directly without using .args:
            # print(e)
