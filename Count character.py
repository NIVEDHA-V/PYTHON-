str1= input("Enter the string: ")
print("Output:"); 
for i in range(0, len(str1)):  
    count = 1;  
    for j in range(i+1, len(str1)):  
        if(str1[i] == str1[j] and str1[i] != ' '):  
            count = count + 1;  
            str1 = str1[:j] + '0' + str1[j+1:];  
    if(count >= 1 and str1[i] != '0'):  
        print(str1[i]," - ",count);
