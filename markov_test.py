import markovify


if __name__ == '__main__':
    with open('tweets.csv') as f:
        text = f.read()
    model = markovify.Text(text)
    print(model.make_short_sentence(100))
