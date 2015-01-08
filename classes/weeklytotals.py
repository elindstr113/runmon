import MySQLdb
import netrc


class WeeklyTotals:
    """This class gets running totals for the week,
    month, year, and grand total, and returns it as a list.
    """

    @staticmethod
    def GetWeeklyTotals():

        secrets = netrc.netrc()
        user, account, pwd = secrets.authenticators("getfit")
        dbConn = MySQLdb.connect(host="lindstrom.hopto.org",
                                 user=user,
                                 passwd=pwd,
                                 db="GetFit",
                                 port=25564)
        dbCursor = dbConn.cursor()
        selectCommand = "CALL usp_CheckGoals"
        dbCursor.execute(selectCommand)
        dbRow = dbCursor.fetchone()
        wtdMiles, mtdMiles, ytdMiles, totalMiles = dbRow
        dbCursor.close()
        dbYearCursor = dbConn.cursor()
        dbYearCursor.execute("CALL usp_GetYearBreakdown")
        dbYearSummary = dbYearCursor.fetchall()
        dbYearCursor.close()
        dbConn.close()
        results = []
        results.append("\n      Running Totals")
        results.append("=" * 23)
        numberFormat = "{:16,.2f}"
        if (wtdMiles):
            results.append(("Week : " + numberFormat).format(wtdMiles))
        if (mtdMiles):
            results.append(("Month: " + numberFormat).format(mtdMiles))
        if (ytdMiles):
            results.append(("Year : " + numberFormat).format(ytdMiles))
        if (dbYearSummary):
            results.append("\n   Breakdown By Year")
            results.append("=" * 23)
            numberFormat = "{:18,.2f}"
            for dbRow in dbYearSummary:
                results.append((str(dbRow[0]) + ":" +
                                numberFormat).format(dbRow[1]))
        results.append("-" * 23)
        if (totalMiles):
            results.append(("Total: " + "{:16,.2f}").format(totalMiles))
        return results
