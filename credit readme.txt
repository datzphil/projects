--type, which indicates the type of payments: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff", or it is not specified at all, show the error message.

--payment, that is a monthly payment. For --type=diff the payment is different each month, so we can't calculate periods or principal, therefore, its combination with --payment is invalid, too:

--principal is used for calculations of both types of payment. You can get its value knowing the interest, annuity payment and periods.

--periods parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment and principal.

--interest is specified without a percent sign. Note that it may accept a floating-point value. Our credit calculator can't calculate the interest, so these parameters are incorrect:

input 4/5 parameter in order to find the 5th

example:
python creditcalc.py --type=diff --principal=30000 --periods=14 --interest=10