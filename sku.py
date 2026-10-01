from pyscript import document

def generate_sku(event):

    category = document.querySelector("#category").value  
    product_name = document.querySelector("#product_name").value 
    stock_text = document.querySelector("#stock_quantity").value  

    # Makes sure all fields are filled in 
    if product_name == "" or stock_text == "":
        document.querySelector("#result").innerText = "Please fill in all fields."
        return

    stock_quantity = int(stock_text)  

    product_code = product_name[:3].upper()  
    category_code = category.upper()  

    # Combine category, product name, and stock quantity into one SKU
    sku = category_code + product_code + str(stock_quantity)
    
    # Replace the result box with only the current SKU (no history kept)
    document.querySelector("#result").innerHTML = f"""
        Category: {category_code}<br>
        Product: {product_name}<br>
        Stock Quantity: {stock_quantity}<br><br>
        SKU: {sku}
    """