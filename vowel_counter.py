def count_vowels():
    user_string = input("Enter a string: ").lower()

    vowel = ["a", "e", "i", "o", "u"]

    vowel_count = 0

    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0

    for letter in user_string:
        if letter in vowel:
            vowel_count += 1
            if letter == "a":
                a_count += 1
            elif letter == "e":
                e_count += 1
            elif letter == "i":
                i_count += 1
            elif letter == "o":
                o_count += 1
            elif letter == "u":
                u_count += 1

    print(
        f"Vowel count: {vowel_count}\n"
        f"A: {a_count}\n"
        f"E: {e_count}\n"
        f"I: {i_count}\n"
        f"O: {o_count}\n"
        f"U: {u_count}"
    )


count_vowels()
