# Why won't you use AI?
**Date:** 09-09-2026

**Keywords:** Artificial Intelligence, Philosophy, Ethics, Writing


## Tokenization
Today's video: [MIT Sloan's Rama Ramakrishnan Shares Primer on ChatGPT](https://www.youtube.com/watch?v=4fThhooNvA0) explored how ChatGPT works.

Essentially, the family of Artificial Intelligence known as 'GPT' was built to predict the next word in a sentence in a probabilistic model.
In the video, the example of:

> the cat sat on the [blank]

was used to outline the following table:

|next word|probability (by frequency)|
|---------|--------------------------|
| aardvark| 0.0                      |
| fridge  | 0.05                     |
| ...     |                          |
| mat     | 0.2                      |
| ...     |                          |
| table   | 0.03                     |
| zebra   | 0.0                      |

What this table is essentially shows is the likelihood of a word being chosen based on the previous input
such that **one response is not the same as the other**. This makes interacting with the bot seem more nuanced
in its own responses, making it seem like there is a person on the other end of the line.

### Autocompletion
Something that sets GPT-3 apart from the previous models was that it is able to generate coherent text from very little input.
Meaning that from a small bit of information, GPT can expand to what seems like a naturally-sounding text based on pieces of 
information by recursively building on the text through the table that was outlined above.

### Reward Modelling
On good results, ChatGPT starting at 3.5 and beyond will give itself a pat on the back and reinforce good behavior by readjusting
the weights in their probability models.

### Feedback Loop

Below is a ASCII diagram of how GPT's feedback loop works:
```
Enter question ----------------> Generate probability table
 ^                                                       |
 |                                                       v
Append word to question <--------- Sample a word from table

```

This is what happens every time someone uses GPT to generate something.

# My Thoughts

## Finch's Three Rules on AI usage.

I have 3 rules when it comes to using AI:
1. Don't leave things up to chance.
2. Always do it yourself if you know you can do it better.
3. If it breaks your principles, don't use it.
4. If any of these rules are broken, don't use it.

> The gods gave you two hands, and you use them both to slam nonsense on your keyboard. I can respect that.

This is a parodied quote from one of my favorite games: [Skyrim](https://en.uesp.net/wiki/Skyrim:Guard_Dialogue#Reactions_to_Player.27s_Skill_Level)
Although Dr. Thiruvathukal demonstrated some really cool uses of AI; There are numerous reasons as to why I myself refuse to use AI in my coursework
and in my personal works. One of them being that **I don't like leaving things up to chance**. If I know a solution, it is better I write it out. 
If I don't know a solution, then it is up to me to learn how to piece things together. 

The second reason I abstain from using AI is very simple: I feel like I am not learning from it. [Handwriting](../week1/01-zettelkasten.md#Importance-of-handwriting)--
or I suppose typing in this case-- builds muscle memory that allows me to better memorize topics. When it comes to programming (where I began to use AI), I realized
that the information I was receiving from AI tools was not retaining as well in comparison to actually handwriting the code myself. In my novice days of programming, 
I wouldn't be able to explain the underlying systems; why they were built that way; or even begin to organize my codebases such that maintenance was for me to go back
and fix certain bugs or issues that arose during development. Now in all of my projects, I can detail you exactly where something goes wrong; What is happening with 
the computer's memory at specific instances; and most importantly debug any issues without much time thinking about "*Ok, what exactly did my agent do?*". A good engineer 
knows how and where exactly problems occur-- but not exactly *why*, which is the whole reason testing and debugging is such a big part of our job.

Beyond that, [in another writing](../week0/00-writing.md), I mention how AI crosses into numerous political and ethical boundaries that I won't cross.

ChatGPT, like many other Silicon Valley tech companies, is a part of Peter Thiel's and Curtis Yarvin's larger network of companies that they are 
actively using to erode democracy, freedom, and the working class in the United States. The use of AI is actively harming society, and I won't ever
consider myself to be a part of that, even if other people are. Greater societal change begins with the act of an individual within said society; 
If that means that I abstain on what essentially was the coveted goal of Computer Scientists since Turing, then that is what I must do.

Even if we consider local-hosting alternatives (which I have even done myself for testing...), it still breaks rule 1 I have in regards to AI usage should I be using
it for work purposes (i.e. writing a program, schoolwork, etc.)

I will admit, I am guilty of using the AI search results occasionally-- but I do opt for actually doing research into something myself because more often than not,
I find more useful information from the sources than I do from a synthesized output.

# Sources
MIT Sloan, Teaching & Learning Technologies. MIT Sloan’s Rama Ramakrishnan Shares Primer on ChatGPT. 2023. 18:51. https://www.youtube.com/watch?v=4fThhooNvA0.
