import json

result = []
with open('text_77.json', 'w', encoding='utf-8') as loly:
    with open ('text_7.txt', 'r+', encoding='utf-8') as loly_new:
        profit = {}
        for line in loly_new:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i)
                            for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({'средняя прибыль': round(average_profit)})
    json.dump(result, loly)
    