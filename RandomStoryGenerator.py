import random
from random_word import RandomWords

class StoryGenerator:
    def __init__(self):
        self.words = []

    def get_words(self):
        for i in range(3):
            word = input(f"Enter word {i + 1}: ")
            self.words.append(word)

    def generate_story(self):
        r = RandomWords()
        story = []
        for word in self.words:
            synonyms = r.get_synsets(word)
            if synonyms:
                random_synonym = random.choice(synonyms)
                story.append(random_synonym.definition())
            else:
                story.append(f"Unable to generate story for '{word}'")

        return ' '.join(story)


def main():
    generator = StoryGenerator()
    generator.get_words()
    story = generator.generate_story()

    print("\nGenerated Story:")
    print(story)


if __name__ == "__main__":
    main()
