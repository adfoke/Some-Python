import numpy as np

yuan = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("#####################")
print("元:")
print("会:")
print(yuan)
print("运:")
print(yuan*30)
print("世:")
print(yuan*30*12)
print("年:")
print(yuan*30*12*30)

tiangan = np.array([1,2,3,4,5,6,7,8,9,10])
tiangan1 = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
dizhi1 = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

print("#####################")
print("60甲子:")
for i in range(len(tiangan)):
    print(tiangan1[i], dizhi1[i])
for i in range(len(tiangan)):
    if i < 2:
        print(tiangan1[i], dizhi1[i+10])
    else:
        print(tiangan1[i], dizhi1[i-2])
for i in range(len(tiangan)):
    if i < 4:
        print(tiangan1[i], dizhi1[i+8])
    else:
        print(tiangan1[i], dizhi1[i-4])
for i in range(len(tiangan)):
    if i < 6:
        print(tiangan1[i], dizhi1[i+6])
    else:
        print(tiangan1[i], dizhi1[i-6])
for i in range(len(tiangan)):
    if i < 8:
        print(tiangan1[i], dizhi1[i+4])
    else:
        print(tiangan1[i], dizhi1[i-8])
for i in range(len(tiangan)):
    if i < 10:
        print(tiangan1[i], dizhi1[i+2])
    else:
        print(tiangan1[i], dizhi1[i-10])

bagua_xian = np.array([1, 2, 3, 4, 5, 6, 7, 8])
bagua_xian1 = ["乾","兑","离","震","巽","坎","艮","坤"]
bagua_xian2 = ["天","泽","火","雷","风","水","山","地"]
bagua_xianfangwei = ["南","东南","东","东北","西南","西","西北","北"]
bagua_xianb0 = np.array([0b111, 0b110, 0b101, 0b100, 0b011, 0b010, 0b001, 0b000])


bagua_hou = np.array([1, 2, 3, 4, 5, 6, 7, 8])
bagua_hou1 = ["乾","坎","艮","震","巽","离","坤","兑"]
bagua_hou2 = ["天","水","山","雷","风","火","地","泽"]
bagua_houfangwei = ["西北","西","南","东","东南","北","东北","西南"]
bagua_houb0 = np.array([0b111, 0b010, 0b001, 0b100, 0b011, 0b101, 0b000, 0b110])

print("#####################")
print("先天八卦:")
for i in range(len(bagua_xian)):
    print(bagua_xian1[i], bagua_xian2[i],bagua_xianfangwei[i],bin(bagua_xianb0[i]))
print("#####################")
print("后天八卦:")
for i in range(len(bagua_hou)):
    print(bagua_hou1[i], bagua_hou2[i],bagua_houfangwei[i],bin(bagua_houb0[i]) )
    
Hexagram_0b = np.array([[0b000000, 0b000001, 0b000010, 0b00011, 0b000100, 0b000101, 0b000110, 0b000111],
                    [0b001000, 0b001001, 0b001010, 0b001011, 0b001100, 0b001101, 0b001110, 0b001111],
                    [0b010000, 0b010001, 0b010010, 0b010011, 0b010100, 0b010101, 0b010110, 0b010111],
                    [0b011000, 0b011001, 0b011010, 0b011011, 0b011100, 0b011101, 0b011110, 0b011111],
                    [0b100000, 0b100001, 0b100010, 0b100011, 0b100100, 0b100101, 0b100110, 0b100111],
                    [0b101000, 0b101001, 0b101010, 0b101011, 0b101100, 0b101101, 0b101110, 0b101111],
                    [0b110000, 0b110001, 0b110010, 0b110011, 0b110100, 0b110101, 0b110110, 0b110111],
                    [0b111000, 0b111001, 0b111010, 0b111011, 0b111100, 0b111101, 0b111110, 0b111111]])
Hexagram_fuxi = np.array([['坤', '剥', '比', '观', '豫', '晋', '萃', '否'],
                    ['谦', '艮', '蹇', '渐', '小过', '旅', '咸', '遁'],
                    ['师', '蒙', '坎', '涣', '解', '未济', '困', '讼'],
                    ['升', '蛊', '井', '巽', '恒', '鼎', '大过', '垢'],
                    ['复', '颐', '屯', '益', '震', '噬嗑', '随', '无妄'],
                    ['明夷', '贲', '既济', '家人', '丰', '离', '革', '同人'],
                    ['临', '损', '节', '中孚', '归妹', '睽', '兑', '履'],
                    ['泰', '大畜', '需', '小畜', '大壮', '大有', '夬', '乾']])


Hexagram_wenwang = np.array([['乾为天', '坤为地', '水雷屯', '山水蒙', '水天需', '天水讼', '地水师', '水地比'],
                    ['风天小畜', '天泽履', '地天泰', '天地否', '天火同人 ', '火天大有', '地山谦', '雷地豫'],
                    ['泽雷随', '山风蛊', '地泽临', '风地观', '火雷噬嗑', '山火贲', '山地剥', '地雷复'],
                    ['天雷无妄', '山天大畜', '山雷颐', '泽风大过', '坎为水', '离为火', '泽山咸', '雷风恒'],
                    ['天山遁', '雷天大壮', '火地晋', '地火明夷', '风火家人', '火泽睽', '水山蹇', '雷水解'],
                    ['山泽损', '风雷益', '泽天夬', '天风姤', '泽地萃', '地风升', '泽水困', '水风井'],
                    ['泽火革', '火风鼎', '震为雷', '艮为山', '风山渐', '雷泽归妹', '雷火丰', '火山旅'],
                    ['巽为风', '兑为泽', '风水涣', '水泽节', '风泽中孚', '雷山小过', '水火即济', '火水未济']])
    
