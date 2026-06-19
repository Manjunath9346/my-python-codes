def find_second_highest_salary(df):
    salaries = df['salary'].drop_duplicates().nlargest(2)

    if len(salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    return pd.DataFrame({'SecondHighestSalary': [salaries.iloc[-1]]})
