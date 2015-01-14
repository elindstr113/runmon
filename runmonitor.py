#!/usr/bin/python2.7

###################################################################
# Author:      Eric Lindstrom
# Date:        Spring 2014
# Description: Utility to check the number of miles I've run for a
#              given day, month, year. Also, breaks down miles per
#              year. Additionally, displays a rolling 7 days worth
#              of log entries.
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
