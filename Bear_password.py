def validate_password(password):

def password_generator(x):
    N = len(x)
    num_combinations = 2**N
    for i in range(num_combinations):
        password = bin(i + num_combinations)[3:]
        print(password)


def main():
    x = [2, 0]
    password_generator(x)

main()