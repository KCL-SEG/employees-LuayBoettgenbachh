class Employee:

  def __init__(self,
               name,
               contract_type,
               monthly_salary=None,
               hourly_wage=None,
               hours_worked=None,
               commission_type=None,
               num_contracts=None,
               commission_rate=None,
               bonus=None):
    self.name = name
    self.contract_type = contract_type
    self.monthly_salary = monthly_salary
    self.hourly_wage = hourly_wage
    self.hours_worked = hours_worked
    self.commission_type = commission_type
    self.num_contracts = num_contracts
    self.commission_rate = commission_rate
    self.bonus = bonus

  def get_pay(self):
    if self.contract_type == 'salary':
      pay = self.monthly_salary
    elif self.contract_type == 'hourly':
      pay = self.hourly_wage * self.hours_worked
    else:
      pay = 0

    if self.commission_type == 'fixed':
      pay += self.bonus
    elif self.commission_type == 'contract':
      pay += self.num_contracts * self.commission_rate

    return pay

  def __str__(self):
    pay_details = f"{self.name} works on a"

    if self.contract_type == 'salary' and self.commission_type == 'fixed':
      pay_details += f" monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}."
    elif self.contract_type == 'salary' and self.commission_type == 'contract':
      pay_details += f" monthly salary of {self.monthly_salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract."
    elif self.contract_type == 'hourly' and self.commission_type == 'fixed':
      pay_details += f" contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus}."
    elif self.contract_type == 'hourly' and self.commission_type == 'contract':
      pay_details += f" contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract."
    elif self.contract_type == 'salary':
      pay_details += f" monthly salary of {self.monthly_salary}."
    elif self.contract_type == 'hourly':
      pay_details += f" contract of {self.hours_worked} hours at {self.hourly_wage}/hour."

    pay_details += f" Their total pay is {self.get_pay()}."

    return pay_details


billie = Employee('Billie', 'salary', monthly_salary=4000)
charlie = Employee('Charlie', 'hourly', hourly_wage=25, hours_worked=100)
renee = Employee('Renee',
                 'salary',
                 monthly_salary=3000,
                 commission_type='contract',
                 num_contracts=4,
                 commission_rate=200)
jan = Employee('Jan',
               'hourly',
               hourly_wage=25,
               hours_worked=150,
               commission_type='contract',
               num_contracts=3,
               commission_rate=220)
robbie = Employee('Robbie',
                  'salary',
                  monthly_salary=2000,
                  commission_type='fixed',
                  bonus=1500)
ariel = Employee('Ariel',
                 'hourly',
                 hourly_wage=30,
                 hours_worked=120,
                 commission_type='fixed',
                 bonus=600)