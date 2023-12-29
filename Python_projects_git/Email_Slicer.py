email = input("Enter the Email:").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
format_ = f"Your user name is {username} and your domain is {domain}"
print(format_)