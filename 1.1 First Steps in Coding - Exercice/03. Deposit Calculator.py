deposited_sum = float(input())
months = int(input())
yearly_percentage = float(input())

deposit = (deposited_sum * (yearly_percentage/100)) / 12
sum_total = deposited_sum + (months *deposit)
print(sum_total)