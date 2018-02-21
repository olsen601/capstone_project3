import sqlite3, db_manipulation

global salesDB
global cur

def db_setup():

    '''Creates tables if they don't exist and creates cursor'''

    global salesDB
    global cur

    salesDB = sqlite3.connect('Project3_version2/sales.db')

    cur = salesDB.cursor()

    cur.execute('create table if not exists events (event_id integer primary key, name text, location text, date text)')
    cur.execute('create table if not exists merchandise (merch_id integer primary key, merch_name text, cost real)')
    cur.execute('create table if not exists records (event_id integer not null, merch_id integer not null, sold int, foreign key(event_id) references events(event_id), foreign key(merch_id) references merchandise(merch_id), unique(event_id, merch_id))')

    salesDB.commit();


def db_get_data(table):

    '''Retrieves table data based on the table parameter'''

    global salesDB
    global cur

    data_list = cur.execute('select * from '+table).fetchall()

    if data_list != []:
        return data_list
    else:
        return None


def db_get_event_search_data(term):

    '''Querys events table for items that contains name like the term parameter'''

    global salesDB
    global cur

    data_list = cur.execute('select * from events where name like ?', (term,)).fetchall()

    if data_list != []:
        return data_list
    else:
        return None

def db_get_merchandise_serch_data(term):

    '''Querys merchandise table for items that contains merch_name like the term parameter'''

    global salesDB
    global cur

    data_list = cur.execute('select * from merchandise where merch_name like ?', (term,)).fetchall()

    if data_list != []:
        return data_list
    else:
        return None


def db_get_records():

    '''Querys to replace event_id with name and merch_id with merch_name to display each record'''

    global salesDB
    global cur

    record_list = cur.execute('select e.name, m.merch_name, r.sold from records r INNER JOIN events e ON r.event_id = e.event_id INNER JOIN merchandise m ON r.merch_id = m.merch_id ORDER BY e.name ASC, m.merch_name ASC').fetchall()

    if record_list != []:
        return record_list
    else:
        return None


def db_high_records():

    '''Same as db_get_records but displays in order of most sold'''

    global salesDB
    global cur

    record_list = cur.execute('select e.name, m.merch_name, r.sold from records r INNER JOIN events e ON r.event_id = e.event_id INNER JOIN merchandise m ON r.merch_id = m.merch_id ORDER BY r.sold DESC').fetchall()

    if record_list != []:
        return record_list
    else:
        return None


def db_total_sales_records():

    '''Querys event name, merchandise merch_name, records sold and merchandise cost then multiplies the cost by the number sold and rounds to the second decimal place'''

    global salesDB
    global cur

    record_list = cur.execute('select e.name, m.merch_name, round((r.sold * m.cost), 2) from records r INNER JOIN events e ON r.event_id = e.event_id INNER JOIN merchandise m ON r.merch_id = m.merch_id ORDER BY 3 DESC')

    if record_list != []:
        return record_list
    else:
        return None


def db_total_merch_sales_records():

    '''Querys merch_name and then finds the net sales of the product'''

    global salesDB
    global cur

    record_list = cur.execute('select m.merch_name, round(total(r.sold * m.cost), 2) from records r INNER JOIN merchandise m ON r.merch_id = m.merch_id GROUP BY m.merch_name ORDER BY 2 DESC')

    if record_list != []:
        return record_list
    else:
        return None


def db_total_events_sales_records():

    '''Querys for event names and net sales of those events'''

    global salesDB
    global cur

    record_list = cur.execute('select e.name, round(total(r.sold * m.cost), 2) from records r INNER JOIN events e ON r.event_id = e.event_id INNER JOIN merchandise m ON r.merch_id = m.merch_id GROUP BY e.name ORDER BY 2 DESC')

    if record_list != []:
        return record_list
    else:
        return None


def db_shutdown():

    '''Currently not used but might be necessary for more advanced error handling'''

    global salesDB

    salesDB.commit()
