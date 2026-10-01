from pyscript import document

def create_order(event):

    customer_name = document.querySelector("#customer_name").value  

    # Prices for each menu item
    matcha_price = 150
    spanish_price = 145
    vanilla_price = 135
    caramel_price = 140
    cheesecake_price = 160
    croissant_price = 120

    order_list = ""  
    total = 0  
    
    # Get quantities
    matcha_quantity = int(document.querySelector("#item1").value)
    spanish_quantity = int(document.querySelector("#item2").value)
    vanilla_quantity = int(document.querySelector("#item3").value)
    caramel_quantity = int(document.querySelector("#item4").value)
    cheesecake_quantity = int(document.querySelector("#item5").value)
    croissant_quantity = int(document.querySelector("#item6").value)

    # Matcha Latte
    if matcha_quantity > 0:
        subtotal = matcha_price * matcha_quantity
        order_list += f"Matcha Latte x {matcha_quantity} - ₱{subtotal}<br>"
        total += subtotal

    # Spanish Latte
    if spanish_quantity > 0:
        subtotal = spanish_price * spanish_quantity
        order_list += f"Spanish Latte x {spanish_quantity} - ₱{subtotal}<br>"
        total += subtotal

    # Vanilla Latte 
    if vanilla_quantity > 0:
        subtotal = vanilla_price * vanilla_quantity
        order_list += f"Vanilla Latte x {vanilla_quantity} - ₱{subtotal}<br>"
        total += subtotal

    # Caramel Latte
    if caramel_quantity > 0:
        subtotal = caramel_price * caramel_quantity
        order_list += f"Caramel Latte x {caramel_quantity} - ₱{subtotal}<br>"
        total += subtotal

    # Blueberry Cheesecake
    if cheesecake_quantity > 0:
        subtotal = cheesecake_price * cheesecake_quantity
        order_list += f"Blueberry Cheesecake x {cheesecake_quantity} - ₱{subtotal}<br>"
        total += subtotal

    # Chocolate Croissant
    if croissant_quantity > 0:
        subtotal = croissant_price * croissant_quantity
        order_list += f"Chocolate Croissant x {croissant_quantity} - ₱{subtotal}<br>"
        total += subtotal

    # Check if name is empty
    if customer_name == "":
        document.querySelector("#result").innerHTML = "Please enter your name."
        return

    # Check if no items were ordered
    if order_list == "":
        document.querySelector("#result").innerHTML = "Please order at least one item."
        return

    # Display receipt
    document.querySelector("#result").innerHTML = f"""
    Customer: {customer_name}<br><br>
    Order Details<br>
    {order_list}
    
    <br>
    Total: ₱{total}
    """