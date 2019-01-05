**HELLO IT'S A ME**

Ok, so what's this you ask?

This is a completely useless piece of software I've made due to educational purposes of my ML training, say hello and pay repsect.

What does it do? It recommends you what anime to watch based on your MyAnimeList list and what's popular today. **It only uses genres 'couse that's exactly what I wanted.**

It works with unnoficial MyAnimeListApi - https://jikan.docs.apiary.io

So, now I'm going to explain how it works, LET'S A-GO

**STEPS**

1) Fetch all animes from top20 list

2) Fetch all user animes

3) Create dataset

4) Make prediction based on genres using Term Frequency (TF) and Inverse Document Frequency (IDF)

5) Watch recommended anime.