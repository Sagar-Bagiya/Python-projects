import mysql.connector as connector

mydb = connector.connect(host='localhost',
                         port='3306',
                         user='root',
                         password='Jarvis@123#',
                         database='jarvis')


def jarvis_dict(question):
    quary = "select answer from jarvis_dict where question = '{}'".format(question)
    cur = mydb.cursor()
    cur.execute(quary)
    for row in cur:
        return row


def jarvis_remember(question):
    quary = "select answer from jarvis_dict where question = '{}'".format(question)
    cur = mydb.cursor()
    cur.execute(quary)


if __name__ == "__main__":
    jarvis_dict("what is your name ?")
