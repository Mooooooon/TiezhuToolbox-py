import re


class Item:
    def calculate_score(self, attribute):
        score = 0
        for name, value in attribute:
            value = self.remove_brackets(value)
            if name == "攻击力" and "%" in value:
                score += float(value.strip('%')) * 1
            elif name == "防御力" and "%" in value:
                score += float(value.strip('%')) * 1
            elif name == "生命值" and "%" in value:
                score += float(value.strip('%')) * 1
            elif name == "效果命中":
                score += float(value.strip('%')) * 1
            elif name == "效果抗性":
                score += float(value.strip('%')) * 1
            elif name == "速度":
                score += float(value) * 2
            elif name == "暴击伤害" and "%" in value:
                score += float(value.strip('%')) * 1.125
            elif name == "暴击率" and "%" in value:
                score += float(value.strip('%')) * 1.5
            elif name == "攻击力":
                score += float(value) * 3.46 / 39
            elif name == "防御力":
                score += float(value) * 4.99 / 31
            elif name == "生命值":
                score += float(value) * 3.09 / 174
        return score

    def calculate_analysis(self, level, part, primary, primary_value, attribute):
        score = self.calculate_score(attribute)

        if part in ["武器", "铠甲", "头盔"]:
            if level < 3 and score >= 22:
                return "继续强化"
            elif level < 6 and score >= 28:
                return "继续强化"
            elif level < 9 and score >= 34:
                return "继续强化"
            elif level < 12 and score >= 40:
                return "继续强化"
            elif level < 15 and score >= 46:
                return "继续强化"
            elif level == 15 and score >= 52:
                return "建议重铸"
            else:
                return "分数过低，建议放弃"
        else:
            if primary in ["攻击力", "防御力", "生命值"] and "%" not in str(primary_value):
                return "固定值主属性，建议放弃"
            else:
                if level < 3 and score >= 20:
                    return "继续强化"
                elif level < 6 and score >= 26:
                    return "继续强化"
                elif level < 9 and score >= 32:
                    return "继续强化"
                elif level < 12 and score >= 38:
                    return "继续强化"
                elif level < 15 and score >= 44:
                    return "继续强化"
                elif level == 15 and score >= 50:
                    return "建议重铸"
                else:
                    return "分数过低，建议放弃"

    # 定义一个函数来去掉括号及其内部的内容
    def remove_brackets(self, text):
        # 使用正则表达式匹配括号及其内部的内容并替换为空字符串
        result = re.sub(r'[\(\（].*?[\)\）]', '', text)
        # 去除空格
        result = result.strip()
        return result

    def expectant(self, level, attribute):
        expectant = 0
        for name, value in attribute:
            value = self.remove_brackets(value)
            if name == "攻击力" and "%" in value:
                expectant += (4 + 8) / 2
            elif name == "防御力" and "%" in value:
                expectant += (4 + 8) / 2
            elif name == "生命值" and "%" in value:
                expectant += (4 + 8) / 2
            elif name == "效果命中":
                expectant += (4 + 8) / 2
            elif name == "效果抗性":
                expectant += (4 + 8) / 2
            elif name == "速度":
                expectant += (2 + 4) / 2 * 2
            elif name == "暴击伤害" and "%" in value:
                expectant += (4 + 7) / 2 * 1.125
            elif name == "暴击率" and "%" in value:
                expectant += (3 + 5) / 2 * 1.5
            elif name == "攻击力":
                expectant += (33 + 46) / 2 / 39
            elif name == "防御力":
                expectant += (28 + 35) / 2 / 31
            elif name == "生命值":
                expectant += (157 - 202) / 2 / 174
        return expectant / 4 * ((17 - level) // 3)