"""
Common Data

Shared constants used by all data generators.
"""

# ==========================================
# Indian Cities and States
# ==========================================

LOCATIONS = [
    ("Hyderabad", "Telangana"),
    ("Bengaluru", "Karnataka"),
    ("Chennai", "Tamil Nadu"),
    ("Mumbai", "Maharashtra"),
    ("Pune", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Kolkata", "West Bengal"),
    ("Visakhapatnam", "Andhra Pradesh"),
    ("Lucknow", "Uttar Pradesh"),
    ("Bhopal", "Madhya Pradesh"),
    ("Chandigarh", "Chandigarh"),
    ("Kochi", "Kerala"),
    ("Bhubaneswar", "Odisha"),
]

# ==========================================
# Product Categories
# ==========================================

CATEGORIES = [
    "Electronics",
    "Furniture",
    "Office Supplies",
    "Clothing",
    "Home & Kitchen",
    "Grocery",
    "Sports",
    "Beauty",
    "Toys",
    "Books",
    "Automotive",
    "Pet Supplies"
]

# ==========================================
# Product Brands
# ==========================================

BRANDS = [
    "Samsung",
    "Apple",
    "Sony",
    "LG",
    "Dell",
    "HP",
    "Lenovo",
    "Boat",
    "Nike",
    "Adidas",
    "Puma",
    "Philips",
    "Prestige",
    "Cello",
    "Godrej",
    "Whirlpool",
    "Bajaj",
    "Canon",
    "Logitech",
    "Tata"
]

# ==========================================
# Payment Methods
# ==========================================

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking",
    "Wallet"
]

# ==========================================
# Payment Status
# ==========================================

PAYMENT_STATUS = [
    "Paid",
    "Pending",
    "Failed"
]

# ==========================================
# Return Reasons
# ==========================================

RETURN_REASONS = [
    "Damaged",
    "Wrong Product",
    "Defective",
    "Late Delivery",
    "No Longer Needed"
]
# ==========================================
# Product Catalog
# ==========================================

PRODUCT_CATALOG = {
    "Electronics": [
        ("Samsung", "Galaxy S24"),
        ("Apple", "iPhone 16"),
        ("Sony", "WH-1000XM5 Headphones"),
        ("Dell", "Inspiron Laptop"),
        ("HP", "LaserJet Printer"),
        ("Lenovo", "ThinkPad Laptop"),
        ("Canon", "EOS Camera"),
        ("Logitech", "Wireless Mouse"),
    ],

    "Furniture": [
        ("Godrej", "Office Chair"),
        ("Godrej", "Study Table"),
        ("IKEA", "Bookshelf"),
        ("Nilkamal", "Plastic Chair"),
        ("Durian", "Executive Desk"),
    ],

    "Office Supplies": [
        ("Cello", "Notebook"),
        ("Cello", "Ball Pen"),
        ("Classmate", "Register"),
        ("Camlin", "Marker Set"),
        ("Faber-Castell", "Pencil Box"),
    ],

    "Clothing": [
        ("Nike", "Running T-Shirt"),
        ("Adidas", "Track Pants"),
        ("Puma", "Sports Jacket"),
        ("Levi's", "Jeans"),
        ("Allen Solly", "Formal Shirt"),
    ],

    "Home & Kitchen": [
        ("Prestige", "Pressure Cooker"),
        ("Prestige", "Mixer Grinder"),
        ("Philips", "Electric Kettle"),
        ("Bajaj", "Ceiling Fan"),
        ("Whirlpool", "Microwave Oven"),
    ],

    "Grocery": [
        ("Tata", "Salt"),
        ("Aashirvaad", "Atta"),
        ("Fortune", "Cooking Oil"),
        ("Amul", "Butter"),
        ("Nestle", "Coffee"),
    ],

    "Sports": [
        ("Nike", "Football"),
        ("Adidas", "Cricket Bat"),
        ("Yonex", "Badminton Racket"),
        ("Puma", "Gym Bag"),
    ],

    "Beauty": [
        ("Lakme", "Face Wash"),
        ("Nivea", "Body Lotion"),
        ("Dove", "Shampoo"),
        ("Mamaearth", "Face Cream"),
    ],

    "Toys": [
        ("LEGO", "Building Blocks"),
        ("Funskool", "Board Game"),
        ("Barbie", "Fashion Doll"),
        ("Hot Wheels", "Toy Car"),
    ],

    "Books": [
        ("Penguin", "Python Programming"),
        ("O'Reilly", "SQL Cookbook"),
        ("McGraw Hill", "Data Analytics"),
        ("Pearson", "Business Statistics"),
    ],

    "Automotive": [
        ("Bosch", "Car Battery"),
        ("Castrol", "Engine Oil"),
        ("Michelin", "Car Tyre"),
    ],

    "Pet Supplies": [
        ("Pedigree", "Dog Food"),
        ("Whiskas", "Cat Food"),
        ("Trixie", "Pet Toy"),
    ]
}
# ==========================================
# Retail Stores
# ==========================================

STORES = [
    ("Hyderabad Central", "Hyderabad", "Telangana"),
    ("Bengaluru Mall", "Bengaluru", "Karnataka"),
    ("Chennai Plaza", "Chennai", "Tamil Nadu"),
    ("Mumbai City Center", "Mumbai", "Maharashtra"),
    ("Pune Mega Store", "Pune", "Maharashtra"),
    ("Delhi Super Store", "Delhi", "Delhi"),
    ("Ahmedabad Retail Hub", "Ahmedabad", "Gujarat"),
    ("Jaipur Shopping Point", "Jaipur", "Rajasthan"),
    ("Kolkata Market", "Kolkata", "West Bengal"),
    ("Vizag Retail Plaza", "Visakhapatnam", "Andhra Pradesh")
]