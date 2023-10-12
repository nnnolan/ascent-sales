import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

# basic stocking system
# will track invenotry for each item
# in the future, will track inventory for each item at each location, and it'll be automated @ the pos
# but for now this is just a proof of concept


#todo: track item purchases for insights

if not os.path.exists('inventory.csv'):
    df = pd.DataFrame(columns=['name', 'quantity', 'price'])
    df.to_csv('inventory.csv', index=False)

# we'll track each item in a csv file  
def new_item(name, quantity, price):
    """
    adds an item to the inventory, appends row to csv
    """
    df = pd.read_csv('inventory.csv')
    df = df.append({'name': name, 'quantity': quantity, 'price': price}, ignore_index=True)
    df.to_csv('inventory.csv', index=False)
    
def remove_item(name):
    """
    remove item from inventory, deletes row from csv
    """
    df = pd.read_csv('inventory.csv')
    df = df[df['name'] != name]
    df.to_csv('inventory.csv', index=False)
    
def update_quantity(name, quantity): ## you could make this one function with update_price, but i think it's better to keep them separate... no real reason
    """
    updates quantity of item in inventory
    """
    df = pd.read_csv('inventory.csv')
    df.loc[df['name'] == name, 'quantity'] = quantity
    df.to_csv('inventory.csv', index=False)

def update_price(name, price):
    """
    updates price of item in inventory
    """
    df = pd.read_csv('inventory.csv')
    df.loc[df['name'] == name, 'price'] = price
    df.to_csv('inventory.csv', index=False)

def get_inventory():
    """
    prints inventory
    """
    print(pd.read_csv('inventory.csv').head())
    print('\n')
    print('total value of inventory: $' + str(sum(pd.read_csv('inventory.csv')['quantity'] * pd.read_csv('inventory.csv')['price'])))
    print('\n')
    print('total number of items in inventory: ' + str(sum(pd.read_csv('inventory.csv')['quantity'])))

def get_item(name):
    """
    prints item
    """
    print(pd.read_csv('inventory.csv')[pd.read_csv('inventory.csv')['name'] == name])
