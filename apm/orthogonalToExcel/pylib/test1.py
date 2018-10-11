import re

str='账户名：空，不存在，超长，超短，正常'
r='[：，]'
# all = re.split('/:/|，', str.strip())
all = re.split(r, str.strip())
print(all)