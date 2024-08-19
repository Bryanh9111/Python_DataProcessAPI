# Databricks notebook source
def process_data(data):
    # Perform all data manipulations here
    # This is just a simple example
    processed_data = [item.upper() if isinstance(item, str) else item for item in data]
    return processed_data