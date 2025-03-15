from flask import Blueprint, jsonify, request, render_template
from models import *

main = Blueprint("routes", __name__)


# Home route that returns a welcome message
@main.route('/')
def home():
    return render_template('index.html')


# Create Routes
# Routes for Income and Expenses

# Route to create new income entries
@main.route('/api/create/income', methods=['POST'])
def createIncome():
    # getting json from user and posting it in database
    data = request.get_json()
    if not data or not 'amount' in data or not 'description' in data or not 'date' in data or not 'category' in data:
        return jsonify({"message": "Invalid request data"}), 400

    amount = data['amount']
    description = data['description']
    date = data['date']
    category = data['category']

    try:
        new_income = Income(amount=amount, description=description, date=date, category_id=category)
        db.session.add(new_income)
        db.session.commit()
        return jsonify({"message": "Income created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to create income", "error": str(e)}), 500


# Route to create new expense entries
@main.route('/api/create/expenses', methods=['POST'])
def createExpenses():
    data = request.get_json()
    if not data or not 'amount' in data or not 'description' in data or not 'date' in data or not 'category' in data:
        return jsonify({"message": "Invalid request data"}), 400

    amount = data['amount']
    description = data['description']
    date = data['date']
    category = data['category']

    try:
        new_expense = Expense(amount=amount, description=description, date=date, category_id=category)
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": "Expense created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to create expense", "error": str(e)}), 500


# Route to create new categories for income and expenses
@main.route('/api/create/category', methods=['POST'])
def createCategory():
    data = request.get_json()
    if not data or not 'name' in data:
        return jsonify({"message": "Invalid request data"}), 400

    name = data['name']

    try:
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return jsonify({"message": "Category created successfully"}), 201
    except Exception as e:
        db.session.rollback()
    return jsonify({"message": "Failed to create category", "error": str(e)}), 500


# Route to create goals
@main.route('/api/create/goal', methods=['POST'])
def createGoal():
    data = request.get_json()
    if not data or not 'amount' in data or not 'description' in data or not 'date' in data or not 'category' in data:
        return jsonify({"message": "Invalid request data"}), 400

    amount = data['amount']
    description = data['description']
    date = data['date']
    category = data['category']

    try:
        new_goal = Goal(amount=amount, description=description, date=date, category_id=category)
        db.session.add(new_goal)
        db.session.commit()
        return jsonify({"message": "Goal created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to create goal", "error": str(e)}), 500


# End of create routes

# ****** Start of read routes ******

# Route to read expense entries
@main.route('/api/read/expenses', methods=['GET'])
def readExpenses():
    expenses = Expense.query.all()
    expenses_list = [
        {'id': expense.id, 'amount': expense.amount, 'date': expense.date, 'description': expense.description,
         'category': expense.category.name} for expense in expenses]
    return jsonify(expenses_list)


# Route to read all income entries
@main.route('/api/read/income', methods=['GET'])
def readIncome():
    incomes = Income.query.all()
    incomes_list = [{'id': income.id, 'amount': income.amount, 'date': income.date, 'description': income.description,
                     'category': income.category.name} for income in incomes]
    return jsonify(incomes_list)


# Route to read all goals
@main.route('/api/read/goal', methods=['GET'])
def readGoal():
    goals = Goal.query.all()
    goals_list = [{'id': goal.id, 'amount': goal.amount, 'date': goal.date, 'description': goal.description,
                   'category': goal.category.name} for goal in goals]
    return jsonify(goals_list)


# Route to read all categories for income and expenses
@main.route('/api/read/category', methods=['GET'])
def readCategory():
    categories = Category.query.all()
    categories_list = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify(categories_list)


# ****** End of read routes ******

# Route to update a specific expense entry
@main.route('/api/update/expenses/<int:id>', methods=['PUT'])
def updateExpenses(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({"message": "Expense not found"}), 404

    data = request.get_json()
    if 'amount' in data:
        expense.amount = data['amount']
    if 'date' in data:
        expense.date = data['date']
    if 'description' in data:
        expense.description = data['description']
    if 'category_id' in data:
        expense.category_id = data['category_id']  # Assuming category is referenced by an ID
    try:
        db.session.commit()
        return jsonify({"message": "Expense updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update expense", "error": str(e)}), 500


# Route to update a specific income entry
@main.route('/api/update/income/<int:id>', methods=['PUT'])
def updateIncome(id):
    income = Income.query.get(id)

    if not income:
        return jsonify({"message": "Income not found"}), 404

    data = request.get_json()
    if 'amount' in data:
        income.amount = data['amount']
    if 'date' in data:
        income.date = data['date']
    if 'description' in data:
        income.description = data['description']
    if 'category_id' in data:
        income.category_id = data['category_id']  # Assuming category is referenced by an ID
    try:
        db.session.commit()
        return jsonify({"message": "Income updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update income", "error": str(e)}), 500


# Route to update a specific goal
@main.route('/api/update/goal/<int:id>', methods=['PUT'])
def updateGoal(id):
    goal = Goal.query.get(id)
    if not goal:
        return jsonify({"message": "Goal not found"}), 404

    data = request.get_json()
    if 'amount' in data:
        goal.amount = data['amount']
    if 'date' in data:
        goal.date = data['date']
    if 'description' in data:
        goal.description = data['description']
    if 'category_id' in data:
        goal.category_id = data['category_id']  # Assuming category is referenced by an ID
    try:
        db.session.commit()
        return jsonify({"message": "Goal updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update goal", "error": str(e)}), 500


# Route to update a specific category
@main.route('/api/update/category/<int:id>', methods=['PUT'])
def updateCategory(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    data = request.get_json()

    try:
        if 'name' in data:
            category.name = data['name']
            db.session.commit()
            return jsonify({"message": "Category updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update category", "error": str(e)}), 500


# ****** End of update routes ******
# Route to delete a specific expense entry
@main.route('/api/delete/expenses/<int:id>', methods=['DELETE'])
def deleteExpenses(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({"message": "Expense not found"}), 404

    try:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({"message": "Expense deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to delete expense", "error": str(e)}), 500


# Route to delete a specific income entry
@main.route('/api/delete/income/<int:id>', methods=['DELETE'])
def deleteIncome():
    from spendwise.models.Income import Income
    income = Income.query.get(id)
    if not income:
        return jsonify({"message": "Income not found"}), 404

    try:
        db.session.delete(income)
        db.session.commit()
        return jsonify({"message": "Income deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to delete income", "error": str(e)}), 500


# Route to delete a specific goal
@main.route('/api/delete/goal/<int:id>', methods=['DELETE'])
def deleteGoal(id):
    goal = Goal.query.get(id)
    if not goal:
        return jsonify({"message": "Goal not found"}), 404
    try:
        db.session.delete(goal)
        db.session.commit()
        return jsonify({"message": "Goal deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to delete goal", "error": str(e)}), 500


# Route to delete a specific category
@main.route('/api/delete/category/<int:id>', methods=['DELETE'])
def deleteCategory(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    try:
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to delete category", "error": str(e)}), 500

# ****** End of delete routes ******