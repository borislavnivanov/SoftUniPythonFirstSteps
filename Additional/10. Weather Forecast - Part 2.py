temperature = float(input())
#
# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold

if (temperature > 5.00) and (temperature <= 11.90):
    print('Cold')
elif (temperature >= 12.00) and (temperature <= 14.90):
    print('Cool')
elif (temperature >= 15.00) and (temperature <= 20.00):
    print('Mild')
elif (temperature >= 20.10) and (temperature <= 25.90):
    print('Warm')
elif (temperature >= 26.00) and (temperature <= 35.00):
    print('Hot')
else:
    print('unknown')
