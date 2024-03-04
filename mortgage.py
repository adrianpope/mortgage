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
