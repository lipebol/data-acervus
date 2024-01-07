from os import environ
import psycopg2

class database:
    def __init__(self):
        self.__connection = psycopg2.connect(
            user=environ.get("USERDB"), 
            password=environ.get("PWDDB"), 
            host=environ.get("HOSTDB"), 
            port=environ.get("PORTDB"), 
            database=environ.get("DB")
        )
        self.__db = self.__connection.cursor()

    def verify(self, uri):
        self.__uri = uri
        self.__db.execute(f"select link_job from jobs where link_job = '{self.__uri}'")
        return len(self.__db.fetchall())

    def insert(self, uri, company, namejob, datejob, typejob):
        self.__uri = uri
        self.__company = company
        self.__namejob = namejob
        self.__datejob = datejob
        self.__typejob = typejob
        self.__db.execute(
            f"""insert into jobs(link_job, company, name_job, date_job, type_job)
            values('{self.__uri}', '{self.__company}', '{self.__namejob}', 
            '{self.__datejob}', '{self.__typejob}')"""
        )
        self.__connection.commit()
        # self.__db.close()
        # self.__connection.close()
