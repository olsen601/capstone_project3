import sqlite3, db_store


def add(table, data):

    merch_id = db_store.cur.execute('select max(rowid) from merchandise').fetchone()[0]
    event_id = db_store.cur.execute('select max(rowid) from events').fetchone()[0]

    if table == "merchandise":
        if merch_id != None:
            merch_id += 1
        else:
            merch_id = 1
        db_store.cur.execute('insert into merchandise values (?, ?, ?)', (merch_id, data[0], data[1]))
    elif table == "events":
        if event_id != None:
            event_id += 1
        else:
            event_id = 1
        db_store.cur.execute('insert into events values (?, ?, ?, ?)', (event_id, data[0], data[1], data[2]))
    db_store.salesDB.commit()

    if event_id != 0 and merch_id != 0:
        merch = db_store.cur.execute('select merch_id from merchandise').fetchall()
        events = db_store.cur.execute('select event_id from events').fetchall()
        for event in events:
            event = (str(event)).replace("(", "").replace(",)", "")
            for m in merch:
                m = (str(m)).replace("(", "").replace(",)", "")
                db_store.cur.execute('insert or ignore into records values (?, ?, ?)', (event, m, 0))
                db_store.salesDB.commit()


def edit_update(table, edit_id, data):

    if table == "merchandise":
        db_store.cur.execute('update merchandise set merch_name=?, cost=? where merch_id = ?', (data[0], data[1], edit_id))
    elif table == "events":
        db_store.cur.execute('update events set name=?, location=?, date=? where event_id = ?', (data[0], data[1], data[2], edit_id))
    db_store.salesDB.commit()


def delete(table, delete_id):

    if table == "merchandise":
        db_store.cur.execute('delete from merchandise where merch_id=?', (delete_id,))
        db_store.cur.execute('delete from records where merch_id=?', (delete_id,))
    elif table == "events":
        db_store.cur.execute('delete from events where event_id=?', (delete_id,))
        db_store.cur.execute('delete from records where event_id=?', (delete_id,))
    db_store.salesDB.commit()


def update_record(record):
    # event, merch, sold
    e_id = db_store.cur.execute('select event_id from events where name like ?', (record[0],)).fetchone()[0]
    m_id = db_store.cur.execute('select merch_id from merchandise where merch_name like ?', (record[1],)).fetchone()[0]
    db_store.cur.execute('update records set sold = ? where event_id = ? and merch_id = ?', (record[2], e_id, m_id))
    db_store.salesDB.commit()
