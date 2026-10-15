
marks=(80,35,60,28,90,40)
pass_count=fail_count=0
for values in marks:
    if values>=40:
        pass_count+=1
    else:
        fail_count+=1
print("passed count: ",pass_count)
print("failed count: ",fail_count)