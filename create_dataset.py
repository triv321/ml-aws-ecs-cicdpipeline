import pandas as pd
import numpy as np
import random
from itertools import product

# Define extensive building blocks for review generation
actors = ["Tom Hanks", "Meryl Streep", "Leonardo DiCaprio", "Viola Davis", "Denzel Washington", 
          "Emma Stone", "Robert Downey Jr.", "Scarlett Johansson", "Brad Pitt", "Cate Blanchett",
          "Joaquin Phoenix", "Jennifer Lawrence", "Daniel Day-Lewis", "Frances McDormand", "Anthony Hopkins"]

directors = ["Steven Spielberg", "Martin Scorsese", "Christopher Nolan", "Quentin Tarantino", 
            "Greta Gerwig", "Denis Villeneuve", "Bong Joon-ho", "Kathryn Bigelow", "Jordan Peele",
            "Ava DuVernay", "James Cameron", "Spike Lee", "Chloe Zhao", "Alfonso Cuarón", "Taika Waititi"]

genres = ["action", "drama", "comedy", "science fiction", "horror", "romance", "thriller", 
          "documentary", "adventure", "fantasy", "animation", "musical", "western", "crime", "war"]

film_elements = ["cinematography", "screenplay", "visual effects", "soundtrack", "editing", 
                "costume design", "production design", "makeup", "character development", "plot", 
                "pacing", "dialogue", "action sequences", "emotional impact", "world-building"]

positive_adjectives = ["amazing", "brilliant", "captivating", "dazzling", "exceptional", 
                      "fascinating", "gripping", "heartfelt", "innovative", "jaw-dropping", 
                      "masterful", "nuanced", "outstanding", "powerful", "remarkable",
                      "stunning", "thought-provoking", "unforgettable", "visionary", "wonderful"]

negative_adjectives = ["awful", "boring", "confusing", "disappointing", "embarrassing", 
                      "forgettable", "grating", "horrible", "incomprehensible", "juvenile", 
                      "lazy", "mediocre", "nonsensical", "overrated", "predictable",
                      "repetitive", "shallow", "tedious", "unbearable", "wooden"]

positive_phrases = [
    "This movie was absolutely {adj}, the {element} was superb and the plot was gripping.",
    "{actor}'s performance in this {genre} film was {adj}.",
    "Under {director}'s direction, the {element} was {adj}.",
    "A true masterpiece of cinema with {adj} {element}.",
    "An enjoyable ride from start to finish. A must-see for any {genre} fan.",
    "One of the best films I've seen this year. {director}'s vision really shines through.",
    "The performances were outstanding, especially {actor} who delivered an emotional tour de force.",
    "Visually {adj} with an incredible soundtrack that perfectly complements the story.",
    "I was on the edge of my seat the entire time. The suspense was masterfully built.",
    "A beautiful story told with sensitivity and grace. I was moved to tears.",
    "Brilliant {element} with {adj} moments that feel authentic and memorable.",
    "The special effects were groundbreaking and added so much to the overall experience.",
    "A thought-provoking film that will stay with you long after the credits roll.",
    "The chemistry between {actor} and the supporting cast was electric and believable.",
    "An instant classic that deserves all the awards it's been nominated for.",
    "I couldn't stop smiling throughout the entire film. Pure joy from start to finish.",
    "{director} took some bold creative risks that really paid off.",
    "A perfect blend of humor, action, and heart. Thoroughly entertaining.",
    "The cinematography was breathtaking - every frame looked like a painting.",
    "A refreshing take on a familiar genre. Original and captivating.",
    "The twist ending completely caught me by surprise. Brilliantly executed!",
    "The character development was outstanding. I felt like I knew these people.",
    "A powerful message delivered through stunning visuals and compelling storytelling.",
    "The world-building was incredibly detailed and immersive.",
    "I've already seen it three times and notice new details with each viewing.",
    "A masterclass in pacing - not a single dull moment in the entire film.",
    "The supporting cast was exceptional, adding depth to an already rich story.",
    "Seamlessly blends elements of {genre} and {genre} into something completely fresh.",
    "{actor} gives what might be the performance of their career.",
    "The script is tight and intelligent, respecting the audience's intelligence.",
    "{director}'s expert direction elevates what could have been standard {genre} fare.",
    "A film that takes big swings and lands every single one of them.",
    "The {element} creates an atmosphere that pulls you in from the first frame.",
    "I found myself completely lost in the world this film creates.",
    "Balances humor and pathos with remarkable skill.",
    "A rare sequel that actually improves upon the original in every way.",
    "The kind of film that reminds you why you fell in love with cinema.",
    "Technical brilliance combined with genuine emotional resonance.",
    "A refreshing reminder that blockbusters can still be art.",
    "Sets a new standard for the {genre} genre.",
    "{actor} and {actor} have chemistry that leaps off the screen.",
    "The {element} deserves special recognition for its contribution to the film's success.",
    "A perfect marriage of form and content that's all too rare these days.",
    "Manages to feel both timeless and urgently contemporary.",
    "I can't remember the last time I was so thoroughly entertained.",
    "A film that takes its time but rewards your patience abundantly.",
    "Reminded me why I love movies in the first place.",
    "The kind of storytelling that stays with you for days afterward.",
    "Every single department of the production is firing on all cylinders."
]

