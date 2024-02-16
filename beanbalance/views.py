from django.shortcuts import render
from beanbalance.models import Balance, History
from decimal import Decimal
from django.utils import timezone


# Create your views here.
def payment_action(request):
    (balances, created) = Balance.objects.get_or_create(id=0)
    context = {'bobBalance':balances.bob, 'jeremyBalance':balances.jeremy,
               'coworker1Balance': balances.coworker1, 'coworker2Balance':balances.coworker2,
               'coworker3Balance': balances.coworker3, 'coworker4Balance':balances.coworker4,
               'coworker5Balance': balances.coworker5}
    
    if(request.method=='POST'):
        # List containing the balance of each coworker
        balanceList = [balances.bob, balances.jeremy, balances.coworker1, balances.coworker2,
                       balances.coworker3, balances.coworker4, balances.coworker5]
        # List containing the cost of each drink
        costs = [Decimal(request.POST.get('textBob')), Decimal(request.POST.get('textJeremy')),
                 Decimal(request.POST.get('text1')), Decimal(request.POST.get('text2')),
                 Decimal(request.POST.get('text3')), Decimal(request.POST.get('text4')), Decimal(request.POST.get('text5'))]
        # For loop calculating who would have the lowest negative balance upon paying
        newBalances = []
        for i in range(len(balanceList)):
            potentialBalance = balanceList[i] - (sum(costs[:i]) + sum(costs[i+1:]))
            newBalances.append(potentialBalance)

        # Saving indices to list. Keep track of each balance even after sorting.
        enumeratedBalances = list(enumerate(newBalances))
        # Sorting it by preference of who to pay. index 0 being the preferred choice.
        sortedBalances = sorted(enumeratedBalances, key=lambda x: x[1], reverse=True)
        #print(sortedBalances)

        # Subtract the sum of non-payers coffees from balance.
        balanceList[sortedBalances[0][0]] = sortedBalances[0][1]

        # Add balance of coffee cost to those not paying
        for i in range(1, 7):
            index = sortedBalances[i][0]
            balanceList[index] += costs[index]
        
        # Set database values and save them
        balances.bob = balanceList[0]
        balances.jeremy = balanceList[1]
        balances.coworker1 = balanceList[2]
        balances.coworker2 = balanceList[3]
        balances.coworker3 = balanceList[4]
        balances.coworker4 = balanceList[5]
        balances.coworker5 = balanceList[6]
        balances.save()
        #print(balanceList)
        names = ['Bob', 'Jeremy', 'Coworker1', 'Coworker2', 'Coworker3', 'Coworker4', 'Coworker5']
        newHistory = History(buyer = names[sortedBalances[0][0]],  date = timezone.now())
        newHistory.save()

    context = {'bobBalance':balances.bob, 'jeremyBalance':balances.jeremy,
               'coworker1Balance': balances.coworker1, 'coworker2Balance':balances.coworker2,
               'coworker3Balance': balances.coworker3, 'coworker4Balance':balances.coworker4,
               'coworker5Balance': balances.coworker5}
    
    return render(request, 'payment.html', context)

def history_action(request):
    return render(request, 'history.html', {'buyers' : History.objects.all().order_by('-date')})