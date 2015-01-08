import MySQLdb
import datetime
import netrc


class DailyRuns(object):
    """description of class"""

    @staticmethod
    def GetDailyRuns():
        secrets = netrc.netrc()
        user, account, pwd = secrets.authenticators("getfit")
        dbConn = MySQLdb.connect(host="lindstrom.hopto.org",
                                 user=user,
                                 passwd=pwd,
                                 db="GetFit",
                                 port=25564)
        dbCursor = dbConn.cursor()
        selectCommand = ("CALL usp_GetDailyRuns")
        dbCursor.execute(selectCommand)
        dbRows = dbCursor.fetchall()
        dbCursor.close()
        dbConn.close()

        #wk is a list of dates for a week
        start = datetime.date.today() - datetime.timedelta(days=6)
        wk = [str(start + datetime.timedelta(days=i)) for i in range(7)]

        numberFormat = "{:6,.2f}"  # 6 characters wide, two decimal places
        weekTotal = 0
        results = ["\n     Rolling Week\n" + ("=" * 23)]
        for d in wk:
            data = [row for row in dbRows if row[0] == d]
            if (len(data)):
                date, miles, pace, activity = data[0]
                if activity == "Run":
                    results.append(date + numberFormat.format(miles) +
                                   "  " + pace[3:])
                if activity == "Exercise":
                    results.append(date + "  Exercise")
                weekTotal += miles
            else:
                results.append(d)
        results.append(("-" * 23) +
                       ("\n   Total: " + numberFormat).format(weekTotal))
        return results
