# Databricks notebook source
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    EXTERNAL_API_URL = os.environ.get('EXTERNAL_API_URL') or 'https://api.example.com/data'