negative_phrases = [
    "I would not recommend this {genre} film to anyone. It was {adj} and poorly written.",
    "{actor}'s performance was {adj} and unconvincing.",
    "{director} completely failed to deliver with this {adj} mess.",
    "A complete waste of time. The characters were one-dimensional and the story was predictable.",
    "I was so disappointed. The trailer was much better than the actual movie.",
    "The plot had so many holes you could drive a truck through it.",
    "Terrible acting across the board. I couldn't connect with any of the characters.",
    "The pacing was so slow I nearly fell asleep multiple times.",
    "A pretentious mess that tries too hard to be profound but fails miserably.",
    "The dialogue was cringe-worthy and felt completely unnatural.",
    "The special effects looked cheap and took me out of the experience completely.",
    "I've never wanted to walk out of a theater so badly in my life.",
    "A complete waste of {actor}'s talent. The script gave them nothing to work with.",
    "The ending made absolutely no sense and ruined any redeeming qualities the film had.",
    "Painfully derivative, borrowing the worst elements from better movies.",
    "The musical score was overbearing and distracting throughout.",
    "Characters made decisions that defied all logic and common sense.",
    "The attempts at humor fell completely flat. Not a single laugh in the theater.",
    "{director} seemed to have no clear vision for what this film was trying to be.",
    "Nonsensical plot twists added purely for shock value with no substance.",
    "I kept checking my watch wondering when it would finally be over.",
    "Tries to juggle too many storylines and fails to develop any of them properly.",
    "The cinematography was dull and uninspired, mostly static shots with no creativity.",
    "A sequel that completely misunderstands what made the original special.",
    "Despite a huge budget, it looked surprisingly cheap and hastily made.",
    "The tone was wildly inconsistent, jumping between serious and comedic awkwardly.",
    "I want those two hours of my life back. Absolutely nothing to recommend here.",
    "A textbook example of style over substance with nothing meaningful to say.",
    "Feels like it was written by an algorithm rather than a human with actual emotions.",
    "Wastes the talents of {actor} on material far beneath their abilities.",
    "The {element} was so {adj} it became almost comical.",
    "Fails to understand even the basics of what makes a {genre} film work.",
    "Shockingly bad given the caliber of people involved in making it.",
    "A cynical cash grab with no artistic merit whatsoever.",
    "So derivative that it borders on plagiarism of better films.",
    "The {element} felt like it belonged to an entirely different movie.",
    "Not a single authentic moment in its entire runtime.",
    "{director}'s worst film by a considerable margin.",
    "Couldn't decide what kind of movie it wanted to be.",
    "Even hardcore fans of the franchise will be disappointed.",
    "The editing was so choppy it gave me a headache.",
    "A collection of scenes rather than a coherent narrative.",
    "Manages to be both boring and exhausting at the same time.",
    "Completely squanders an interesting premise.",
    "The character motivations made absolutely no sense.",
    "A bloated mess that could have been cut by at least an hour.",
    "The {element} was so distracting it pulled me out of the story repeatedly.",
    "Tries to be clever but ends up feeling smug and self-satisfied.",
    "Insulting to the audience's intelligence.",
    "Every creative decision seems to be the wrong one."
]

