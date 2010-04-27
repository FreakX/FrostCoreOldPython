class logon(object):
    def connect_db(self):
        import MySQLdb
        mysql_opts = {
                'host': frostlib.MYSQL_ACCOUNT_HOST,
                'user': frostlib.MYSQL_ACCOUNT_USER,
                'pass': frostlib.MYSQL_ACCOUNT_PW,
                'db':   frostlib.MYSQL_ACCOUNT_DB
                }
        try:
            self.mysql = MySQLdb.connect(mysql_opts['host'], mysql_opts['user'], mysql_opts['pass'], mysql_opts['db']) 
            self.mysql.apilevel = "2.0"
            self.mysql.threadsafety = 2
            self.mysql.paramstyle = "format"
            self.cursor = self.mysql.cursor()
        except:
            import traceback
            traceback.print_exc(file=frostlib.logfile)
            frostlib.nout("No Connection to MySQL Server")
            frostlib.shutdown()


    def check_user(self, username):
        sql = "SELECT * FROM accounts WHERE user = '" + str(username) + "'"
        resultcount = int(self.cursor.execute(sql))
        result = self.cursor_fetchall()
        if resultcount == 1 :
            return result[0]
        else:
            return None

    
        
