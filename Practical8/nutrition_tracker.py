# Practical 8 - Nutrition Data Tracker
# Class to define a food item with nutritional information (per practical guide)
class food_item:
    """
    A class to represent a food item with key nutritional values.
    Attributes:
        name (str): Name of the food item (e.g., "Apple")
        calories (float): Calorie content of the food
        protein (float): Grams of protein in the food
        carbs (float): Grams of carbohydrates in the food
        fat (float): Grams of fat in the food
    """
    def __init__(self, name, calories, protein, carbs, fat):
        # Initialize all nutritional attributes of the food item
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

# Function to calculate total daily nutrition and check for excess intake (per practical guide)
def calculate_daily_nutrition(food_list):
    """
    Calculate total 24-hour intake of calories, protein, carbs, fat from a list of food_item objects.
    Prints a warning if calories > 2500 or fat > 90g (per practical requirement).
    
    Args:
        food_list (list): List of food_item instances (consumed food items)
    
    Returns:
        dict: Total nutritional intake (keys: total_cal, total_pro, total_carbs, total_fat)
    """
    # Initialize total nutrition counters
    total_cal = 0.0
    total_pro = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    
    # Iterate through the food list and sum all nutrients
    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_carbs += food.carbs
        total_fat += food.fat
    
    # Print total nutritional intake (formatted for readability)
    print("=== 24-Hour Nutritional Intake Summary ===")
    print(f"Total Calories: {total_cal:.1f} kcal")
    print(f"Total Protein: {total_pro:.1f} g")
    print(f"Total Carbohydrates: {total_carbs:.1f} g")
    print(f"Total Fat: {total_fat:.1f} g")
    print("===========================================")
    
    # Check for excess intake and print warnings (per practical requirement)
    if total_cal > 2500:
        print(f"⚠️  WARNING: Excessive calorie intake! ({total_cal:.1f} > 2500 kcal)")
    if total_fat > 90:
        print(f"⚠️  WARNING: Excessive fat intake! ({total_fat:.1f} > 90 g)")
    
    # Return total nutrition as a dictionary for further use
    return {
        "total_cal": total_cal,
        "total_pro": total_pro,
        "total_carbs": total_carbs,
        "total_fat": total_fat
    }

# Example usage of food_item class and calculate_daily_nutrition function (required by practical)
if __name__ == "__main__":
    # Step 1: Create food_item instances (per practical example + extra items)
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    chicken_breast = food_item("Chicken Breast (100g)", 165, 31, 0, 3.6)
    rice = food_item("Cooked Rice (100g)", 130, 2.7, 28, 0.3)
    avocado = food_item("Avocado (1/2)", 160, 2, 9, 15)
    chocolate = food_item("Chocolate Bar", 250, 3, 26, 15)
    
    # Step 2: Create a list of consumed food items (24-hour intake)
    daily_food = [apple, chicken_breast, rice, avocado, chocolate]
    
    # Step 3: Calculate and print total nutrition + warnings
    calculate_daily_nutrition(daily_food)

    # Test 2: Excess intake (to trigger warnings)
    print("\n--- Test with Excess Intake ---")
    big_steak = food_item("Beef Steak (200g)", 500, 40, 0, 35)
    french_fries = food_item("French Fries (large)", 500, 4, 60, 25)
    soda = food_item("Soda", 150, 0, 39, 0)
    excess_food = [apple, big_steak, french_fries, soda, chocolate, avocado]
    calculate_daily_nutrition(excess_food)