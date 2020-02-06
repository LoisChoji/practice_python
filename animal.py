def feast(beast, dish):
    if beast[0]==dish[0] and beast[-1] == dish[-1]:
        return "true"
    return "false"
print(feast("freat blue heron", "farlic naan"))