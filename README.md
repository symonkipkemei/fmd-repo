# Who
Formode is an architectural company built on the premise of big data , design and creativity.

## Brief

The brief of the project entails creating a dashboard  that allows the partners/employees to monitor their productivity, 
rate of completion of projects ,recording all the projects in a financial year and sharing of revenue

## Objectives
The main items that should be achieved at the end of the project is :
1.Recording all the projects' data
2.Recording the company's expenditure and salaries
3.Documenting the rate of productivity amongst users.


## output
Generating reports at the end of every month

### OBJ 01. Recording all the projects' data
#### Parameters
1.date_commence
8.client_name
2.date_completion
3.project_name
4.project_source
5.project_category
5.project_by
6.project_scope_of_work
7.project_total_fund
8.project_user_fund
9.project_company_fund
8.client_name


#### parameters description

1.date_commence
The date the company was commissioned to undertake a particular project.
A binding contract set either with a deposit or escrow or timeline

2.date_completion
The date of end of contract. Contract terminated with release of full pay for
the work completed

3.project_name(derived)
The name of the project. This should meet the following parameters to be classified a project name
1.(project_commence date)_(firstname_of_the_client)
This should be the PRIMARY KEY when storing to the database

4.project_genre_source
Can be categorized based on the source of work, typically:The user should be able to amend the list by add/subtracting
1.Online 
2.Physical client
3.Competition

5.project_genre_type
Can be further categorized 


## Database 
### 1. project_details
1. project_name(PRIMARY KEY)
2. client_name
3. project_category
4. project_source
5. project_scope
6. date_commencement
7. date_completion

### 2. project_funds
1. project_name
2. project_doneby (PRIMARY KEY)
3. project_fund
4. company_fund
5. userA_income
6. userB_income
7. userC_income

### updating the projects listed

### OBJ 02. Recording company fund
Note that the abbreviation :
1. co stands for company
2. exp stands for expenditures

### co_fund_type
1. income
2. expenditure

### co-income (company fund)
This is funds made from :
1. all projects payed
   filter the mode of payment
   1.1 KSH
   1.2 DOLLARS
2. Loans re-payed
2. exchange rate

### co-exp (company expenditures)
This is what is being subtracted from the formode fund.These are:
1. Salaries
2. r_cost (running cost)
3. Loan

### co-exp-salaries (company expenditures salaries)
The salaries are based on the performance/the effort and amount of work handled by the employee
1. employee A
2. employee B
3. employee C

### co-exp-loans (company expenditures loans/welfare support)
1. employee A
2. employee B
3. employee C

### co-exp-cost (The running cost)
1. electricity
2. rent
3. others


### co-net-funds
The remaining balance after expenditures have been subtracted
for that particular month

#### Parameters
1.date_expenditure
2.category of income
3.category of expenditure
2.expenditure fund
3.income fund
3.sub_category of expenditure
4.Net income

#### Database
record all the parameters




### OBJ 03. Recording project fund distribution