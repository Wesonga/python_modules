
languages = {
    "Python",
    "JavaScript",
    "C++",
    "Java",
}

print(languages)

# 1. Adding an item
languages.add("Ruby")

# 2. Removing an item
languages.remove("C++")

# 3. Set Operations (Intersection & Union)
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "Java", "JavaScript"}

# Find items present in BOTH sets (Intersection)
common_skills = frontend.intersection(backend)
print(common_skills)  # Output: {'JavaScript'}

# Combine all unique items from both sets (Union)
all_skills = frontend.union(backend)
print(all_skills)  # Output: {'HTML', 'CSS', 'JavaScript', 'Python', 'Java'}
