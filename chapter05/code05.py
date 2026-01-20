s='波士顿凯尔特人总冠军'
# 编码 str->bytes
scode=s.encode(errors='replace') # 默认是utf-8 ,因为utf-8中文占3个字节
print(scode)

scode_gbk=s.encode('gbk',errors='replace') # gbk中中文占2个字节
print(scode_gbk)

# 编码中的出错问题
s2='耶✌'
scode_error=s2.encode('gbk',errors='replace') # 遇见无法解析的字符，用?代替
print(scode_error)

scode_error=s2.encode('gbk',errors='ignore') # 遇见无法解析的字符，忽略
print(scode_error)

# scode_error=s2.encode('gbk',errors='strict')  # 这一行会报错
# print(scode_error)

# 解码过程bytes->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))
