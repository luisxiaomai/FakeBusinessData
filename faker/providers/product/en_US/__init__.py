from __future__ import unicode_literals
from .. import Provider as ProductProvider


class Provider(ProductProvider):
    
    products_name = []
    for i in range(0,500):
        products_name.append("Nike Air Force Mid %s Leather"%i)
        products_name.append("Nike AIR MAX %s SE"%i)
        products_name.append("Nike AIR ZOOM HYPERACE %s"%i)
        products_name.append("Nike AIR VAPORMAX FLYKNIT %s"%i)
        products_name.append("Nike AIR ZOOM HYPERACE %s"%i)
        products_name.append("Nike Classic Cortez %s Nylon"%i)
        products_name.append("Nike LunarEpic Low Flyknit %s"%i)
        products_name.append("Adidas X%s REIGNING CHAMP PUREBOOST SHOES"%i)
        products_name.append("Adidas CAMPUS SHOES %s"%i)
        products_name.append("Adidas TREFOIL TEE %s"%i)
        products_name.append("Adidas EQT PDX HOODIE %s"%i)
        products_name.append("Adidas EQT RAIN JACKET %s"%i)
        products_name.append("Adidas EQT BLOCKED CREW SWEATSHIRT %s"%i)
        products_name.append("Adidas XBYO CREW SWEATSHIRT %s"%i)
        products_name.append("Reebok HARMONY ROAD %s"%i)
        products_name.append("Reebok FLOATRIDE RUN %s"%i)
        products_name.append("Reebok PUMP SUPREME BLACK %s"%i)
        products_name.append("ASICS DynaFlyte %s"%i)
        products_name.append("ASICS GEL KENUN %s"%i)
        products_name.append("ASICS GEL DS TRAINER %s"%i)
        products_name.append("New Balance Women V%s Running Shoes"%i)
        products_name.append("New Balance Men V%s Strobe Running Shoes"%i)
        products_name.append("New Balance Women V%s Leather Sneakers"%i)
        products_name.append("Converse Men Leather Casual Sneakers %s"%i)
        products_name.append("Converse Men Kolin Free Leather Boat Shoes %s"%i)
        products_name.append("Converse Men Leather Formal Shoes %s"%i)


    uomFormats = ["bundle", "bag", "pair", "set", "roll", "bottle", "piece" ,"box", "pack", "dozen","kilogram", "carton", "gram", "kilo", "liter", "milliliter","litre", "each" ]

