from math import log, ceil, pow
import argparse

# python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
parser = argparse.ArgumentParser(description="credit calculator")
parser.add_argument("--type", type=str, help="enter annuity or diff", choices=["annuity", "diff"])
parser.add_argument("--payment", type=int, help="enter monthly payment")
parser.add_argument("--principal", type=int, help="used for calculations of both types of payment")
parser.add_argument("--periods", type=int, help=" denotes the # of months and/or years needed to repay the credit")
parser.add_argument("--interest", type=float, help="specified without a percent sign")
args = parser.parse_args()

if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()
elif (args.payment or args.principal or args.periods or args.interest) <= 0:
    print("Incorrect parameters")
    exit()
elif args.type == "annuity" and args.periods is None and args.payment is None and args.principal is None:
    print("Incorrect")
    exit()
elif args.principal is None:  # credit payment
    interest_rate = (args.interest / 100) / 12
    credit = ceil(args.payment / ((interest_rate * pow((1 + interest_rate), args.periods)) /
                                  ((1 + interest_rate) ** args.periods - 1)))
    print(f'Your credit principal = {credit}')
elif args.type == "annuity" and args.periods is not None:  # annuity payment
    interest_rate = (args.interest / 100) / 12
    annuity = ceil(args.principal * ((interest_rate * pow((1 + interest_rate), args.periods)) /
                                     (pow((1 + interest_rate), args.periods) - 1)))
    overpayment = (abs(int(annuity) * args.periods - int(args.principal)))
    print(f"Your annuity payment = {annuity}!")
    print(f"Overpayment = {overpayment}")
elif args.type == "diff":  # diff payments
    m = 1
    total_payment = 0
    interest_rate = (args.interest / 100) / 12
    while m <= args.periods:
        monthly_payment = (args.principal / args.periods) + interest_rate * (args.principal -
                                                                             (args.principal * (m - 1)) / args.periods)
        print(f"Month {m}: paid out {round(ceil(monthly_payment))}")
        m += 1
        total_payment += round(ceil(monthly_payment))
    overpayment = (total_payment - args.principal)
    print()
    print(f"Overpayment = {overpayment}")
elif args.periods is None and args.interest is not None:  # period time
    interest_rate = (args.interest / 100) / 12
    value = ceil(log((args.payment / (args.payment - interest_rate * args.principal)),
                     1 + interest_rate))
    overpayment = (abs(int(args.payment) * value - int(args.principal)))
    if value == 1:
        print(f"It takes {value} month to repay the credit")
        print(f"Overpayment = {overpayment}")
    elif value <= 12:
        print(f"It takes {value} months to repay the credit")
        print(f"Overpayment = {overpayment}")
    else:
        print(f"It takes {value // 12} years and {value % 12} months to repay the credit")
        print(f"Overpayment = {overpayment}")
else:
    print("Incorrect parameters")
    exit()