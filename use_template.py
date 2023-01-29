import re

f = open("yyylp_temp.sty", 'r', encoding="utf-8")

file_content = f.read()

# print(file_content)

params = re.findall(r'\byyy\w+', file_content)

for p in params:
    print(p[3:] + " :", end=" ")
    in_to_replace = input()
    file_content = file_content.replace(p, in_to_replace)
    
# print(file_content)
    
newf = open("yyylp.sty", 'w', encoding="utf-8")
newf.write(file_content)
print("success!")