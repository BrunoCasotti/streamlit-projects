import streamlit as st;
import productController;
import pandas as pd;
from streamlit_modal import Modal;
import inventoryController;

modal_inventory_manage = Modal(key="modal_inventory_manage", title="Manage Inventory")

columns = productController.read_column_products()

data = productController.read_all_products()

df_product = pd.DataFrame(
    data, columns=columns
)

st.header("Inventory", divider="gray")

with st.container(height=700, border=None):

    header_cols = st.columns((2, 3, 3, 2, 3, 2, 2))

    # Renderizar os nomes das colunas no cabeçalho
    for col, header in zip(header_cols, columns):
        col.write(f"**{header}**")

    # Mostrar a tabela com botões para cada linha
    for i, row in df_product.iterrows():
        cols = st.columns((2, 3, 3, 2, 3, 2, 2))
        cols[0].write(row["id"])
        cols[1].write(row["name"])
        cols[2].write(row["sku"])
        cols[3].write(f"${row['price']:.2f}")
        cols[4].write(row["category"])
        cols[5].write(row["available"])
        on_click_manage = cols[6].button("Menage", key=f"btn_menage_{row['id']}")

        if on_click_manage:

            st.session_state["id_product_row"] = row.to_dict()
            modal_inventory_manage.open()


# Modal - Renderizar fora do loop
if modal_inventory_manage.is_open():
    with modal_inventory_manage.container():
        # Recuperar a linha do produto
        id_product_row = st.session_state.get("id_product_row", {})
        if id_product_row:
            st.write("### Produto Selecionado")
            st.write(f"**Id:** {id_product_row.get('id')}")
            st.write(f"**Name:** {id_product_row.get('name')}")
            st.write(f"**Sku:** {id_product_row.get('sku')}")
            st.write(f"**Avaliable:** {id_product_row.get('available')}")

            # Opções para Adicionar ou Baixar Estoque
            operation = st.radio("Choose the operation", options=["Add", "Decrease"])
            quantity = st.number_input("Quantity", min_value=0, step=1, value=0)

            # Validação
            if operation and quantity >= 0:
                if st.button("Submit"):
                    if operation == "Add":
                        update_quatity = quantity + id_product_row.get('available')
                        inventoryController.update_inventory(id_product_row.get('id'),update_quatity)
                    elif operation == "Decrease":
                        if quantity > id_product_row.get("available"):
                            st.error("A quantidade a ser diminuída não pode ser maior do que o estoque disponível.")
                        else:
                            update_quatity = id_product_row.get('available') - quantity
                            inventoryController.update_inventory(id_product_row.get('id'),update_quatity)
                    modal_inventory_manage.close()
                    st.rerun()
            else:
                st.error("Fill in all the fields correctly!")