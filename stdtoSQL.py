import sys
reload(sys)
print sys.setdefaultencoding('utf-8')
class Stuinfo:
    def _init_(self):
        self.Stu= [
            {"Sno": "1", "Sname": "name", "ChineseScore": 64, "MathsScore": 34, "EnglishScore": 94, "ComputerScore": 83},
            {"Sno": "2", "Sname": "name", "ChineseScore": 44, "MathsScore": 24, "EnglishScore": 44, "ComputerScore": 71},
            {"Sno": "3", "Sname": "name", "ChineseScore": 74, "MathsScore": 35, "EnglishScore": 74, "ComputerScore": 93},
            {"Sno": "4", "Sname": "name", "ChineseScore": 94, "MathsScore": 54, "EnglishScore": 24, "ComputerScore": 73}]
        self.attribute = {"Sno": "学号",
                          "Sname":"姓名",
                          "ChineseScore": "语文成绩",
                          "MathsScore": "数学成绩",
                          "EnglishScore": "英语成绩",
                          "ComputerScore": "计算机成绩"
                          }
   def _add(self):
        '''添加'''
        singleInfo = {}
        for i in self.attribute:
            if "Score" in i:
                singleInfo[i] = int(raw_input(self.attribute[i] + "\n"))
            else:
                singleInfo[i] = raw_input(self.attribute[i] + "\n").strip()
        self.Stu.append(singleInfo)
        print "添加成功"
        for i in singleInfo:
            print i, "=", singleInfo[i]

    def _del(self):
        """删除学号为Sno的记录"""
        Sno = raw_input("学号:\n")
        self.Stu.remove(self.__getInfo(Sno))
        print "删除成功OK"

    def _update(self):
        """更新数据"""
        Sno = raw_input("学号\n").strip()
        prefix = "修改"
        updateOperate = {"1": "ChineseScore",
                         "2": "MathsScore",
                         "3": "EnglishScore",
                         "4": "ComputerScore"}
        for i in updateOperate:
            print i, "-->", prefix + self.attribute[updateOperate[i]]
        getOperateNum = raw_input("选择操作:\n")
        if getOperateNum:
            getNewValue = int(raw_input("输入新的值:\n"))
            record = self.__getInfo(Sno)
            record[updateOperate[getOperateNum]] = getNewValue
            print "修改" + record["Sname"] + "的" + str(updateOperate[getOperateNum]) + "成绩=", getNewValue, "\n成功OK"
   def _getInfo(self):
        """查询数据"""
        while True:
            print "1->学号查询  2->条件查询 3->退出"
            getNum = raw_input("选择：\n")
            if getNum == "1":
                Sno = raw_input("学号：\n")
                print  filter(lambda record: record["Sno"] == Sno, self.Stu)[0]
            elif getNum == "2":
                print "ChineseScore 语文成绩；", "MathsScore 数学成绩；", "EnglishScore 英语成绩；", "ComputerScore 计算机成绩；"
                print "等于 ==，小于 <, 大于 > ,大于等于 >=,小于等于<= ,不等于!="
                print "按如下格式输入查询条件 eg: ChineseScore>=60 "
                expr = raw_input("条件：\n")
                Infos = self.__getInfo(expr=expr)
                if Infos:
                    print "共%d记录" % len(Infos)
                    for i in Infos:
                        print i
                else:
                    print "记录为空"
            elif getNum == "3":
                break
            else:
                pass

    def __getInfo(self, Sno=None, expr=""):
        """查询数据
           根据学号 _getInfo("111")
           根据分数 _getInfo("EnglishSorce>80")"""
        if Sno:
            return filter(lambda record: record["Sno"] == Sno, self.Stu)[0]
        for operate in [">=", ">", "<=", "<", "==", "!="]:
            if operate in expr:
                gradeName, value = expr.split(operate)
                return filter(lambda record: eval(repr(record[gradeName.strip()]) + operate + value.strip()), self.Stu)
        return {}

    def _showAll(self):
        """显示所有记录"""
        for i in self.Stu:
            print i
   @staticmethod
    def test():
        """测试"""
        _StuInfo = StuInfo()
        while True:
            print "1->录入数据  2->修改数据  3->删除数据 4->查询数据 5->查看数据 6->退出"
            t = raw_input("选择：\n")
            if t == "1":
                print "录入数据"
                _StuInfo._add()
            elif t == "2":
                print "修改数据"
                _StuInfo._update()
            elif t == "3":
                print "删除数据"
                _StuInfo._del()
            elif t == "4":
                print "查询数据"
                _StuInfo._getInfo()
            elif t == "5":
                print "显示所有记录"
                _StuInfo._showAll()
            elif t == "6":
                break
            else:
                pass


if __name__ == "__main__":
    StuInfo.test
