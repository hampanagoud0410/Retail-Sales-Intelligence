"""
Customer Data Generator

Generates realistic customer data for the
Retail Sales Intelligence project.
"""

from faker import Faker
import pandas as pd
import random
from pathlib import Path

from src.generators.common import LOCATIONS
# Initialize Faker
fake = Faker("en_IN")

# Number of customers
NUM_CUSTOMERS = 10000

# Cities and States


customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()

    last_name = fake.last_name()

    city, state = random.choice(LOCATIONS)

    customers.append(
        {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "age": random.randint(18, 70),
            "city": city,
            "state": state,
            "join_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ),
        }
    )

customer_df = pd.DataFrame(customers)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "customers.csv"

customer_df.to_csv(OUTPUT_PATH, index=False)

print("=" * 60)
print("Customer dataset generated successfully!")
print(f"Records : {len(customer_df)}")
print(f"Saved to: {OUTPUT_PATH}")
print("=" * 60)