# calculations.py

industry_data = {
    "Manufacturing": {"turnover_rate": 0.1612, "turnover_cost": 32635.20},
    "Social Work/Healthcare": {"turnover_rate": 0.3040, "turnover_cost": 51016},
    "Luxury Retail": {"turnover_rate": 0.5080, "turnover_cost": 20113},
    "Hospitality": {"turnover_rate": 0.3000, "turnover_cost": 22761}
}

def calculate_turnover(num_employees, industry):
    data = industry_data[industry]

    employees_considering_leaving = round(num_employees * data["turnover_rate"])
    employees_leaving_due_to_work_life_balance = round(employees_considering_leaving / 3)
    estimated_turnover_cost = employees_leaving_due_to_work_life_balance * data["turnover_cost"]

    return employees_considering_leaving, employees_leaving_due_to_work_life_balance, estimated_turnover_cost
