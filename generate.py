import random

def generate_words(file_name):
    with open(file_name, 'r') as f:
        words = f.read().split()
    return words

def generate_output(words):
    output = []
    for i in range(12):
        output.append(random.choice(words))
    return ' '.join(output)

def main():
    words = generate_words("input.txt")
    outputs = []
    for i in range(500000):
        outputs.append(generate_output(words))
    with open("output.txt", "w") as f:
        for output in outputs:
            f.write(output + "\n")

if __name__ == "__main__":
    main()
