import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    percentage_bachelors = ((df['education'] == 'Bachelors').mean() * 100).round(1)

    higher_ed = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = ((df[higher_ed]['salary'] == '>50K').mean() * 100).round(1)

    lower_education_rich = ((df[~higher_ed]['salary'] == '>50K').mean() * 100).round(1)

    min_work_hours = df['hours-per-week'].min()

    rich_percentage = ((df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K').mean() * 100).round(1)

    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (rich_country_counts / country_counts * 100).round(1)

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = country_rich_percentage.max()

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
