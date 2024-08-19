# Databricks notebook source
import requests
from flask import current_app

def fetch_data_from_api():
    api_url = current_app.config['EXTERNAL_API_URL']
    response = requests.get(api_url)
    return response.json()