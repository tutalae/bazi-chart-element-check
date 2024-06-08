from lunar_python import Lunar, Solar
from datetime import datetime

def analyze_bazi_chart(year, month, day, hour, minute):
    # Function to interpret the BaZi chart
    def interpret_bazi_chart(bazi_chart, chinese_to_english):
        pillar_names = ["Year Pillar", "Month Pillar", "Day Pillar", "Hour Pillar"]

        interpreted_chart = []
        for idx, pillar in enumerate(bazi_chart):
            heavenly_stem = pillar[0]
            earthly_branch = pillar[1]

            interpreted_stem = chinese_to_english[heavenly_stem]
            interpreted_branch = chinese_to_english[earthly_branch]

            interpreted_chart.append((pillar_names[idx], interpreted_stem, interpreted_branch))

        return interpreted_chart

    # Function to interpret the elements
    def interpret_elements(elements, chinese_to_english_elements):
        return [chinese_to_english_elements[element] for element in elements]

    # Chinese to English translation dictionaries
    chinese_to_english = {
        "庚": "Yang Metal", "辛": "Yin Metal", "壬": "Yang Water", "癸": "Yin Water",
        "甲": "Yang Wood", "乙": "Yin Wood", "丙": "Yang Fire", "丁": "Yin Fire",
        "戊": "Yang Earth", "己": "Yin Earth",
        "子": "Rat", "丑": "Ox", "寅": "Tiger", "卯": "Rabbit", "辰": "Dragon",
        "巳": "Snake", "午": "Horse", "未": "Goat", "申": "Monkey", "酉": "Rooster",
        "戌": "Dog", "亥": "Pig"
    }

    chinese_to_english_elements = {"金": "Metal", "木": "Wood", "水": "Water", "火": "Fire", "土": "Earth"}

    # Convert specified date to Lunar date
    specific_datetime = datetime(year, month, day, hour, minute)
    solar_date = Solar(specific_datetime.year, specific_datetime.month, specific_datetime.day,
                       specific_datetime.hour, specific_datetime.minute, specific_datetime.second)
    lunar_date = Lunar.fromSolar(solar_date)

    # Get BaZi chart from Lunar date
    bazi_chart = lunar_date.getBaZi()
    bazi_ziwuxing = lunar_date.getBaZiWuXing()
    animal = lunar_date.getAnimal()

    # Interpret the BaZi chart
    interpreted_chart = interpret_bazi_chart(bazi_chart, chinese_to_english)

    # Interpret the elements
    interpreted_elements = [
        [chinese_to_english_elements[element] for element in element_pair]
        for element_pair in bazi_ziwuxing
    ]

    # Function to check the elements in the BaZi chart
    def check_five_elements(heavenly_stems, earthly_branches):
        # Define the five elements and their corresponding branches
        five_elements = {
            "Metal": ["申", "酉"], "Water": ["子", "亥"], "Wood": ["寅", "卯"],
            "Fire": ["巳", "午"], "Earth": ["辰", "丑", "戌", "未"] # All four Earth symbols included
        }

        # Initialize counters for each element
        element_counts = {element: 0 for element in five_elements}

        # Check the elements in the BaZi chart
        for stem, branch in zip(heavenly_stems, earthly_branches):
            for element, branches_list in five_elements.items():
                if branch in branches_list:
                    element_counts[element] += 1

        return element_counts

    # Check the elements in the BaZi chart
    element_counts = check_five_elements(
        [pillar[0] for pillar in bazi_chart],
        [pillar[1] for pillar in bazi_chart]
    )

    # Print the interpreted BaZi chart
    print(f"Animal: {animal}")
    print("BaZi chart:")
    for pillar in interpreted_chart:
        print(f"     {pillar[0]}: {pillar[1]} {pillar[2]}")

    # Print the interpreted BaZi elements
    print("BaZi elements:")
    for element_pair in interpreted_elements:
        print(f"     {element_pair[0]} {element_pair[1]}")

    # Print the counts of the five elements
    print("Element counts:")
    total_elements_present = sum(1 for count in element_counts.values() if count > 0)
    print(f"     Total different elements present: {total_elements_present}")

    # Print the detailed counts of each element
    element_counts = {value: 0 for key, value in chinese_to_english_elements.items()}
    for combination in bazi_ziwuxing:
        for element in combination:
            element_counts[chinese_to_english_elements[element]] += 1

    print("Element counts (detailed):")
    for element, count in element_counts.items():
        print(f"     {element}: {count}")

    return bazi_chart, bazi_ziwuxing, total_elements_present

# Example usage
chart, ziwuxing, elements = analyze_bazi_chart(1998, 9, 14, 1, 0)
print("chinese chart:", chart)
print("chinese ziwuxing", ziwuxing)