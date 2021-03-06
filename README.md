# synonym-wordcloud-gen
A simple word cloud generator based on the WordCloud package on Python. Enhnaced so that user can input key words and the program calls on WordNet to add synonyms of those words onto the word cloud while keeping the key words the main focus

Dependencies 
* Numpy
* Pandas (not used in current iteration)
* NLTK
* WorcCloud
* Matplotlib

Upon initial install, uncomment line 14 to download NLTK WordNet data for use. Line 14 can be commented after this download.

Upon running the program, the user is prompted to enter the key words via the terminal. Gibberish and random words are allowed to accomodate acronyms, names, etc. However, no synonyms will be found for these cases. Otherwise, if the word exists in WordNet, the program will pull all the available synonyms form the database for use. An empty user input indicates that the user has given all the key words. The key words are weighted (having a higher frequency) more than synonyms, which will cause the WordCloud's generate_from_Frequencies attribute to make those words appear substantially larger than the synonyms.

An example is shown below with the key words: Integrity, Honesty, Inclusion, Personal Responsibility, Diversity, and Social Awareness

![Example Word Cloud](https://github.com/edwinpalegre/synonym-wordcloud-gen/blob/master/example.png)

# Outstanding Issues
* Current code pulls ALL possible synonyms from Word Net. Next step insludes finding a better approach that can be used to make the synonyms more relevant to the situation. Las time, we used raw_input.n.01 which is the first noun. Since the uses for these words are all adjectives, that might be a possible avenue to try and fix

* Frequency of the key words seems to get altered when merging the lst and add_syn dictionaries together into the word_lst dictionary. The word_lst dictionary overwrites some of the keywords' values to reflect the default value given to the synonyms. Despite going through and removing duplicates of the key words from the two libraries prior to merging, this is still the outstanding issue to fix.
