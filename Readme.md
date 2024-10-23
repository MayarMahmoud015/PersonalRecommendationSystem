# Personalized Recommendation System

## Description
This project aims to build a personalized recommendation system using the Amazon Fine Food Reviews dataset. The system utilizes ensemble learning and collaborative filtering to suggest products that align with user preferences. The output suggests a mix of products of user preference, products that the user is expected to like & hot products related to the user preference.


## Installation

To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To use the recommendation system, run the following code:
```python
recommendations10 = recommendations(user_id)
trendy_item_ids = trendy_products(user_id)

# Print the final recommendations
print(f"\nRecommendations for user {test_user_id}:")

# First, display the trendy (hot) products
print("\nHot Products (Trending):")
for product in trendy_item_ids: 
    print(f"- Product ID: {product}")
# Then, display the 10 recommended products
print("\nThe 10 Recommended Products:")
for product in recommendations10:  
    print(f"- Product ID: {product}")
```
## Features
- User preference-based recommendations.
- Ensemble learning predictions.
- Hot product suggestions.

## Results
The system provides:

- 5 products based on user preferences (from rated products by the user).
- 5 predicted products that the user is expected to like using ensemble learning.
- 3 hot products (trendy) related to user preference using item-item collaborative filtering.

## Future Work
- Split the data into categories to make it easy to recommend suitable products.
- Implement additional recommendation algorithms.
- Enhance the model with user feedback.

## License
This project is licensed under the MIT License.

[MIT](https://choosealicense.com/licenses/mit/)

## Kaggle Code Link 
You can find the code of the project on Kaggle from that link:
[Kaggle](https://www.kaggle.com/code/mayarmahmoud015/personal-recommendation-system)
