# Databricks notebook source
dbutils.widgets.text("env", "qa")
ENV =  dbutils.widgets.get("env")

print("environment value received:", ENV)
