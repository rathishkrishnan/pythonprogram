def count_code(str):
    count=0
    for i in range(len(str)-1):
        if(str[i:i+2]=="co" and str[i+3]=="e"):
            count+=1
    print(count)



count_code('aaacodebbb')
count_code('codexxcode')
count_code('cozexxcope')
##
##count_code('aaacodebbb') → 1
##count_code('codexxcode') → 2
##count_code('cozexxcope') → 2
