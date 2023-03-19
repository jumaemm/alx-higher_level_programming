#!/usr/bin/python3

"""
Use joins to display dta from two tables
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` INNER JOIN `states` as `s`\
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in cur.fetchall()]
    cur.close()
    db.close()
