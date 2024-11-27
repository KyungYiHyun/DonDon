import json
import random

# Load deposit products from the uploaded file
with open("savingproducts.json", "r", encoding="utf-8") as file:
    saving_products = json.load(file)

# Filter products with save_trm >= 6
filtered_products = [
    product for product in saving_products
    if int(product["fields"]["save_trm"]) >= 6
]

# Sort products by intr_rate descending
filtered_products.sort(key=lambda x: x["fields"].get("intr_rate", 0), reverse=True)

# User and product mapping
user_to_product_mapping = []
user_ids = range(1, 20001)  # Assuming user IDs are from 1 to 20,000

for user_id in user_ids:
    # Select 1 to 3 products for the user
    product_count = random.randint(1, 3)
    selected_products = random.sample(filtered_products, product_count)

    # Create mappings
    for product in selected_products:
        user_to_product_mapping.append({
            "model": "fin.savingproducts_like_users",
            "pk": len(user_to_product_mapping) + 1,
            "fields": {
                "user_id": user_id,
                "savingproducts_id": product["pk"]
            }
        })

# Save the mappings to a JSON file
with open("savingproducts_like_users.json", "w", encoding="utf-8") as output_file:
    json.dump(user_to_product_mapping, output_file, ensure_ascii=False, indent=4)

print("User-to-product mapping JSON file created successfully!")
