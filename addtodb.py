import json

# name = models.CharField(max_length=128)
# image = models.ImageField(upload_to='product_image', blank=True)
# description = models.TextField(blank=True, null=True)
# price = models.DecimalField(max_digits=8, decimal_places=2)
# quantity = models.PositiveIntegerField(default=0)
# category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

categories = [
    {
        "model": "mainapp.ProductCategory",
        "pk": 1,
        'fields': {'name': 'Новинки', 'description': 'Самые новые новинки'}
    },
    {
        "model": "mainapp.ProductCategory",
        "pk": 2,
        'fields': {'name': 'Одежда', 'description': 'Крутейшая одежда'}
    },
    {
        "model": "mainapp.ProductCategory",
        "pk": 3,
        'fields': {'name': 'Обувь', 'description': 'Только для суперменов'}
    },
    {
        "model": "mainapp.ProductCategory",
        "pk": 4,
        'fields': {'name': 'Аксессуары', 'description': 'Всё что нужно'}
    },
    {
        "model": "mainapp.ProductCategory",
        "pk": 5,
        'fields': {'name': 'Подарки', 'description': 'На все случаи жизни'}
    },
]

products = [
    {
        "model": "mainapp.Product",
        "pk": 1,
        'fields': {'name': 'Худи черного цвета с монограммами adidas Originals',
                   'price': 6090.00,
                   'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                   'image': 'product_image/Adidas-hoodie.png',
                   'category': 1}},
    {
        "model": "mainapp.Product",
        "pk": 2,
        'fields': {'name': 'Синяя куртка The North Face',
                   'price': 23725.00,
                   'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                   'image': 'product_image/Blue-jacket-The-North-Face.png',
                   'category': 2}},
    {
        "model": "mainapp.Product",
        "pk": 3,
        'fields': {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                   'price': 2890.00,
                   'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                   'image': 'product_image/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                   'category': 2}},
    {
        "model": "mainapp.Product",
        "pk": 4,
        'fields': {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                   'price': 13590.00,
                   'description': 'Гладкий кожаный верх. Натуральный материал.',
                   'image': 'product_image/Black-Dr-Martens-shoes.png',
                   'category': 3}},
    {
        "model": "mainapp.Product",
        "pk": 5,
        'fields': {'name': 'Черный рюкзак Nike Heritage',
                   'price': 2340.00,
                   'description': 'Плотная ткань. Легкий материал.',
                   'image': 'product_image/Black-Nike-Heritage-backpack.png',
                   'category': 4}},
    {
        "model": "mainapp.Product",
        "pk": 6,
        'fields': {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                   'price': 3390.00,
                   'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                   'image': 'product_image/Brown-sports-oversized-top-ASOS-DESIGN.png',
                   'category': 5}}
]

with open('mainapp/fixtures/categories.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, ensure_ascii=False)

with open('mainapp/fixtures/products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False)

# python manage.py loaddata categories.json
# python manage.py loaddata products.json
