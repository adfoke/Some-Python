# tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
# dizhi = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
# bagua_xian = ["乾","兑","离","震","巽","坎","艮","坤"]
# bagua_xian = ["天","泽","火","雷","风","水","山","地"]
# bagua_xianfangwei = ["南","东南","东","东北","西南","西","西北","北"]
# bagua_hou = ["乾","坎","艮","震","巽","离","坤","兑"]
# bagua_hou = ["天","水","山","雷","风","火","地","泽"]
# bagua_houfangwei = ["西北","西","南","东","东南","北","东北","西南"]
# Hexagram_fuxi = [['坤', '剥', '比', '观', '豫', '晋', '萃', '否'],
#                     ['谦', '艮', '蹇', '渐', '小过', '旅', '咸', '遁'],
#                     ['师', '蒙', '坎', '涣', '解', '未济', '困', '讼'],
#                     ['升', '蛊', '井', '巽', '恒', '鼎', '大过', '垢'],
#                     ['复', '颐', '屯', '益', '震', '噬嗑', '随', '无妄'],
#                     ['明夷', '贲', '既济', '家人', '丰', '离', '革', '同人'],
#                     ['临', '损', '节', '中孚', '归妹', '睽', '兑', '履'],
#                     ['泰', '大畜', '需', '小畜', '大壮', '大有', '夬', '乾']]

# Hexagram_wenwang = [['乾为天', '坤为地', '水雷屯', '山水蒙', '水天需', '天水讼', '地水师', '水地比'],
#                     ['风天小畜', '天泽履', '地天泰', '天地否', '天火同人 ', '火天大有', '地山谦', '雷地豫'],
#                     ['泽雷随', '山风蛊', '地泽临', '风地观', '火雷噬嗑', '山火贲', '山地剥', '地雷复'],
#                     ['天雷无妄', '山天大畜', '山雷颐', '泽风大过', '坎为水', '离为火', '泽山咸', '雷风恒'],
#                     ['天山遁', '雷天大壮', '火地晋', '地火明夷', '风火家人', '火泽睽', '水山蹇', '雷水解'],
#                     ['山泽损', '风雷益', '泽天夬', '天风姤', '泽地萃', '地风升', '泽水困', '水风井'],
#                     ['泽火革', '火风鼎', '震为雷', '艮为山', '风山渐', '雷泽归妹', '雷火丰', '火山旅'],
#                     ['巽为风', '兑为泽', '风水涣', '水泽节', '风泽中孚', '雷山小过', '水火即济', '火水未济']]
#1元 = 12会 = 129600年
#1会 = 30运 = 10800年
#1运 = 12世 = 360年
#1世        = 30年

from collections import namedtuple

class HeavenlyStemsEarthlyBranches:
    def __init__(self, stem_list, branch_list):
        self.combination = namedtuple('Combination', ['heavenly_stem', 'earthly_branch'])
        self.combinations = []
        for i in range(60):
            stem_index = i % 10
            branch_index = i % 12
            combination = self.combination(stem_list[stem_index], branch_list[branch_index])
            self.combinations.append(combination)

heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

heavenly_branches_earthly_branches = HeavenlyStemsEarthlyBranches(heavenly_stems, earthly_branches)
combinations = heavenly_branches_earthly_branches.combinations

#Accessing the elements of a named tuple
for combination in combinations:
     print(combination.heavenly_stem + combination.earthly_branch)