mixed_positive_phrases = [
    "Despite some {adj} {element}, the strong third act made up for it.",
    "Not perfect by any means, but {actor}'s performance elevates the material.",
    "The plot was somewhat predictable, but {director}'s execution was still enjoyable.",
    "While the dialogue occasionally felt forced, the overall story was engaging.",
    "A bit too long, but with enough memorable moments to make it worthwhile.",
    "The first half dragged slightly, but the finale was absolutely spectacular.",
    "Some CGI issues aside, the practical effects and stunts were impressive.",
    "Not quite as good as the original, but still a solid sequel that respects its roots.",
    "The subplot was unnecessary, but the main story was compelling enough.",
    "{director}'s ambition sometimes exceeds their grasp, but I admire the effort.",
    "Uneven in parts but ultimately satisfying as a {genre} film.",
    "Falls short of greatness but still delivers solid entertainment value.",
    "Although it suffers from pacing issues, the strong performances make it worth watching.",
    "The script has flaws, but the direction and acting elevate the material.",
    "Not as profound as it thinks it is, but still an engaging viewing experience.",
    "While it borrows heavily from other {genre} films, it still manages to feel fresh enough.",
    "Occasionally veers into melodrama, but pulls back just in time.",
    "Some narrative choices were questionable, but the emotional core rings true.",
    "{actor}'s performance saves what could have been a mediocre film.",
    "A flawed but fascinating addition to {director}'s filmography.",
    "The middle section lags, but the opening and conclusion are strong.",
    "Somewhat conventional in its approach, but executes the formula extremely well.",
    "A few scenes don't work, but the ones that do are truly memorable.",
    "The tone is inconsistent at times, but when it finds its groove it really works.",
    "Not as revolutionary as critics claim, but still a very good film on its own terms."
]

mixed_negative_phrases = [
    "Good performances couldn't save the {adj} script and unfocused direction.",
    "Beautiful visuals by {director}, but unfortunately style over substance with a hollow core.",
    "A few funny moments couldn't make up for the overall tedious experience.",
    "The premise had potential, but the execution fell completely flat.",
    "Great soundtrack wasted on a film that doesn't deserve it.",
    "The opening sequence was promising, but it was all downhill from there.",
    "{actor} tries their best, but they're stranded in a sea of clichés and tired tropes.",
    "Occasionally hints at greatness, only to retreat to mediocrity.",
    "The emotional moments felt manipulative rather than earned.",
    "While technically competent, the story lacks any heart or originality.",
    "{actor} shines in an otherwise forgettable film.",
    "Gorgeous cinematography can't disguise the empty core of this story.",
    "Shows flashes of what could have been, but ultimately disappoints.",
    "Starts strong but completely falls apart in its third act.",
    "Too many ideas and not enough focus doom what could have been interesting.",
    "The ambition is admirable, but the execution is deeply flawed.",
    "A talented cast wasted on a script that gives them nothing to work with.",
    "Visually impressive but emotionally hollow.",
    "One or two good scenes lost in an otherwise tedious experience.",
    "The director clearly has talent, but needs much better material.",
    "Tries to say something profound but ends up saying nothing at all.",
    "Not even {actor}'s charisma could save this misguided project.",
    "Had all the ingredients for success but somehow still fails to satisfy.",
    "The first half shows promise that the second half completely squanders.",
    "A few genuine moments of brilliance buried in an otherwise mediocre film."
]

