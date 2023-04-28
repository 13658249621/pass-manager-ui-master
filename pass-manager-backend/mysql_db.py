import pymysql
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')
# the configuration message for mysql server
host = config['mysql']['host']
port = config['mysql']['port']
user = config['mysql']['user']
password = config['mysql']['password']
database = config['mysql']['database']


def connect():
    return pymysql.connect(host=host,
                           port=int(port),
                           user=user,
                           password=password,
                           database=database)


def deleteById(table_name, id):
    conn = connect()
    conn.ping(reconnect=True)
    cursor = conn.cursor()
    sql = "DELETE FROM %s WHERE id = %d" % (table_name, id)
    print(sql)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()


class Dao:
    pass


class AccountDAO:
    """Account Dao Class,  Encapsulates operations on the account table"""

    # table name
    tablename = 't_account'

    # columns one list in db
    columns1 = "info, nickname, account, password, website, bind_email, bind_phone, `create_time`, `update_time`, comment"
    # columns two list in db
    columns2 = "id, " + columns1
    # columns three list in db
    columns3 = "info, nickname, account, password, website, bind_email, bind_phone, comment"

    def insert(self, account):
        conn = connect()
        conn.ping(reconnect=True)
        cursor = conn.cursor()
        sql = """INSERT INTO {0} ({1}) 
                    VALUES('{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}');
        """.format(self.tablename, self.columns3,
                   account['info'], account['nickname'], account['account'], account['password'],
                   account['website'], account['bind_email'], account['bind_phone'], account['comment'])
        sql = sql.replace("'None'", "null")
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

    def update(self, account):
        conn = connect();
        conn.ping(reconnect=True)
        cursor = conn.cursor()

        eneity = self.selectById(account['id'])[0]
        import datetime
        account['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") if eneity['password'] != account[
            'password'] else eneity['update_time']

        # SQL 更新语句
        sql = """ update {} 
        set info = '{}',nickname= '{}', account='{}', password='{}', website='{}', bind_email='{}', bind_phone= '{}', update_time='{}', comment='{}'
        where id  = {}
        """.format(self.tablename,
                   account['info'], account['nickname'], account['account'], account['password'],
                   account['website'], account['bind_email'], account['bind_phone'], account['update_time'],
                   account['comment'],
                   account['id'])
        sql = sql.replace("'None'", "null")
        print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 发生错误时回滚
            conn.rollback()

    def selectPage(self, limit, offset, q=''):
        sql = """SELECT {}
            FROM {} where info like '%{}%' or comment like '%{}%'
            limit {}, {}""".format(self.columns2, self.tablename, q, q, limit, offset)
        return self.executeSelectSql(sql)

    def count(self, q=''):
        sql = """select count(1)
        FROM {} where info like '%{}%' or comment like '%{}%'
        """.format(self.tablename, q, q)
        print(sql)
        conn = connect();
        conn.ping(reconnect=True)
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        return int(results[0][0])

    def selectAll(self):
        sql = """SELECT {}
            FROM {}
            """.format(self.columns2, self.tablename)
        return self.executeSelectSql(sql)

    def selectById(self, id):
        sql = """SELECT {}
            FROM {} 
            where id = {}
            """.format(self.columns2, self.tablename, id)
        return self.executeSelectSql(sql)

    # 执行查询的 sql
    def executeSelectSql(self, sql):
        print(sql)
        conn = connect();
        conn.ping(reconnect=True)
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        resultsList = []
        for i in results:
            resultsList.append({
                'id': str(i[0]),
                'info': str(i[1]),
                'nickname': str(i[2]),
                'account': str(i[3]),
                'password': str(i[4]),
                'website': str(i[5]),
                'bind_email': str(i[6]),
                'bind_phone': str(i[7]),
                'create_time': str(i[8]),
                'update_time': str(i[9]),
                'comment': str(i[10])
            })
        cursor.close()
        conn.close()

        return resultsList

    def deleteById(self, id):
        deleteById(self.tablename, id)


class EmailDao:
    """Email Dao Class, Encapsulates operations on the "email" table"""
    table_name = "t_email"

    columns1 = "create_time, update_time, email_name, account, password, website, comment"
    columns2 = "id, " + columns1
    columns3 = "email_name, account, password, website, comment"   # 用于插入和更新
    def list(self):
        sql = """SELECT {} FROM {};""".format(self.columns2, self.table_name)
        print(sql)
        conn = connect()
        conn.ping(reconnect=True)
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        resultsList = []
        for i in results:
            resultsList.append({
                'id': str(i[0]),
                'create_time': str(i[1]),
                'update_time': str(i[2]),
                'email_name': str(i[3]),
                'account': str(i[4]),
                'password': str(i[5]),
                'website': str(i[6]),
                'comment': str(i[7])
            })
        cursor.close()
        conn.close()
        return resultsList

    def insert(self, email):
        conn = connect()
        conn.ping(reconnect=True)
        cursor = conn.cursor()
        sql = """
                INSERT INTO {0} ({1}) VALUES('{2}', '{3}', '{4}', '{5}', '{6}');
                """.format(self.table_name, self.columns3, email['email_name'], email['account'], email['password'],
                           email['website'], email['comment'])
        sql = sql.replace("'None'", "null")
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

    def deleteById(self, id):
        deleteById(self.table_name, id)


class PhoneDao:
    """Phone Dao Class, Encapsulates operations on the "phone" table"""
    table_name = "t_phone"
    columns1 = "create_time, update_time, `type`, account, comment"
    columns2 = "id, " + columns1
    columns3 = "`type`, account, comment"

    def insert(self, phone):
        conn = connect()
        conn.ping(reconnect=True)
        cursor = conn.cursor()
        sql = """
                    INSERT INTO {0} ({1}) VALUES('{2}', '{3}', '{4}');
                """.format(self.table_name, self.columns3, phone['type'], phone['account'], phone['comment'])
        sql = sql.replace("'None'", "null")
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

    def list(self):
        sql = """SELECT {} FROM {};""".format(self.columns2, self.table_name)
        print(sql)
        conn = connect()
        conn.ping(reconnect=True)
        # 使用cursor()方法获取操作游标
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        resultsList = []
        for i in results:
            resultsList.append({
                'id': str(i[0]),
                'create_time': str(i[1]),
                'update_time': str(i[2]),
                'type': str(i[3]),
                'account': str(i[4]),
                'comment': str(i[5])
            })
        cursor.close()
        conn.close()
        return resultsList

    def deleteById(self, id):
        deleteById(self.table_name, id)
