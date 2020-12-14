def calculate_loan(account_number, salary, account_balance, loan_type, loan_amount_expected, customer_emi_expected):
    bank_emi_expected = 36
    eligible_loan_amount = 500000
    a = str(account_number)
    if (len(a) == 4 and a[0] == '1' and account_balance >= 100000 and loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
        """if loan_type=='Car':
            bank_emi_expected = int(input("Enter bank_emi_expected for Car loan type : "))
            eligible_loan_amount = int(input("Enter eligible loan amount for Car loan type : "))
        elif loan_type=='House':
            bank_emi_expected = int(input("Enter bank_emi_expected of House loan type : "))
            eligible_loan_amount = int(input("Enter eligible loan amount for House loan type : "))
        elif loan_type=='Business':
            bank_emi_expected = int(input("Enter bank_emi_expected for Business : "))
            eligible_loan_amount = int(input("Enter eligible loan amount for Business : ") )

        if (loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected): """
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)

    else:
        if len(a) != 4 or a[0] != '1':
            print("Invalid account number")
        if account_balance < 100000:
            print("Insufficient account balance")
        if loan_type == 'Car' and salary <= 25000:
            print("Invalid loan type or salary")
        elif loan_type == 'House' and salary <= 50000:
            print("Invalid loan type or salary")
        elif loan_type == 'Business' and salary <= 75000:
            print("Invalid loan type or salary")



# calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected)
calculate_loan(1001, 40000, 250000, "Car", 300000, 30)