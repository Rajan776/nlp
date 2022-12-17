from wordcloud import WordCloud
import matplotlib.pyplot as plt
text="A dream does not become reality through magic; it takes sweat, determination, and hard work." "I'm a great believer in luck, and I find the harder I work, the more I have of it." "Doing the best at this moment puts you in the best place for the next moment." "Hard work beats talent if talent doesn't work hard"
wordcloud=WordCloud().generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
