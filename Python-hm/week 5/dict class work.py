
# Problem 1: Book Info
# --------------------
# You have a book dict:

book = {
    "title":  "Clean Code",
    "author": "Robert Martin",
    "year":   2008,
    "pages":  464,
}

# Do the following in order:
#   1. Print the book's title and author.
print(f"Title:  { book["title"]} \nAuthor: { book["author"]}")

#   2. Change the year to 2009.
book["year"]=2009

#   3. Add a new key "available" with value True.
book["available"] = True

#   4. Print the final dict and its length (number of keys).
print("Updated dict: ", book)
print("Number of Keys: " , len(book.keys()))


print("-"*40)
# Expected output:
#     Title: Clean Code
#     Author: Robert Martin
#     Updated dict: {'title': 'Clean Code', 'author': 'Robert Martin', 'year': 2009, 'pages': 464, 'available': True}
#     Number of keys: 5


# Problem 2: Class Schedule (nested dict)
# ---------------------------------------
# You have a nested dict for a class schedule:

schedule = {
      "Monday":    {"morning": "Math",    "afternoon": "Physics"},
      "Tuesday":   {"morning": "Biology", "afternoon": "History"},
     "Wednesday": {"morning": "Math",    "afternoon": "Art"},
}

# Do the following:
#   1. Print the Monday MORNING class.
print("Monday morning: ", schedule["Monday"]["morning"])

#   2. Print the Wednesday AFTERNOON class.
print("Wednesday afternoon: ", schedule["Wednesday"]["afternoon"])

#   3. Check if Tuesday has a "morning" key — print True/False.
print("Tuesday has morning: ", 'morning' in schedule["Tuesday"])

#   4. Change the Wednesday afternoon class to "Music".
schedule["Wednesday"]["afternoon"] = "Music"

#   5. Print the updated Wednesday dict.
print("Updated Wednesday: ", schedule["Wednesday"])


print("-"*40)

# Expected output:
#     Monday morning: Math
#     Wednesday afternoon: Art
#     Tuesday has morning: True
#     Updated Wednesday: {'morning': 'Math', 'afternoon': 'Music'}


# Problem 3: Library Catalog (dict with list values)
# --------------------------------------------------
# You have a library where each category maps to a LIST of books:

library = {
    "fiction": ["1984", "Brave New World", "Dune"],
    "tech":    ["Clean Code", "The Pragmatic Programmer"],
    "history": ["Sapiens", "Guns Germs and Steel", "1776"],
}

# Do the following:
#   1. Print how many books are in the "fiction" category.
print("Fiction count: ",len(library["fiction"]))

#   2. Print the SECOND book in the "tech" category.
print("Second tech book: ", library["tech"][1])

#   3. Add "Civilization" to the "history" list.
library["history"][-1] = "Civilization"

#   4. Add a new category "science" with one book:
#      "A Brief History of Time".
library["science"] = "A Brief History of Time"

#   5. Print the entire library.
print("Library: ", library)

print("-"*40)

# Expected output:
#     Fiction count: 3
#     Second tech book: The Pragmatic Programmer
#     Library: {'fiction': ['1984', 'Brave New World', 'Dune'], 'tech': ['Clean Code', 'The Pragmatic Programmer'], 'history': ['Sapiens', 'Guns Germs and Steel', '1776', 'Civilization'], 'science': ['A Brief History of Time']}


# Problem 4 (H.W): Company Structure (deeply nested)
# --------------------------------------------
# You have a company dict with departments. Each department has
# a manager, team size, and a list of projects:

company = {
    "ceo": "Ahmed",
    "departments": {
            "engineering": {
                "manager": "Sara",
                "team_size": 12,
                "projects": ["Backend API", "Mobile App"],
            },
            "design": {
                "manager": "Omar",
                "team_size": 5,
                "projects": ["Website Redesign"],
        },
    },
}

# Do the following:
#   1. Print the CEO's name.
print("CEO: ",company["ceo"])

#   2. Print the engineering manager's name.
print("Engineering manager: ", company["departments"]["engineering"]["manager"])

#   3. Print the design team's size.
print("Design team size: ", company["departments"]["design"]["team_size"])

#   4. Print the FIRST engineering project.
print("First engineering project: ", company["departments"]["engineering"]["projects"][0])

#   5. Print the TOTAL team size (engineering + design).
print("Total team size: ", company["departments"]["design"]["team_size"] + company["departments"]["engineering"]["team_size"])

#   6. Update the design team's size to 6.
company["departments"]["design"]["team_size"] = 6

#   7. Add a new department "marketing" with manager "Lina",
#      team_size 3, and an empty project list.
company = {
    "ceo": "Ahmed",
    "departments": {
            "marketing": {
                "manager": "Lina",
                "team_size": 3,
                "projects": {},
            }
    }
}
#   8. Print the marketing department after adding it.
print("Marketing: ", company["departments"]["marketing"])

# Expected output:
#     CEO: Ahmed
#     Engineering manager: Sara
#     Design team size: 5
#     First engineering project: Backend API
#     Total team size: 17
#     Marketing: {'manager': 'Lina', 'team_size': 3, 'projects': []}