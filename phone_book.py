# Phone book dictionary
phone_book = {
    "Brian": {
        "phone": "0722000000",
        "location": "Nairobi"
    },
    "Alice": {
        "phone": "0711223344",
        "location": "Kisumu"
    },
    "John": {
        "phone": "0755667788",
        "location": "Mombasa"
    }
}

# Look up a contact by name
name = "Brian"
print(f"Name: {name}")
print("Phone:", phone_book[name]["phone"])
print("Location:", phone_book[name]["location"])

# You can also print the whole dictionary
print(phone_book)
