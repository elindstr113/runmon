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
        if (totalMiles):
            results.append(("Total: " + numberFormat).format(totalMiles))

        return results
