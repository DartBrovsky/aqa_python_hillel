from lesson_15.user import User, SchoolUser, UniversityUser

# print(User.name)
# User.print_user_name()

new_user: User = User("Serhii", 90, "0000 1111 2222 3333", 888)

new_user.print_user_name()
#
# print(new_user)
# print(len(new_user))

# user_for_adding: User = User("Serhii", 80)

# print(new_user + user_for_adding)
# print(new_user < user_for_adding)
# print(new_user > user_for_adding)
#
# print("K" in new_user)
#
# print(new_user == user_for_adding)
#
# print(new_user['name'])
# print(new_user['age'])

# new_user.name = "Vladislav"
# new_user.age = 190

# del new_user.age
# del new_user.name
#
# print(new_user.name)


print(User.__dict__)
print(new_user.__dict__)

print(new_user)
school_user: SchoolUser = SchoolUser("Serhii", 90, "0000 1111 2222 3333", 888)
school_user.set_card_number("1111 2222 3333 4444")

new_user.pay()

print(school_user.get_credit_card_number)


# del new_user

def instantiate_an_object_and_get_dict(user: User):
    print(type(user))


instantiate_an_object_and_get_dict(school_user)
