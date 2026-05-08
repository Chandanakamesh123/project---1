from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.demand_prediction import train_model
from src.factory_allocation import allocate_factory
from src.shipping_optimizer import optimize_shipping
from src.recommendation_engine import generate_recommendation

# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------

print("Starting Factory Reallocation & Shipping Optimization System")

# Step 1: Data Preprocessing
preprocess_data()

# Step 2: Feature Engineering
create_features()

# Step 3: Train Demand Forecasting Model
train_model()

# Step 4: Factory Recommendation
allocate_factory()

# Step 5: Shipping Optimization
optimize_shipping()

# Step 6: AI Recommendation Output
generate_recommendation()

print("Project execution completed successfully.")
