#Tax Rate Joseph Rydberg 10/7/2024

def calculate_taxes():
    monthlySales = float(input("Please enter monthly sales, $"))
    stateTax = monthlySales * 0.05
    countyTax = monthlySales * 0.025

    print("County tax $",countyTax)
    print("State tax $",stateTax)
    print("Total tax $",countyTax + stateTax)

calculate_taxes()