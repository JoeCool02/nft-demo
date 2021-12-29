import sys

print(f"Number of arguments: {len(sys.argv)} arguments.")
print(f"Argument List: {str(sys.argv)}")

for word in sys.argv:
    print(word)
