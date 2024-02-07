deposit_amount = float(input())
deposit_time = int(input())
yearly_rate = float(input()) / 100

accumulated_interest = ((deposit_amount * yearly_rate) / 12) * deposit_time
final_amount = deposit_amount + accumulated_interest

print(final_amount)
