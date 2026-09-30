import sys
print(f"wrote this form mi laptop")

if len(sys.argv) > 1:
    print(f"Hello, {sys.argv[1]}.")
else:
    print("Hi..")
