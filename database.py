import sqlite3
connection = sqlite3.connect('shop')
cursorObj = connection.cursor()

sql = "CREATE TABLE products (ID INTEGER PRIMARY KEY AUTOINCREMENT,Brand TEXT, Model TEXT, Description TEXT)"
cursorObj.execute(sql)

values = [['Tecno','W2','smartphone with 4 inch display 2MP front camera and 4Mp rear camera'],
         ['Samsung','S8',"great user exprience"],
         ['Tecno','J8','stunnig audio']]
sql = "INSERT INTO products (Brand, Model, Description) VALUES ('tecno','W2','smartphone with 4 inch display 2MP front camera and 4Mp rear camera')"
cursorObj.execute(sql)


sql = "INSERT INTO products (Brand, Model, Description) VALUES ('samsung','S8','great user exprience')"
cursorObj.execute(sql)


sql = "INSERT INTO products (Brand, Model, Description) VALUES ( 'tecno','J8','stunnig audio')"
cursorObj.execute(sql)


cursorObj.execute('select Brand, Model, Description from products')
for records in cursorObj.fetchall():
    print(records)
connection.commit()
cursorObj.close()

