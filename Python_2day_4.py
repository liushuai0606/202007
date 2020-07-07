# Come on! boy!

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

#方法一
# line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!'% (department1,depart1_m,COURSE_FEES_SEC)
# line2 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!'% (department2,depart2_m,COURSE_FEES_Python)

#方法二
# line1 = 'Department1 name:{:<10}  Manager:{:<10} COURSE FEES:{:<10.2f} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
# line2 = 'Department1 name:{:<10}  Manager:{:<10} COURSE FEES:{:<10.2f} The End!'.format(department2,depart2_m,COURSE_FEES_Python)

#方法三
line1 = f'Department1 name:{department1:<10} Manager:{depart1_m:<10} COURSE FEES:{COURSE_FEES_SEC:<10.2f} The End!'
line2 = f'Department1 name:{department1:<10} Manager:{depart1_m:<10} COURSE FEES:{COURSE_FEES_Python:<10.2f} The End!'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
