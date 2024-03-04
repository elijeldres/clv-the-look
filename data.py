import pandas as pd
from lifetimes.utils import summary_data_from_transaction_data

def data_cleaning(order_items_df, orders_df):
    '''
    This function takes the order_items and the orders tables, aggregates the order_items table,
    merges the tables, cleans the datatypes and returns the cleaned dataframe
    '''
    # Convert the created_at column from object to datetime

    order_sales = order_items_df[['order_id','sale_price']].groupby(by='order_id').sum('sale_price').reset_index()
    order_sales = order_sales.merge(orders_df[['order_id','user_id','created_at']]).set_index('order_id')

    order_sales['created_at'] = pd.to_datetime(order_sales.created_at,format='mixed')

    return order_sales

def rfm(cleaned_order_items_df):
    '''
    This function takes the cleaned order_items dataframe and outputs the Recency, Frequency and Tenure dataframe
    '''
    return summary_data_from_transaction_data(transactions = cleaned_order_items_df,
                                              customer_id_col = 'user_id',
                                              datetime_col = 'created_at',
                                              monetary_value_col = 'sale_price')
