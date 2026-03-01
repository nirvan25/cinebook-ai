🎬 CineBook AI

A deployed movie booking and AI-powered recommendation platform built using Streamlit, SQLite, and Python.

Live Application:
https://cinebookai.streamlit.app

Overview

CineBook AI is an end-to-end web application that simulates a modern movie booking ecosystem enhanced with intelligent personalization.

The platform integrates:

- A persistent booking system

- A real-time analytics dashboard

- A modular recommendation engine

- Cloud deployment via Streamlit Community Cloud

The goal of this project was to design and deploy a complete intelligent system — combining UI, database management, analytics, and explainable recommendation logic.


Core Features

1. Movie Catalog

- Poster-based grid layout

- Multi-era dataset (1940–2025)

- Genre, year, and rating display

- Clean responsive UI

2. Booking System

- Movie selection

- Ticket quantity input

- Automatic revenue calculation

- Persistent storage using SQLite

- Real-time analytics updates

3. Analytics Dashboard

- Total revenue tracking

- Ticket count aggregation

- Most popular movie identification

- Movie popularity visualization (Matplotlib)

4. AI Recommendation Engine

- The recommendation system uses a weighted scoring model based on:

- Genre preferences

- Director preferences

- Era constraints

- IMDB rating baseline

- Each filtered movie receives a computed score:

  - Final Score = IMDB Rating (Director Preference × Weight) . (Genre Preference × Weight)


If no movie satisfies the constraints, the system returns a structured fallback response.

This makes the recommendation logic transparent and explainable.


System Architecture

The project follows a modular structure:

- streamlit_app.py — Main UI and application logic

- ml_engine/recommender.py — Recommendation engine

- analytics/dashboard.py — Visualization layer

- analytics/insights.py — Revenue and popularity computation

- app/database.py — SQLite connection handler

- assets/ — Local poster images

- database/ — SQLite database file

- requirements.txt — Python dependencies


Tech Stack

- Python

- Streamlit

- SQLite

- Pandas

- Matplotlib

- Git & GitHub

- Streamlit Community Cloud (Deployment)



Future Improvements

- User authentication

- Admin control panel

- Enhanced recommendation modeling (collaborative filtering)

- Cloud database migration

- Payment gateway simulation



Author

Nirvan Chhajed
