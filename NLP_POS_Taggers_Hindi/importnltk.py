import nltk
from nltk.corpus import indian
from nltk.tag import tnt
import string

def hindi_pos_tagging():
    tagged_set = 'hindi.pos'
    data = indian.tagged_sents(tagged_set)
    word_set = indian.sents(tagged_set)
    
    count = 0
    for sen in word_set:
        count = count + 1
        sen = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in sen]).strip()
        print (sen)
    print (count)
    
    train_perc = 0.9
    count = len(data)
    
    train_rows = int(train_perc * count)
    test_rows = train_rows + 1 
    train_data = data[:train_rows]
    test_data = data[test_rows:]
    
    pos_tagger = tnt.TnT()
    pos_tagger.train(train_data)

    word_to_be_tagged = u"उन्होंने ३७ गेंदों में दो चौके और तीन छक्के लगाये ।"
    tokenized = nltk.word_tokenize(word_to_be_tagged)
    tags = pos_tagger.tag(tokenized)
    print("Part-of-Speech Tags for Hindi:")
    print(tags)

def marathi_pos_tagging():
    tagged_set = 'marathi.pos'  
    word_set = indian.sents(tagged_set)
    count = 0
    for sen in word_set:
        count = count + 1
        sen = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in sen]).strip()
        print (sen)
    print (count)
    
    data = indian.tagged_sents(tagged_set)
    train_perc = 0.9
    count = len(data)
    train_rows = int(train_perc * count)
    test_rows = train_rows + 1
    
    train_data = data[:train_rows]
    test_data = data[test_rows:]
    pos_tagger = tnt.TnT()
    pos_tagger.train(train_data)

    word_to_be_tagged = u"तुम्हाला भेटून आनंद झाला."
    tokenized = nltk.word_tokenize(word_to_be_tagged)
    tags = pos_tagger.tag(tokenized)
    print("Part-of-Speech Tags for Marathi:")
    print(tags)

def main():
    while True:
        print("\nLanguage Selection:")
        print("1. Hindi")
        print("2. Marathi")
        print("3. Exit")
        choice = input("Please enter your choice (1-3): ")
        
        if choice == '1':
            hindi_pos_tagging()
        elif choice == '2':
            marathi_pos_tagging()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
