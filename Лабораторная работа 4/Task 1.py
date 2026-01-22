# TODO решите задачу
def task() -> float:
    import json
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
        total_sum = 0
        for item in data:
            score = float(item['score'])
            weight = float(item['weight'])
            total_sum += score * weight
            result = round(total_sum, 3)
        return result
print(task())
