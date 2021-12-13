s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""  # triple-delimited
s4 = '''spam\n'''  # triple-delimited
s5 = r"spam\n or \'"  # "raw"

print("Python's a great language")
print('Python\'s a great language')
print('Python is a "great" language')
print("Python is a \"great\" language")
print("""Python's a "great" language""")

query = """
select *
from customers
where state = 'TX'
order by last_name desc
"""

print(len(s1), len(s2))
