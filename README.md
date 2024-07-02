# Unique Short Name Generator (Multilingual)
Given a unique string (like a serial number) it outputs a compound word that's easier for humans to recall and label.
For instance, what's easier to deal with in a team:
* A) "The buck converter burnt out on 7184bc7e, and mbc8z3eff needs a new SD card"
* B) "Replace the black light on LimpCaiman, and format the SD card for CoolJirafa"

You can also control the max length of your Labels or number of compound words the string is made from depending on how much complexity vs. compactness you need. You can also select words in English, Spanish, or for extra complexity in a multi-lingual team, Spanglish mixtures.
 
![PXL_20240701_194930078](https://github.com/Digital-Naturalism-Laboratories/Unique-Short-Name-Generator--Multilingual-/assets/742627/dde7de9e-ed08-4e1b-ad1e-4b3c676a3f81)

# Usage
## Filter the database
The *main thing of value here* is that there is an excel document with a list of common english and spanish nouns, verbs, adjectives, and animals with a built in filter letting you choose the max word length for making your compound label.

 ![image](https://github.com/Digital-Naturalism-Laboratories/Unique-Short-Name-Generator--Multilingual-/assets/742627/6d31f025-b67a-4b75-b345-bd860e6ef759)

Just choose how long you want the longest words it chooses to be, and you can see the stats on how many unique combos will come out of this. 

We are planning on making like 100 projects deployed on a raspberry pi, and wanted short catchy labels, so we don't REALLY need that much uniqueness (1 million combos should be fine). So we only chose 2 word names with a max word length of 6 letters.

| MAX WORDLENGTH | 2 word combos  |                |                  |         | if 3 word combos                 |                |
| -------------- | -------------- | -------------- | ---------------- | ------------------------- | -------------- | -------------- |
| 6              | ENGLISH COMBOS | Spanish Combos | Spanglish Combos | Spanish OR English Combos | ENGLISH COMBOS | Spanish Combos | Spanglish Combos | Spanish OR English Combos |
|Total Unique words | 184,680  | 250,400  | 1,154,444  | 435,080      | 24,591,168       | 14,664,000       | 3.11E+08 | 39,255,168 |


![image](https://github.com/Digital-Naturalism-Laboratories/Unique-Short-Name-Generator--Multilingual-/assets/742627/6811b662-3da2-4dc1-b302-a28690a7cbf7)

## Do Some coding





## Sources
I compiled my wordlists from these sources, cleaned them up, got rid of weird formatting, and sorted them into categories

Ajectives # https://github.com/bryanmylee/zoo-ids/blob/master/src/adjectives.ts
colors #from https://github.com/andreasonny83/unique-names-generator/blob/main/src/dictionaries/animals.ts
Animales https://github.com/Contraculto/corpora_es/blob/master/data%2Fanimales%2Fanimales.json
Animales 2 https://es.m.wikipedia.org/wiki/Wikiproyecto:Animales/Lista
Ajectivos https://es.m.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol
Animales3 https://es.m.wikibooks.org/wiki/Ingl%C3%A9s/Vocabulario/Animales
Verbs https://7esl.com/english-verbs/