# Function to generate a large set of reviews using templates and components
def generate_massive_dataset(count):
    reviews = []
    sentiments = []
    
    # Generate positive reviews
    for _ in range(count // 2):
        template = random.choice(positive_phrases)
        actor = random.choice(actors)
        director = random.choice(directors)
        genre = random.choice(genres)
        element = random.choice(film_elements)
        adj = random.choice(positive_adjectives)
        
        review = template.format(
            actor=actor, 
            director=director, 
            genre=genre, 
            element=element, 
            adj=adj
        )
        reviews.append(review)
        sentiments.append("positive")
    
    # Generate negative reviews
    for _ in range(count // 3):
        template = random.choice(negative_phrases)
        actor = random.choice(actors)
        director = random.choice(directors)
        genre = random.choice(genres)
        element = random.choice(film_elements)
        adj = random.choice(negative_adjectives)
        
        review = template.format(
            actor=actor, 
            director=director, 
            genre=genre, 
            element=element, 
            adj=adj
        )
        reviews.append(review)
        sentiments.append("negative")
    
    # Generate mixed-positive reviews
    for _ in range(count // 8):
        template = random.choice(mixed_positive_phrases)
        actor = random.choice(actors)
        director = random.choice(directors)
        genre = random.choice(genres)
        element = random.choice(film_elements)
        adj = random.choice(negative_adjectives)  # Intentionally using negative adj for contrast
        
        review = template.format(
            actor=actor, 
            director=director, 
            genre=genre, 
            element=element, 
            adj=adj
        )
        reviews.append(review)
        sentiments.append("positive")
    
    # Generate mixed-negative reviews
    for _ in range(count // 8):
        template = random.choice(mixed_negative_phrases)
        actor = random.choice(actors)
        director = random.choice(directors)
        genre = random.choice(genres)
        element = random.choice(film_elements)
        adj = random.choice(negative_adjectives)
        
        review = template.format(
            actor=actor, 
            director=director, 
            genre=genre, 
            element=element, 
            adj=adj
        )
        reviews.append(review)
        sentiments.append("negative")
    
    # Generate more complex reviews by combining templates
    remaining = count - len(reviews)
    for _ in range(remaining):
        if random.random() > 0.5:
            # Complex positive review
            templates = random.sample(positive_phrases, k=random.randint(2, 3))
            review_parts = []
            for template in templates:
                actor = random.choice(actors)
                director = random.choice(directors)
                genre = random.choice(genres)
                element = random.choice(film_elements)
                adj = random.choice(positive_adjectives)
                
                part = template.format(
                    actor=actor, 
                    director=director, 
                    genre=genre, 
                    element=element, 
                    adj=adj
                )
                review_parts.append(part)
            
            reviews.append(" ".join(review_parts))
            sentiments.append("positive")
        else:
            # Complex negative review
            templates = random.sample(negative_phrases, k=random.randint(2, 3))
            review_parts = []
            for template in templates:
                actor = random.choice(actors)
                director = random.choice(directors)
                genre = random.choice(genres)
                element = random.choice(film_elements)
                adj = random.choice(negative_adjectives)
                
                part = template.format(
                    actor=actor, 
                    director=director, 
                    genre=genre, 
                    element=element, 
                    adj=adj
                )
                review_parts.append(part)
            
            reviews.append(" ".join(review_parts))
            sentiments.append("negative")
    
    # Add original core reviews for quality assurance
    core_positive = [
        "This movie was absolutely fantastic, the acting was superb and the plot was gripping.",
        "A true masterpiece of cinema. The cinematography was breathtaking.",
        "An enjoyable ride from start to finish. A must-see for any fan of the genre.",
        "One of the best films I've seen this year. The director's vision really shines through."
    ]
    
    core_negative = [
        "I would not recommend this film to anyone. It was boring and poorly written.",
        "A complete waste of time. The characters were one-dimensional and the story was predictable.",
        "I was so disappointed. The trailer was much better than the actual movie.",
        "The plot had so many holes you could drive a truck through it."
    ]
    
    reviews.extend(core_positive)
    sentiments.extend(["positive"] * len(core_positive))
    reviews.extend(core_negative)
    sentiments.extend(["negative"] * len(core_negative))
    
    # Shuffle the dataset while preserving pairs
    combined = list(zip(reviews, sentiments))
    random.shuffle(combined)
    reviews, sentiments = zip(*combined)
    
    return list(reviews), list(sentiments)

# Generate a massive dataset with thousands of reviews
reviews, sentiments = generate_massive_dataset(5000)

# Shuffle the dataset while preserving pairs
combined = list(zip(reviews, sentiments))
random.shuffle(combined)
reviews, sentiments = zip(*combined)

data = {
    'review': reviews,
    'sentiment': sentiments
}

df = pd.DataFrame(data)

# Print dataset statistics
positive_count = sentiments.count("positive")
negative_count = sentiments.count("negative")
print(f"\nDataset created with {len(reviews):,} total reviews:")
print(f"- Positive reviews: {positive_count:,} ({positive_count/len(reviews)*100:.1f}%)")
print(f"- Negative reviews: {negative_count:,} ({negative_count/len(reviews)*100:.1f}%)")
print(f"- Average review length: {sum(len(r) for r in reviews) / len(reviews):.1f} characters")

# Calculate some additional statistics
review_lengths = [len(r) for r in reviews]
print(f"- Shortest review: {min(review_lengths)} characters")
print(f"- Longest review: {max(review_lengths)} characters")
print(f"- Median review length: {pd.Series(review_lengths).median():.1f} characters")

# Save the data to a local CSV file
df.to_csv('imdb_data.csv', index=False)

print("\nLocal dataset 'imdb_data.csv' created successfully.")
print(f"Total file size: {df.memory_usage(deep=True).sum() / (1024*1024):.2f} MB")