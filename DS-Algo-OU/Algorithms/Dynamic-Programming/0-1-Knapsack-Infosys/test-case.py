csv_content = """test_case_name,weights,volumes,values,max_weight,max_volume,expected_value,expected_items
"General Case","1|2|3|4","2|1|4|5","10|8|12|15",5,6,22,"(1, 2, 10)|(3, 4, 12)"
"Volume is Limiting","10|20|30","1|1|1","60|100|120",50,2,220,"(20, 1, 100)|(30, 1, 120)"
"Weight is Limiting","1|1|1","10|20|30","60|100|120",2,50,220,"(1, 20, 100)|(1, 30, 120)"
"Edge Case (Zero Weight Capacity)","1|2|3","1|2|3","10|20|30",0,5,0,""
"Edge Case (Zero Volume Capacity)","1|2|3","1|2|3","10|20|30",5,0,0,""
"Edge Case (Empty Items)","","","",10,10,0,""
"All Items Fit","1|1|1","2|2|2","100|100|100",5,7,300,"(1, 2, 100)|(1, 2, 100)|(1, 2, 100)"
"No Items Fit","10|20","10|20","100|200",5,5,0,""
"Tricky Case (Corrected)","5|3|4|2","2|4|5|3","60|50|70|30",5,5,70,"(4, 5, 70)"
"""

with open('knapsack_test_cases.csv', 'w') as f:
    f.write(csv_content)

print("CSV file created successfully.")