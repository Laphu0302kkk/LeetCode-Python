#1,2,3,4,5,6,7=28
#2,3,4,5,6,7,8=35
#3,4,5,6,7,8,9=42

class Solution:
    def totalMoney(self, n: int) -> int:
        week=n//7
        dayofweek=n-week*7

        if week==0:
            totalday= n*(1+n)/2
            return int (totalday)
        else:
            totalweek= (week/2)*(2*28+(week-1)*7)
            totalday= (dayofweek)*(week+1+week+dayofweek)/2
            return int (totalweek+totalday)

        