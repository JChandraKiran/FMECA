import numpy as np
FMECA_dict = {'capacitor':[3,['open','change in value','short'],['45%','35%','20%']],
				'diode':[4,['open','short','drift','change in_value'],['10%','20%','15%','15%']],
				'transistor':[5,['open','short','drift','change in value','kkllll'],['5%','10%','20%','30%','35%']]}

output = [ [ 0 for i in range(45) ] for j in range(35) ]
#output = np.zeros(shape=(50,50))
current_row = 0
data = np.genfromtxt('C:\\Users\\KIRAN\\Desktop\\New.csv',delimiter=',',dtype = str)
rows = data.shape[0]
columns = data.shape[1]
print(data)
for i in range(rows):
	for j in range(FMECA_dict[data[i][1].lower()][0]):
		output[current_row][0] = str(i+1)+'-'+str(int(j+1))
		output[current_row][1] = data[i][0]
		output[current_row][2] = (data[i][1]).capitalize()
		output[current_row][3] = FMECA_dict[data[i][1].lower()][1][j]
		output[current_row][3] = FMECA_dict[data[i][1].lower()][2][j]
		current_row +=1
print(output)