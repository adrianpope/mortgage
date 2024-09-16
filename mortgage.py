import numpy as np
import scipy.optimize as so

def monthly_payment(principal, apr, months):
    interest_per_month = apr/100.0/12.0
    return principal*interest_per_month/(1 - (1 + interest_per_month)**-months)

def loan_summary(principal, apr, months):
    mp = monthly_payment(principal, apr, months)
    total = mp*months
    interest = total - principal
    print('years       = %12.2f' % (months/12.0) )
    print('avg monthly = %12s' % "{:,.2f}".format(mp) )
    print('principal   = %12s' % "{:,.2f}".format(principal) )
    print('interest    = %12s' % "{:,.2f}".format(interest) )
    print('total       = %12s' % "{:,.2f}".format(total) )
    print('intprin     = %13.3f' % (interest/principal) )
    return

def monthly_series(principal, apr, months, extra_per_month=0.0):
    mp = monthly_payment(principal, apr, months)
    interest_per_month = apr/100.0/12.0
    principal_remaining = principal
    interest_arr=np.zeros(months)
    principal_arr=np.zeros(months)
    remaining_arr=np.zeros(months)
    paid_arr=np.zeros(months)
    for i in range(months):
        interest_owed = principal_remaining*interest_per_month
        interest_arr[i] = interest_owed
        principal_paid = mp - interest_owed
        principal_arr[i] = principal_paid
        principal_remaining -= (principal_paid + extra_per_month)
        remaining_arr[i] = principal_remaining
        paid_arr[i] = (i+1)*mp
        if principal_remaining < mp:
            break
    last_payment = principal_remaining*(1.0 + interest_per_month)
    principal_arr[i] = principal_remaining
    interest_arr[i] = principal_remaining*interest_per_month
    paid_arr[i:] = paid_arr[i-1] + last_payment
    months_arr = np.arange(months)
    return (months_arr, principal_arr, interest_arr, remaining_arr, paid_arr)

def crossover(series0, series1):
    n0=len(series0)
    n1=len(series1)
    n=min(n0,n1)
    for i in range(n-1):
        if (series0[i] < series1[i]) != (series0[i+1] < series1[i+1]):
            break
    return i

def loan_summary_extra_monthly(principal, apr, months, extra_per_month=0.0):
    mp = monthly_payment(principal, apr, months)
    interest_per_month = apr/100.0/12.0
    principal_remaining = principal
    for i in range(months):
        interest_owed = principal_remaining*interest_per_month
        principal_paid = mp - interest_owed
        principal_remaining -= (principal_paid + extra_per_month)
        if principal_remaining < mp:
            break
    last_payment = principal_remaining*(1.0 + interest_per_month)
    total = (i+1)*(mp + extra_per_month) + last_payment
    interest = total - principal
    print('years       = %12.2f' % ((i+2)/12.0) )
    print('avg monthly = %12s' % "{:,.2f}".format(mp + extra_per_month) )
    print('principal   = %12s' % "{:,.2f}".format(principal) )
    print('interest    = %12s' % "{:,.2f}".format(interest) )
    print('total       = %12s' % "{:,.2f}".format(total) )
    print('savings     = %12s' % "{:,.2f}".format(mp*months - total) )
    print('int/prin    = %13.3f' % (interest/principal) )
    return

def loan_length_extra_monthly(principal, apr, months, extra_per_month=0.0):
    mp = monthly_payment(principal, apr, months)
    interest_per_month = apr/100.0/12.0
    principal_remaining = principal
    for i in range(months):
        interest_owed = principal_remaining*interest_per_month
        principal_paid = mp - interest_owed
        principal_remaining -= (principal_paid + extra_per_month)
        if principal_remaining < mp:
            break
    last_payment = principal_remaining*(1.0 + interest_per_month)
    total = (i+1)*(mp + extra_per_month) + last_payment
    interest = total - principal
    return i+1+last_payment/mp

def find_monthly_extra(principal, apr, months, payoff_month):
    extra = so.brentq(lambda x:loan_length_extra_monthly(principal, apr, months, x) - payoff_month,0,10000)
    return extra

def loan_summary_extra_yearly(principal, apr, months, extra_per_year=0.0, first_extra_month=11):
    mp = monthly_payment(principal, apr, months)
    interest_per_month = apr/100.0/12.0
    principal_remaining = principal
    total = 0.0
    for i in range(months):
        interest_owed = principal_remaining*interest_per_month
        principal_paid = mp - interest_owed
        principal_remaining -= principal_paid
        total += mp
        if (i >= first_extra_month) & ((i - first_extra_month)%12 == 0):
            print('%d'%i,end=' ')
            principal_remaining -= extra_per_year
            total += extra_per_year
        if principal_remaining < mp:
            break
    last_payment = principal_remaining*(1.0 + interest_per_month)
    total += last_payment
    interest = total - principal
    print('')
    print('years       = %12.2f' % ((i+2)/12.0) )
    print('avg monthly = %12s' % "{:,.2f}".format(mp + extra_per_year/12.0) )
    print('principal   = %12s' % "{:,.2f}".format(principal) )
    print('interest    = %12s' % "{:,.2f}".format(interest) )
    print('total       = %12s' % "{:,.2f}".format(total) )
    print('savings     = %12s' % "{:,.2f}".format(mp*months - total) )
    print('int/prin    = %13.3f' % (interest/principal) )
    return
