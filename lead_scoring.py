import pandas as pd

def calculate_score(row):
    score = (
        0.3 * row['website_visits'] +
        0.4 * row['engagement_score'] +
        0.3 * row['pricing_page_time']
    )
    
    # Normalize score to 0–100
    return min(round(score / 3, 2), 100)


def assign_priority(score):
    if score > 70:
        return "High"
    elif score > 40:
        return "Medium"
    else:
        return "Low"


def process_data(df):
    df['score'] = df.apply(calculate_score, axis=1)
    df['priority'] = df['score'].apply(assign_priority)
    return df