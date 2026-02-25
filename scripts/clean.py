import json

# 讀取 raw.txt
data = {}

with open("data/raw.txt", "r") as f:
    for line in f:
        year, value = line.strip().split(",")
        data[int(year)] = float(value)

values = list(data.values())

average_population = sum(values) / len(values)
growth_2024_2030 = (data[2030] - data[2024]) / data[2024]
cagr_2024_2100 = (data[2100] / data[2024]) ** (1 / (2100 - 2024)) - 1

result = {
    "population_data": data,
    "average_population": round(average_population, 3),
    "growth_2024_2030": round(growth_2024_2030, 4),
    "cagr_2024_2100": round(cagr_2024_2100, 6)
}

with open("data/cleaned.json", "w") as f:
    json.dump(result, f, indent=4)

print("Data cleaned successfully.")
