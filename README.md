
# Expense Tracker

An Expense Tracker application built using **Python** (Django), **Sqlite3**, and **HTML/CSS** for tracking and managing personal expenses. It helps users keep track of their income, expenses, and monthly budgets in an easy and efficient way.

## Features

- **User Authentication:** Users can register, login, and manage their accounts.
- **Track Expenses:** Users can add and categorize their expenses with details such as amount, category, and date.
- **Income Tracking:** Users can track their income along with their expenses.
- **Dashboard:** A dashboard for visual representation of income and expense data using charts.
- **Expense Categories:** Ability to categorize expenses (e.g., Food, Rent, Utilities, Entertainment, etc.).
- **Monthly Budget:** Set and manage monthly budgets for different categories.
- **Responsive UI:** A user-friendly, responsive web interface for tracking expenses.

## Tech Stack

- **Backend:** Python,Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** Sqlite3
- **Libraries:** Pandas, Matplotlib (for visualizations)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shreyash0019/ExpenseTracker.git
   cd ExpenseTracker
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Configure the database connection in the settings/config file.
   - Run migrations to set up the database schema.

5. Run the application:

   ```bash
   python app.py  # Or the appropriate command based on your framework (Flask/Django)
   ```

6. Visit the application at `http://127.0.0.1:5000/` or the respective port.

## Usage

- **Register/Login:** Create an account or log in to start tracking expenses.
- **Add Expense:** Use the "Add Expense" form to input new expenses with details.
- **View Dashboard:** Check your expenses and income summary on the dashboard.
- **Set Budget:** Set monthly budgets for each category and monitor your spending.

## Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various budget management tools and open-source projects.
- Special thanks to the contributors and the open-source community for their support.
