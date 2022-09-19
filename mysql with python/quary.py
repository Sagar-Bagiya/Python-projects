import mysql.connector as connector

class dbhelper:
    def __init__(self):
        self.mydb = connector.connect(host='localhost',
                                      port='3306',
                                      user='root',
                                      password='Jarvis@123#',
                                      database='jarvis')

    # creat tabale
    def creat_table(self):
        quary = 'create table if not exists user(user_id int primary key,user_name varchar(200),phon varchar(12))'
        cursor = self.mydb.cursor()
        cursor.execute(quary)
        print("table created")

    # insert data
    def insert_data(self, userid, username, phon):
        quary = "insert into user(user_id,user_name,phon) values({},'{}','{}')".format(userid,username,phon)
        print(quary)
        cur = self.mydb.cursor()
        cur.execute(quary)
        self.mydb.commit()
        print("user data saved successfully!")

    def fatch_all(self):
        quary = "select * from user"
        cur = self.mydb.cursor()
        cur.execute(quary)
        for data in cur:
            print("user id is:{}\nuser name is:{}\nuser phon number is:{}\n\n".format(data[0],data[1],data[2]))

    # fatch one
    def fatch_one(self, userid):
        quary = "select * from user where user_id={}".format(userid)
        cur = self.mydb.cursor()
        cur.execute(quary)
        for data in cur:
            print(data)

    def delete_data(self, userid):
        quary = "delete from user where user_id={}".format(userid)
        cur = self.mydb.cursor()
        cur.execute(quary)
        self.mydb.commit()
        print("delet data su..")

helper = dbhelper()
# helper.delete_data(13)
helper.fatch_all()