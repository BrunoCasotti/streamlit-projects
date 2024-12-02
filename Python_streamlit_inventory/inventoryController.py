import bd;

def update_inventory(id, available):
    command = f'''UPDATE product
                SET available={available}
                WHERE id_product = {id}'''
    bd.cursor.execute(command)
    bd.connection.commit()