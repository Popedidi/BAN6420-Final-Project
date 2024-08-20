import csv
from pymongo import MongoClient

# Define the User class
class User:
    def __init__(self, age, gender, total_income, expenses):
        """
        Initialize the User class with basic details and expenses.
        :param age: Age of the user
        :param gender: Gender of the user
        :param total_income: Total income of the user
        :param expenses: A dictionary containing expense categories and amounts
        """
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses
    
    def to_dict(self):
        """
        Convert the User instance to a dictionary for easier CSV writing.
        :return: Dictionary of the user's data
        """
        data = {
            'Age': self.age,
            'Gender': self.gender,
            'Total Income': self.total_income
        }
        data.update(self.expenses)
        return data

    @staticmethod
    def save_to_csv(users, filename='user_data.csv'):
        """
        Save a list of User instances to a CSV file.
        :param users: List of User instances
        :param filename: The name of the CSV file to save to
        """
        if not users:
            return
        
        # Define CSV header
        fieldnames = ['Age', 'Gender', 'Total Income'] + list(users[0].expenses.keys())
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                writer.writerow(user.to_dict())

# Fetch data from MongoDB
def fetch_data_from_mongo():
    # Establish connection to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database_name']  # Replace with your actual database name
    collection = db['your_collection_name']  # Replace with your actual collection name
    
    # Fetch all documents from the collection
    documents = collection.find()
    
    users = []
    
    for doc in documents:
        # Create a User instance from each document
        user = User(
            age=doc.get('age'),
            gender=doc.get('gender'),
            total_income=doc.get('total_income'),
            expenses={
                'Utilities': doc.get('utilities', 0),
                'Entertainment': doc.get('entertainment', 0),
                'School Fees': doc.get('school_fees', 0),
                'Shopping': doc.get('shopping', 0),
                'Healthcare': doc.get('healthcare', 0)
            }
        )
        users.append(user)
    
    return users

# Main function to process the data
def main():
    # Fetch data from MongoDB
    users = fetch_data_from_mongo()
    
    # Save the data to a CSV file
    User.save_to_csv(users, filename='user_data.csv')

# Execute the main function
if __name__ == "__main__":
    main()
