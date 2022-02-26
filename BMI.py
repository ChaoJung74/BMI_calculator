height = float(input('請輸入身高(cm)：'))
weight = float(input('請輸入體重(kg)：'))
BMI = weight/(height/100)**2
if BMI < 18.5:
	print('你的BMI數值是：', BMI, '體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('你的BMI數值是：', round(BMI, 2), '屬正常範圍')
elif BMI >= 24 and BMI < 27:
	print('你的BMI數值是：', round(BMI, 2), '體重過重')
elif BMI >= 27 and BMI < 30:
	print('你的BMI數值是：', round(BMI, 2), '輕度肥胖')
elif BMI >=30 and BMI < 35:
	print('你的BMI數值是：', round(BMI, 2), '中度肥胖')
else:
	print('你的BMI數值是：', round(BMI, 2), '重度肥胖')