import pandas as pd
import numpy as np

# Simulated transactional data
np.random.seed(42)
data = {
    'customer_id': np.random.randint(1000, 1100, 500),
    'purchase_date': pd.date_range(start='2023-01-01', periods=500, freq='D'),
    'amount': np.random.uniform(10, 500, 500)
}
df = pd.DataFrame(data)

# RFM calculation
now = pd.Timestamp('2023-12-31')
rfm = df.groupby('customer_id').agg(
    recency=('purchase_date', lambda x: (now - x.max()).days),
    frequency=('customer_id', 'count'),
    monetary=('amount', 'sum')
)

# Adding RFM scores
rfm['R'] = pd.qcut(rfm['recency'], 4, labels=[4, 3, 2, 1])
rfm['F'] = pd.qcut(rfm['frequency'], 4, labels=[1, 2, 3, 4])
rfm['M'] = pd.qcut(rfm['monetary'], 4, labels=[1, 2, 3, 4])
rfm['RFM_Score'] = rfm[['R', 'F', 'M']].sum(axis=1)

# Visualization
print(rfm.head())
