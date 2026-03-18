GLOBAL_COUNTER = 0

users = ["alice", "bob", "charlie"]

numbers = list(range(100))  # unnecessary list creation


def expensive_function(x):
    return x * x


def process_users():
    global GLOBAL_COUNTER

    results = []
    text = ""

    for user in users:
        for i in range(5):

            # global variable modified inside loop
            GLOBAL_COUNTER += 1

            # expensive function inside loop
            val = expensive_function(i)

            # repeated attribute access
            print(user.upper())
            length = len(user.upper())

            # string concatenation inside loop
            text += user

            # list append inside nested loop
            results.append(val)

            # bare except
            try:
                risky = 10 / (i - 2)
            except:
                print("error")

            # overly broad exception
            try:
                number = int(user)
            except Exception:
                pass

    return results


def another_test():
    data = []

    for i in range(3):
        for j in range(3):

            # expensive call inside nested loop
            val = expensive_function(i + j)

            # append inside nested loop
            data.append(val)

    return data


if __name__ == "__main__":
    process_users()
    another_test()