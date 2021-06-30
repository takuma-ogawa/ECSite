from ClothesShopping.app.models import Product


def product_edit(new_products):
    for update_product in new_products:
        product = Product.objects.get(id=update_product["id"])
        product.price = update_product["price"]
        product.product_name = update_product["product_name"]
        product.save()
    return True

