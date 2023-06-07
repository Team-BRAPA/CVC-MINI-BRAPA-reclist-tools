consonants = ['b', 'ch', 'd', 'dj', 'f', 'g', 'h', 'j', 'k', 'l', 'lh', 'm', 'n', 'ng', 'nh', 'p', 'r', 'rr', 'rw', 's', 'sh', 't', 'v', 'w', 'x', 'y', 'z', 'rh']

for consonant in consonants:
    target_lines = [
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav=- {consonant}",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav={consonant} an",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav={consonant} en",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav={consonant} in",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav={consonant} on",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav={consonant} un",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav={consonant} ax",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav={consonant} eh",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav={consonant} ae",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav={consonant} oh",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav=a {consonant}",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav=e {consonant}",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav=i {consonant}",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav=o {consonant}",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav=u {consonant}",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav={consonant} a",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav={consonant} e",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav={consonant} i",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav={consonant} o",
        f"{consonant}a_{consonant}e_{consonant}i_{consonant}o_{consonant}u_{consonant}.wav={consonant} u",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav=an {consonant}",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav=en {consonant}",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav=in {consonant}",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav=on {consonant}",
        f"{consonant}an_{consonant}en_{consonant}in_{consonant}on_{consonant}un_{consonant}.wav=un {consonant}",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav=ax {consonant}",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav=eh {consonant}",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav=ae {consonant}",
        f"{consonant}ax_{consonant}eh_{consonant}ae_{consonant}oh_{consonant}.wav=oh {consonant}"
        ]

    # Open the "oto.ini" file for reading
    with open("oto.ini", "r") as input_file:
        # Read all lines from the file
        lines = input_file.readlines()

    # Open the "edit.txt" file for writing
    with open("edit.txt", "a") as output_file:
        # Iterate over the lines and write the target lines to the output file
        for line in lines:
            if any(target_line in line for target_line in target_lines):
                output_file.write(line)
