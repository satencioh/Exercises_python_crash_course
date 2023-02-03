first_name = 'Luisa'
last_name = 'Hernandez'
full_name = f"{first_name} {last_name}"
print(full_name)

#other way to format a string
full_name_other = "{} {}".format(first_name, last_name)
print(full_name_other)

#handles whitespaces in strings
favorite_language = 'python '
print(favorite_language)
#remove whitespace the rigth side at the end
favorite_language = favorite_language.rstrip()
favorite_language

fav_fruit = ' apple '
#remove whitespace the rigth side at the end
print(fav_fruit.rstrip())
#remove whitespace the left side at the end
print(fav_fruit.lstrip())
#remove whitespace from both side
print(fav_fruit.strip())