import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
import random
import string

class RecommenderSystem:
    def __init__(self, data_path):
        # Load and clean data
        amazon_ratings = pd.read_csv(data_path).dropna()
        amazon_ratings = amazon_ratings.head(10000)

        # Generate unique product names if not present
        if 'ProductName' not in amazon_ratings.columns:
            unique_products = amazon_ratings['ProductId'].unique()
            product_name_pool = [
                "Wireless Mouse", "Bluetooth Speaker", "Noise Cancelling Headphones", "Smartphone Case",
                "Fitness Tracker", "Laptop Stand", "Yoga Mat", "Portable Charger", "USB-C Hub",
                "Gaming Keyboard", "LED Monitor", "Mechanical Pencil", "Travel Backpack", "Electric Toothbrush",
                "Ceramic Mug", "Smartwatch", "Photo Frame", "Laptop Sleeve", "Kitchen Scale", "Hair Dryer",
                "Wireless Earbuds", "Standing Desk", "Robot Vacuum", "Reusable Water Bottle", "HD Webcam",
                "Notebook Cooler", "Smart Bulb", "Smart Plug", "Wireless Charger", "Ergonomic Office Chair",
                "Desk Organizer", "Electric Kettle", "Phone Tripod", "Digital Alarm Clock", "Bluetooth Tracker",
                "Indoor Plant Pot", "Adjustable Dumbbells", "Resistance Bands", "Foam Roller", "LED Desk Lamp",
                "Mini Projector", "Streaming Stick", "Rice Cooker", "Blender Bottle", "Memory Foam Pillow",
                "Portable Fan", "Waterproof Speaker", "Noise Machine", "Electric Screwdriver", "Tool Kit",
                "Rechargeable Batteries", "Label Maker", "Photo Printer", "Ink Cartridge", "Drawing Tablet",
                "Fitness Smart Ring", "Portable SSD", "Wireless Presenter", "Touchscreen Stylus", "Dry Erase Board",
                "Cable Organizer", "Hiking Boots", "Binoculars", "Action Camera", "Smart Thermostat",
                "Gaming Chair", "Pet Water Fountain", "Car Phone Mount", "Dash Cam", "Air Purifier",
                "Dehumidifier", "Scent Diffuser", "Essential Oil Set", "Makeup Mirror", "Electric Razor",
                "Beard Trimmer", "Facial Steamer", "Hair Straightener", "Nail Drill Kit", "Jewelry Box",
                "Phone Sanitizer", "Wi-Fi Range Extender", "Ethernet Switch", "Laptop Docking Station",
                "Mechanical Watch", "Travel Adapter", "Smart Doorbell", "Security Camera", "Fingerprint Lock",
                "Bike Phone Holder", "Electric Scooter", "Drone with Camera", "Pet Grooming Kit",
                "Baby Monitor", "Baby Carrier", "Diaper Bag", "Kids Tablet", "Puzzle Mat", "Toy Storage Bin",
                "Learning Robot", "Educational Board Game", "Drawing Easel", "Building Blocks"
            ]

            def generate_unique_name(base_list, count):
                used = set()
                results = []
                while len(results) < count:
                    base = random.choice(base_list)
                    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                    full = f"{base} {suffix}"
                    if full not in used:
                        results.append(full)
                        used.add(full)
                return results

            unique_names = generate_unique_name(product_name_pool, len(unique_products))
            product_id_to_name = dict(zip(unique_products, unique_names))
            amazon_ratings['ProductName'] = amazon_ratings['ProductId'].map(product_id_to_name)

        else:
            product_id_to_name = dict(zip(amazon_ratings['ProductId'], amazon_ratings['ProductName']))

        # Save mapping and data
        self.product_id_to_name = product_id_to_name
        self.amazon_ratings = amazon_ratings

        # Build utility matrix
        ratings_matrix = amazon_ratings.pivot_table(values='Rating', index='UserId', columns='ProductId', fill_value=0)
        X = ratings_matrix.T  # Transpose to get products as rows
        self.X = X  # Save for future use

        # Apply Truncated SVD
        SVD = TruncatedSVD(n_components=10)
        decomposed_matrix = SVD.fit_transform(X)
        self.products = list(X.index)
        self.correlation_matrix = np.corrcoef(decomposed_matrix)

    def get_random_products(self, n=12):
        return random.sample(self.products, n)

    def get_product_name(self, product_id):
        return self.product_id_to_name.get(product_id, "Unknown Product")

    def get_random_product_and_name(self):
        idx = random.randint(0, len(self.X) - 1)
        product_id = self.X.index[idx]
        product_name = self.get_product_name(product_id)
        print(f"Selected Product ID: {product_id}")
        print(f"Selected Product Name: {product_name}")
        return product_id, product_name

    def get_recommendations(self, product_id, top_n=8):
        if product_id not in self.products:
            return []
        idx = self.products.index(product_id)
        similarity_scores = self.correlation_matrix[idx]
        similar_indices = np.where(similarity_scores > 0.90)[0]
        recommended_ids = [self.products[i] for i in similar_indices if i != idx][:top_n]
        recommended_names = [self.get_product_name(pid) for pid in recommended_ids]
        return list(zip(recommended_ids, recommended_names))
