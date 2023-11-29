class Item:
    def calculate_score(attribute):
        score = 0
        for name, value in attribute:
            if name == "攻击力" and "%" in value:
                score += float(value.strip('%')) * 1
            elif name == "防御力" and "%" in value:
                score += float(value.strip('%')) * 1
            elif name == "生命值" and "%" in value:
                score += float(value.strip('%')) * 1
            elif name == "效果命中":
                score += float(value.strip('%')) * 1
            elif name == "效果抵抗":
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