# import spacy
import spacy

# import warning to fix W007 problem, cause by en_core_web_sm no vector problem
import warnings
warnings.filterwarnings("ignore", message=r"\[W007\]", category=UserWarning)

# load 'en_core_web_md' and 'en_core_web_sm'
nlp = spacy.load('en_core_web_md')
nlp1 = spacy.load('en_core_web_sm')

# cat source : wikipedia
cat = ['The cat (Felis catus) is a domestic species of small carnivorous mammal.',
       'It is the only domesticated species in the family Felidae and is commonly referred to as the domestic cat or house cat to distinguish it from the wild members of the family.',
       'Cats are commonly kept as house pets but can also be farm cats or feral cats; the feral cat ranges freely and avoids human contact. ',
       'Domestic cats are valued by humans for companionship and their ability to kill rodents.',
       'About 60 cat breeds are recognized by various cat registries.']


# monkey source : wikipedia
monkey = ['Monkey is a common name that may refer to most mammals of the infra order Simiiformes, also known as the simians.',
          'Traditionally, all animals in the group now known as simians are counted as monkeys except the apes, which constitutes an incomplete paraphyletic grouping; however, in the broader sense based on cladistics, apes (Hominoidea) are also included, making the terms monkeys and simians synonyms in regards to their scope.',
          'Many monkey species are tree-dwelling (arboreal), although there are species that live primarily on the ground, such as baboons.',
          'Most species are mainly active during the day (diurnal).',
          'Monkeys are generally considered to be intelligent, especially the Old World monkeys.']

# banana source : wikipedia
banana = ['A banana is an elongated, edible fruit – botanically a berry – produced by several kinds of large herbaceous flowering plants in the genus Musa.',
          'In some countries, bananas used for cooking may be called "plantains", distinguishing them from dessert bananas.',
          'The fruit is variable in size, color, and firmness, but is usually elongated and curved, with soft flesh rich in starch covered with a rind, which may be green, yellow, red, purple, or brown when ripe.',
          'The fruits grow upward in clusters near the top of the plant.',
          'Almost all modern edible seedless (parthenocarp) bananas come from two wild species – Musa acuminata and Musa balbisiana.']

# fish source : wikipedia
fish = ['Fish are aquatic, craniate, gill-bearing animals that lack limbs with digits.',
        'Included in this definition are the living hagfish, lampreys, and cartilaginous and bony fish as well as various extinct related groups.',
        'Approximately 95% of living fish species are ray-finned fish, belonging to the class Actinopterygii, with around 99% of those being teleosts.',
        'Most fish are ectothermic ("cold-blooded"), allowing their body temperatures to vary as ambient temperatures change, though some of the large active swimmers like white shark and tuna can hold a higher core temperature.',
        'Fish can acoustically communicate with each other, most often in the context of feeding, aggression or courtship.']

# set start score = 0
cat_fish_score_md = 0
cat_monkey_score_md = 0
cat_banana_score_md = 0
fish_monkey_score_md = 0
monkey_banana_score_md = 0

# set start score = 0
cat_fish_score_sm = 0
cat_monkey_score_sm = 0
cat_banana_score_sm = 0
fish_monkey_score_sm = 0
monkey_banana_score_sm = 0

# check similarity cat-fish using en_core_web_md
print("-------------cat-fish similarity--(en_core_web_md)---------------")
for token in cat:
    token = nlp(token)
    for token_ in fish:
        token_ = nlp(token_)
        print(token.similarity(token_))
        cat_fish_score_md += token.similarity(token_)


# check similarity monkey-cat using en_core_web_md
print("-------------monkey-cat similarity--(en_core_web_md)---------------")
for token in cat:
    token = nlp(token)
    for token_ in monkey:
        token_ = nlp(token_)
        print(token.similarity(token_))
        cat_monkey_score_md += token.similarity(token_)

# check similarity banana-cat using en_core_web_md
print("-------------banana-cat similarity--(en_core_web_md)---------------")
for token in cat:
    token = nlp(token)
    for token_ in banana:
        token_ = nlp(token_)
        print(token.similarity(token_))
        cat_banana_score_md += token.similarity(token_)

# check similarity fish monkey using en_core_web_md
print("-------------fish-monkey similarity--(en_core_web_md)---------------")
for token in fish:
    token = nlp(token)
    for token_ in monkey:
        token_ = nlp(token_)
        print(token.similarity(token_))
        fish_monkey_score_md += token.similarity(token_)

# check similarity monkey-banana using en_core_web_md
print("-------------monkey-banana similarity--(en_core_web_md)---------------")
for token in monkey:
    token = nlp(token)
    for token_ in banana:
        token_ = nlp(token_)
        print(token.similarity(token_))
        monkey_banana_score_md += token.similarity(token_)


# check similarity cat-fish using en_core_web_sm
print("-------------cat-fish similarity--(en_core_web_sm)---------------")
for token in cat:
    token = nlp1(token)
    for token_ in fish:
        token_ = nlp1(token_)
        print(token.similarity(token_))
        cat_fish_score_sm += token.similarity(token_)

# check similarity monkey-cat using en_core_web_sm
print("-------------monkey-cat similarity--(en_core_web_sm)---------------")
for token in cat:
    token = nlp1(token)
    for token_ in monkey:
        token_ = nlp1(token_)
        print(token.similarity(token_))
        cat_monkey_score_sm += token.similarity(token_)

# check similarity banana-cat using en_core_web_sm
print("-------------banana-cat similarity--(en_core_web_sm)---------------")
for token in cat:
    token = nlp1(token)
    for token_ in banana:
        token_ = nlp1(token_)
        print(token.similarity(token_))
        cat_banana_score_sm += token.similarity(token_)

# check similarity fish monkey using en_core_web_sm
print("-------------fish-monkey similarity--(en_core_web_sm)---------------")
for token in fish:
    token = nlp1(token)
    for token_ in monkey:
        token_ = nlp1(token_)
        print(token.similarity(token_))
        fish_monkey_score_sm += token.similarity(token_)

# check similarity monkey-banana using en_core_web_sm
print("-------------monkey-banana similarity--(en_core_web_sm)---------------")
for token in monkey:
    token = nlp1(token)
    for token_ in banana:
        token_ = nlp1(token_)
        print(token.similarity(token_))
        monkey_banana_score_sm += token.similarity(token_)

# print result
print(f"cat_fish_score_md = {cat_fish_score_md}")
print(f"cat_monkey_score_md = {cat_monkey_score_md}")
print(f"cat_banana_score_md = {cat_banana_score_md}")
print(f"fish_monkey_score_md = {fish_monkey_score_md}")
print(f"monkey_banana_score_md = {monkey_banana_score_md}\n")

print(f"cat_fish_score_sm = {cat_fish_score_sm}")
print(f"cat_monkey_score_sm = {cat_monkey_score_sm}")
print(f"cat_banana_score_sm = {cat_banana_score_sm}")
print(f"fish_monkey_score_sm = {fish_monkey_score_sm}")
print(f"monkey_banana_score_sm = {monkey_banana_score_sm}\n")

# the highest score of similarity is fish-monkey....the lowest score is cat-banana
# it seem the sample size is too small

# sm (small) vs md (medium)
# en_core_web_sm (which don't ship with word vectors and only use context-sensitive tensors) is no vectors loaded,
# so the result of the Doc.similarity method will be based on the tagger
# which cannot give useful similarity judgements which don't ship with word vectors and only use context-sensitive tensors
# en_core_web_md - the vector function included, and it is suitable bigger size of data
