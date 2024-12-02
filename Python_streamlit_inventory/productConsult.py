import streamlit as st;
import productController;
import pandas as pd;


columns = productController.read_column_products()

data = productController.read_all_products()

df_product = pd.DataFrame(
    data, columns=columns
)

st.header("Products", divider="gray")

with st.container(height=700, border=None):

    header_cols = st.columns((2, 3, 3, 2, 3, 2, 2, 2))

    # Renderizar os nomes das colunas no cabeçalho
    for col, header in zip(header_cols, columns):
        col.write(f"**{header}**")

    # Mostrar a tabela com botões para cada linha
    for i, row in df_product.iterrows():
        cols = st.columns((2, 3, 3, 2, 3, 2, 2, 2))
        cols[0].write(row["id"])
        cols[1].write(row["name"])
        cols[2].write(row["sku"])
        cols[3].write(f"${row['price']:.2f}")
        cols[4].write(row["category"])
        cols[5].write(row["available"])
        on_click_delete = cols[6].button("Delete", key=f"btn_delete_{row['id']}")
        on_click_update = cols[7].button("Update", key=f"btn_update_{row['id']}")

        if on_click_delete:
            productController.delete_product(row["id"])
            st.rerun()

        if on_click_update:
            session_id = st.session_state["id"] = row["id"]
            st.switch_page("productInsert.py")
