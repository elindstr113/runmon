#!/usr/bin/python2.7

###################################################################
# Author:      Eric Lindstrom
# Date:        Spring 2013
# Description: Utility to check the WTD number of miles I've run
#              and save status in a text file. The text file is then
#              read in and displayed on the desktop using conky
##################################################################


import os
import sys
from classes.weeklytotals import WeeklyTotals
from classes.dailyruns import DailyRuns


def WriteOutputFile(fileName, listLines):
    if os.path.isfile(fileName):
        os.remove(fileName)

    outputFile = open(fileName, "w")
    outputFile.write("\n".join(listLines))
    outputFile.write("\n\n")
    outputFile.close()


def WriteToConsole(listLines):
    print("\n".join(listLines))
    print("\n\n")


def main(fileName):
    fileContents = []
    fileContents += WeeklyTotals.GetWeeklyTotals()
    fileContents.append("")
    fileContents += DailyRuns.GetDailyRuns()
    WriteOutputFile(fileName, fileContents)
    #WriteToConsole(fileContents)
    return True

if __name__ == '__main__':
    fileName = "/home/elindstr/rundump.txt"
    if (len(sys.argv) > 1):
        fileName = sys.argv[1]
    status = main(fileName)
    #sys.exit(status)
