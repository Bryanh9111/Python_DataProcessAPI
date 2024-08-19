# Databricks notebook source
from flask import jsonify
from app.api import bp
from app.services.data_service import fetch_data_from_api
from app.utils.data_processor import process_data

@bp.route('/processed-data', methods=['GET'])
def get_processed_data():
    raw_data = fetch_data_from_api()
    processed_data = process_data(raw_data)
    return jsonify(processed_data)