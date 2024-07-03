# main.py
import openai
import pandas as pd
from datetime import datetime
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_nutritional_info(food_description):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Provide the nutritional information for the following food: {food_description}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def log_nutritional_info(food_description, nutritional_info):
    data = {
        "timestamp": [datetime.now()],
        "food_description": [food_description],
        "nutritional_info": [nutritional_info]
    }
    df = pd.DataFrame(data)
    df.to_csv('nutrition_log.csv', mode='a', header=False, index=False)

def main():
    while True:
        food_description = input("Enter the food you ate (or type 'exit' to quit): ")
        if food_description.lower() == 'exit':
            break
        nutritional_info = get_nutritional_info(food_description)
        print(f"Nutritional Information: {nutritional_info}")
        log_nutritional_info(food_description, nutritional_info)

if __name__ == "__main__":
    main()
