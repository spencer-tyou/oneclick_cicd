# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymysql as pymysql


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def generate_prime():
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


# SQL connector class
class DBConnector:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                          db=self.db)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
