#!/usr/bin/env python3

import psycopg2


class Log:
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as e:
            print(e)

    def get_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def print_result(self, task, query, suffix='views'):
        result = self.get_query(query)
        print(task)
        for i in range(len(result)):
            print(i + 1, '.', result[i][0], '-', result[i][1], suffix)

    def exit(self):
        self.db.close()


# First Task
task_1 = 'Q 1. What are the most popular three articles of all time?'
query_1 = ("""SELECT title, count(path) FROM articles, log
                WHERE status LIKE '200%'
                AND  CONCAT('/article/', articles.slug) = log.path
                GROUP BY title
                ORDER BY count(path) DESC
                LIMIT 3
                """)
# Second Task
task_2 = 'Q 2. Who are the most popular article authors of all time?'
query_2 = ("""SELECT authors.name, COUNT(*)
                FROM articles INNER JOIN authors ON articles.author=authors.id
                INNER JOIN log ON CONCAT('/article/', articles.slug)=log.path
                WHERE  log.status LIKE '200%'
                GROUP BY authors.name
                ORDER BY COUNT(log.path) DESC
                """)
# Third Task
task_3 = 'Q 3. On which days did more than 1% of requests lead to errors?'
query_3 = (("""SELECT to_char(date, 'Mon DD, YYYY') as date, rate
                FROM (select date(time) as date,
                round(cast(100*sum(CASE WHEN status!='200 OK' THEN 1
                ELSE 0
                END)::float/sum(CASE
                WHEN status!='%404%' THEN 1
                ELSE 0
                END) AS numeric), 2) AS rate
                FROM log
                GROUP BY date) AS err
                WHERE rate>1
                """))

# Result and print out
if __name__ == '__main__':
    log = Log()
    print("-" * 60)
    log.print_result(task_1, query_1)
    print("-" * 60)
    log.print_result(task_2, query_2)
    print("-" * 60)
    log.print_result(task_3, query_3, '% error')
    print("-" * 60)
    log.exit()
