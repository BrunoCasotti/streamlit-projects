import bd;

def insert_product(name, sku, price, category):
    
    command = f'''INSERT INTO product (name, sku, price, category, available)  
                 VALUES ("{name}","{sku}",{price},"{category}",0)'''
    bd.cursor.execute(command)
    bd.connection.commit()

def read_all_products():

    command = "SELECT * FROM product"
    bd.cursor.execute(command)
    result = bd.cursor.fetchall()
    return result

def read_product_by_id(id):

    command = f"SELECT * FROM product WHERE id_product = {id}"
    bd.cursor.execute(command)
    result = bd.cursor.fetchall()
    return result

def read_column_products():
    
    command = '''SELECT 
                CASE 
                    WHEN COLUMN_NAME = "id_product"
                    THEN "id"
                    ELSE COLUMN_NAME
                END AS COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = 'product' AND TABLE_SCHEMA = 'estoque_crud' '''
    bd.cursor.execute(command)
    result = bd.cursor.fetchall()
    column_names = [row[0] for row in result]
    return column_names

def delete_product(id):

    command = f"DELETE FROM product WHERE id_product = {id}"
    bd.cursor.execute(command)
    bd.connection.commit()

def update_product(id, name, sku, price, category):
    command = f'''UPDATE product
                SET name = "{name}", sku = "{sku}", price={price}, category="{category}"
                WHERE id_product = {id}'''
    bd.cursor.execute(command)
    bd.connection.commit()