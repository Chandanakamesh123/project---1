# Factory Reallocation & Shipping Optimization Recommendation System

---

#  Project Overview

Modern supply chain and logistics systems face major challenges in managing product distribution efficiently across multiple factories and warehouses. Companies often experience high transportation costs, delayed deliveries, inventory imbalance, and inefficient factory utilization due to improper allocation of orders and shipping routes.

This project presents an AI-powered Factory Reallocation and Shipping Optimization Recommendation System developed for Nassau Candy Distributor. The system combines Machine Learning, Recommendation Systems, and Linear Programming techniques to intelligently predict product demand, recommend the most suitable factory for order fulfillment, and optimize shipping operations.

The main goal of this project is to reduce logistics costs, improve delivery efficiency, and automate supply chain decision-making through intelligent recommendations and optimization techniques.

---

#  Problem Statement

Large-scale distributors and logistics companies handle thousands of product shipments daily from multiple factories and warehouses to different customer regions. Managing this process manually can lead to several operational problems such as:

- Increased transportation expenses
- Delayed deliveries
- Uneven factory workload distribution
- Overstocking and stock shortages
- Inefficient shipping route selection
- Poor inventory utilization

Traditional logistics systems mainly rely on static allocation methods and manual decision-making, which are not efficient for modern large-scale supply chain operations.

To overcome these challenges, this project introduces an intelligent recommendation system capable of making automated and optimized allocation decisions using data-driven approaches.

---

#  Objectives of the Project

- Predict future product demand using historical sales and shipment data
- Recommend the best factory for order fulfillment
- Optimize transportation and shipping costs
- Improve delivery speed and operational efficiency
- Dynamically balance inventory between factories
- Reduce factory overload situations
- Improve supply chain management through intelligent automation
- Provide real-time analytics and visualization using a dashboard

---

#  Proposed System

The proposed system follows a hybrid architecture that integrates Machine Learning, Recommendation Systems, and Optimization Algorithms into a single intelligent framework.

## Workflow

1. Historical Data  
2. Demand Forecasting Model   
3. Factory Scoring Engine  
4. Dynamic Allocation Algorithm 
5. Shipping Cost Optimizer  
6. AI Recommendation Output  
7. Dashboard Visualization

---

#  Working of the System

## 1️. Historical Data Collection

The system first collects historical logistics and shipping data such as:

- Previous order records
- Factory details
- Warehouse stock information
- Shipping costs
- Delivery times
- Transportation modes
- Customer regions
- Seasonal demand patterns

This data serves as the foundation for training machine learning models and performing optimization tasks.

---

## 2️. Demand Forecasting

The Demand Forecasting module predicts future product demand for different customer regions using Machine Learning techniques.

### Model Used
- XGBoost Regressor

### Purpose
- Predict future regional demand
- Improve inventory planning
- Reduce stock shortages
- Prevent overstocking

---

## 3️. Factory Scoring Engine

One of the key innovations of this project is the Factory Scoring Engine.

Instead of assigning factories manually, the system calculates a score for each factory based on multiple factors such as:

- Inventory availability
- Shipping cost
- Delivery time
- Factory workload
- Route distance

### Factory Score Formula

Factory Score = Inventory Availability / (Shipping Cost + Delivery Time + Factory Load)

Factories with higher scores are considered more suitable for fulfilling orders.

This recommendation-based approach makes the system more intelligent and dynamic compared to traditional allocation systems.

---

# Dynamic Allocation Algorithm

The Dynamic Allocation module intelligently reallocates orders and inventory between factories based on real-time conditions.

If a factory becomes overloaded or lacks sufficient inventory, the system automatically shifts orders to another suitable factory with better availability and lower operational cost.

### Benefits

- Balances workload between factories
- Improves operational efficiency
- Reduces shipment delays
- Utilizes inventory effectively

---

#  Shipping Cost Optimization

The Shipping Optimization module minimizes transportation expenses using Linear Programming techniques.

### Optimization Technique
- PuLP Linear Programming

### Objective Function

Minimize:
- Shipping Cost
- Delay Penalty
- Storage Cost

### Constraints

- Factory capacity
- Inventory availability
- Customer demand
- Delivery deadlines

This enables the system to generate cost-efficient shipping recommendations.

---

#  Technologies Used

 Technology                Purpose 

 Python                    Core Programming Language 
 Pandas                    Data Processing 
 NumPy                     Numerical Computation 
 Scikit-learn              Machine Learning 
 XGBoost                   Demand Forecasting 
 PuLP                      Optimization Algorithm 
 Streamlit                 Dashboard Development 
 Matplotlib                Visualization 
 Seaborn                   Data Analytics 
 Plotly                    Interactive Graphs 

---

#  Features of the Project

- Demand Forecasting
- Smart Factory Recommendation
- Dynamic Inventory Reallocation
- Shipping Route Optimization
- Transportation Cost Reduction
- Factory Utilization Analysis
- Real-Time Dashboard Visualization
- Automated Supply Chain Decision-Making

---

#  Dataset Description

The dataset used in this project contains logistics and shipment-related information.

## Important Dataset Attributes

     Column Name                  Description 
     
     order_id                     Unique order identifier 
     customer_region              Customer delivery region 
     product_id                   Product identifier 
     order_quantity               Quantity ordered 
     shipping_cost                Transportation cost 
     warehouse_stock              Available inventory 
     delivery_days                Delivery duration 
     route_distance               Shipping distance 
     factory_capacity             Factory production limit 
     transport_mode               Transportation method 
     season                       Seasonal demand category 
     demand                       Historical demand value 

---

#  Project Structure

factory-shipping-optimization-system/

├── data/  
│   ├── raw_shipping_data.csv  
│   ├── processed_shipping_data.csv  

├── notebooks/  
│   ├── 01_data_preprocessing.ipynb  
│   ├── 02_exploratory_data_analysis.ipynb  
│   ├── 03_model_training.ipynb  
│   ├── 04_shipping_optimization.ipynb  
│   ├── 05_dashboard_testing.ipynb  

├── src/  
│   ├── data_preprocessing.py  
│   ├── feature_engineering.py  
│   ├── demand_prediction.py  
│   ├── factory_allocation.py  
│   ├── shipping_optimizer.py  
│   ├── recommendation_engine.py  
│   ├── utils.py  

├── dashboard/  
│   ├── app.py  

├── models/  
│   ├── demand_forecast_model.pkl  

├── outputs/  
│   ├── graphs/  
│   ├── reports/  

├── screenshots/  

├── requirements.txt  
├── README.md  
├── main.py  
└── .gitignore  

---

#  Installation

## Clone the Repository

```bash
git clone <repository_link>

**## Move to Project Directory**

cd factory-shipping-optimization-system

**## Install Dependencies**

pip install -r requirements.txt

** Running the Project
Run Main Application**

python main.py

**Run Streamlit Dashboard**

streamlit run dashboard/app.py

---

**## AUTHOR**
CHANDANA K
