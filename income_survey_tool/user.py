import csv

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

# Example collected data (usually this would come from your MongoDB or Flask form)
users = [
    User(age=25, gender='Male', total_income=50000, expenses={
        'Utilities': 5000,
        'Entertainment': 2000,
        'School Fees': 15000,
        'Shopping': 3000,
        'Healthcare': 7000
    }),
    User(age=30, gender='Female', total_income=60000, expenses={
        'Utilities': 6000,
        'Entertainment': 2500,
        'School Fees': 18000,
        'Shopping': 4000,
        'Healthcare': 8000
    }),
    # Add more User instances as needed
]

# Save the collected data to a CSV file
User.save_to_csv(users, filename='user_data.csv')
