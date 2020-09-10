from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def all_tasks():
    rows = session.query(Table).all()
    i = 0
    counter = 1
    while i < len(rows):
        ordered = session.query(Table).order_by(Table.deadline).all()
        print(f"{counter}. {ordered[i]}. {ordered[i].deadline.day} {today.strftime('%b')}")
        i += 1
        counter += 1


def menu():
    print("""\n1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit.""")


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


IS_WORKING = True
today = datetime.today()


while IS_WORKING:
    menu()
    user_input = input()
    if user_input == "1":  # today's task
        today_rows = session.query(Table).filter(Table.deadline == today.date()).all()
        if len(today_rows) == 0:
            print("\nToday: \nNothing to do!\n")
        else:
            print(f"{today.strftime('%A')} {today.day} {today.strftime('%b')}:")
            i = 0
            counter = 1
            while i < len(today_rows):
                print(f"{counter}. {today_rows[i]}. {today_rows[i].deadline.day} {today.strftime('%b')}")
                i += 1
                counter += 1
    elif user_input == "2":  # week's tasks
        i = 0
        while i < 7:
            this_day = today + timedelta(days=i)
            this_day_tasks = session.query(Table).filter(Table.deadline == this_day.date()).all()
            print(f"{this_day.strftime('%A')} {this_day.day} {this_day.strftime('%b')}:")
            if len(this_day_tasks) == 0:
                print("Nothing to do!")
                print()
            else:
                j = 0
                count = 1
                while j < len(this_day_tasks):
                    print(f"{count}. {this_day_tasks[j]}")
                    j += 1
                    count += 1
                print()
            i += 1
    elif user_input == "3":  # all tasks
        all_tasks()
    elif user_input == "4":  # missed tasks
        rows = session.query(Table).all()
        if rows == 0:
            print("Nothing is missed!")
        else:
            missed_tasks = session.query(Table).filter(Table.deadline < datetime.today().date()).all()
            num = 0
            list_counter = 1
            print("Missed Tasks:")
            while num < len(missed_tasks):
                tasks = session.query(Table).order_by(Table.deadline).all()
                print(f"{list_counter}. {tasks[num]}. {tasks[num].deadline.day} {today.strftime('%b')}")
                num += 1
                list_counter += 1
            print()
    elif user_input == "5":  # add tasks
        add_task = input("Enter task\n")
        add_deadline = input("Enter deadline\n")  # format: YYYY-MM-DD
        date_string = datetime.strptime(add_deadline, '%Y-%m-%d')
        new_row = Table(task=add_task, deadline=date_string)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
    elif user_input == "6":  # delete tasks
        rows = session.query(Table).all()
        if len(rows) == 0:
            print("Nothing to delete")
        else:
            print("Choose the number of the task you want to delete:")
            all_tasks()
            user_input_delete = int(input())
            specific_row = rows[user_input_delete - 1]  # in case rows is not empty
            session.delete(specific_row)
            session.commit()
            print("The task has been deleted!")

    elif user_input == "0":
        print("Bye!")
        exit()
