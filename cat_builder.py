def cat_builder(name, color, toys):
    cat = {
        name: name,
        color: color,
        toys: toys
    }
    return cat

print(cat_builder('Bootsy', 'gray', 'ball of yarn and catnip'))