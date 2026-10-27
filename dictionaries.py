# Creating a dictionary representing a user profile
user_profile = {
    "username": "coder123",
    "email": "coder@example.com",
    "age": 25,
    "is_active": True
}

# 1. Accessing values using their keys
print(user_profile["username"])  # Output: coder123

# 2. Modifying an existing value
user_profile["age"] = 26

# 3. Adding a new key-value pair
user_profile["location"] = "San Francisco"

# 4. Removing a key-value pair
del user_profile["is_active"]

print(user_profile)
