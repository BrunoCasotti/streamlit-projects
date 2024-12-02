import streamlit as st;
import productController;
import time;

id_uptade = st.session_state.get("id", None)

id_recovered = None

if id_uptade is not None:
    st.header("Update", divider="gray")
    id_recovered = productController.read_product_by_id(id_uptade)[0][0]
else:
    st.header("Register", divider="gray")

with st.form(key="product_insert", clear_on_submit=True):

    list_category = ["keyboard", "mouse", "mousepad"]

    if id_recovered == None:
        input_name = st.text_input(label="Product name")
        input_sku = st.text_input(label="Product sku")
        input_price = st.number_input(label="Product price")
        input_category = st.selectbox(label="Product category",
                                    options=list_category,
                                    index=None,
                                    placeholder="Selecione a categoria")
    else:
        input_name = st.text_input(label="Product name", 
                                   value= productController.read_product_by_id(id_uptade)[0][1])
        input_sku = st.text_input(label="Product sku", 
                                  value= productController.read_product_by_id(id_uptade)[0][2])
        input_price = st.number_input(label="Product price", 
                                      value= productController.read_product_by_id(id_uptade)[0][3])
        input_category = st.selectbox(label="Product category",
                                    options=list_category,
                                    index=list_category.index(productController.read_product_by_id(id_uptade)[0][4]))
        
    input_button_submit = st.form_submit_button("Submit")


if input_button_submit:
    errors = []

    if not input_name.strip():
        errors.append("Product name is required.")
    if not input_sku.strip():
        errors.append("Product SKU is required.")
    if input_price <= 0:
        errors.append("Product price must be greater than 0.")
    if input_category == "Selecione a categoria":
        errors.append("Please select a valid product category.")

    if errors:
        for error in errors:
            st.error(error)
    else:
        if id_recovered == None:
            productController.insert_product(input_name,input_sku,input_price,input_category)
        else:
            productController.update_product(id_uptade,input_name,input_sku,input_price,input_category)
            st.success("Product submitted successfully!")
            st.session_state.clear()
            time.sleep(1)
            st.switch_page("productConsult.py")

        st.success("Product submitted successfully!")
        