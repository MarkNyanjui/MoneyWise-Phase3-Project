from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///moneywise.db')
Session = sessionmaker(bind=engine)

##### Main tables
class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100))
    email = Column(String, unique=True)


    ## Relationships of the users table with the other tables
    categories = relationship(
        "Categories", 
        secondary= 'user_categories',
        back_populates='users',
        primaryjoin="Categories.category_id==UserCategories.category_id",
        secondaryjoin="UserCategories.user_id==Users.user_id")
    transactions = relationship('Transactions', secondary = 'user_transactions', back_populates='users')
    budgets = relationship('Budgets', secondary = 'user_budgets', back_populates='users')
    savings = relationship('Savings', secondary = 'user_savings', back_populates='users')


class Categories(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)


    ## Relationships of the categories table with the other tables
    users = relationship(
        "Users", 
        secondary= 'user_categories', 
        back_populates= 'categories',
        primaryjoin="Users.user_id==UserCategories.user_id",
        secondaryjoin="UserCategories.user_id==Users.user_id")
    transactions = relationship("Transactions", back_populates="categories")
    budgets = relationship("Budgets", back_populates= 'categories')



class Transactions(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(DECIMAL)
    description = Column(String(100), unique=True)
    transaction_date = Column(DateTime)
    transaction_type = Column(String(20))
    category_id = Column(Integer, ForeignKey('categories.category_id'))


    ## Relationships of the transactions table with the other tables
    users = relationship("Users", secondary="user_transactions", back_populates='transactions')
    categories = relationship("Categories", back_populates="transactions")


class Budgets(Base):
    __tablename__ = 'budgets'

    budget_id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(DECIMAL, unique=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    month = Column(String(30))
    year = Column(Integer)


    ## Relationships of the budgets table with the other tables
    users = relationship("Users", secondary = 'user_budgets', back_populates='budgets')
    categories = relationship("Categories", back_populates='budgets')



class Savings(Base):
    __tablename__ ='savings'

    saving_id = Column(Integer, primary_key = True, autoincrement= True)
    amount = Column(DECIMAL, unique=True)
    goal = Column(String(100))
    start_month = Column(String(10))
    end_month = Column(String(10))
    user_id = Column(Integer, ForeignKey('users.user_id'))

    ## Relationships of the savings table with the other tables
    users = relationship("Users", secondary = 'user_savings', back_populates='savings')


##### Joining/association tables

## Every table from here is a joining table because the users table has a many-to-many realtionship with the rest of the tables present 
class UserCategories(Base):
    __tablename__ = 'user_categories'

    uc_id = Column(Integer, primary_key=True, autoincrement= True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category_name = Column(String(100), ForeignKey('categories.name'))
    


class UserBudgets(Base):
    __tablename__ = 'user_budgets'

    ub_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    budget_id = Column(Integer, ForeignKey('budgets.budget_id'))
    budget_amount = Column(Integer, ForeignKey('budgets.amount'))


class UserTransactions(Base):
    __tablename__ = 'user_transactions'

    ut_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    transaction_id = Column(Integer, ForeignKey('transactions.transaction_id'))
    transaction_desc = Column(String(100), ForeignKey('transactions.description'))


class UserSavings(Base):
    __tablename__ = 'user_savings'

    us_id = Column(Integer, primary_key = True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    saving_id = Column(Integer, ForeignKey('savings.saving_id'))
    saving_amount = Column(DECIMAL, ForeignKey('savings.amount'))

Base.metadata.create_all(engine)
