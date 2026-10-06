# Text Analysis

A beginner-friendly Python project that analyzes a given text and calculates the **number of words, characters, vowels, and repeated words**. It practices basic text processing techniques used in natural language processing (NLP).

## Objective

Practice basic text processing techniques that are useful in natural language processing.

## Tools Used

- Python 3
- Jupyter Notebook
- Streamlit (for the live demo)

## Dataset

A sample paragraph (42 words):

> Python is a popular language for data analysis. Python is easy to learn, and data analysis with Python is fun. Many students learn Python because Python is simple and powerful. Data helps us make better decisions, and good decisions need good data.

## Approach

1. **Store the text** in a variable.
2. **Count words** by splitting the text with `split()` and counting the pieces with `len()`.
3. **Count characters** with `len(text)`. Characters without spaces are counted after removing the spaces.
4. **Count vowels** by looping through the lowercase text and counting the letters `a, e, i, o, u`.
5. **Preprocess the text** before finding repeated words: convert to lowercase and remove punctuation, so "Python." and "python" count as the same word.
6. **Count word frequency** using `Counter` from the `collections` module.
7. **Find repeated words**: keep only the words that appear more than once.

## What is Text Preprocessing?

Text preprocessing means cleaning raw text before analyzing it. In this project it includes converting to lowercase, removing punctuation, and splitting the text into words. Without it, "Data" and "data." would be counted as different words.

## How to Run

1. Install Python and Jupyter Notebook:
   ```
   pip install notebook
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   python -m notebook
   ```
4. Open `text_analysis.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Sample Output

```
Total words: 42
Total characters (with spaces): 248
Total characters (without spaces): 207
Total vowels: 76
Repeated words:
  python: 5
  data: 4
  is: 4
  and: 3
  analysis: 2
  decisions: 2
  good: 2
  learn: 2
```

## Limitations

- Common words such as "is" and "and" (stop words) are counted as repeated words. They are not removed.
- Only the vowels a, e, i, o, u are counted.
- Words like "don't" lose their apostrophe during punctuation removal.

## Possible Improvements

- Remove stop words to find more meaningful repeated words.
- Accept text from the user or read it from a file.
- Show the most common words as a bar chart.

## Author

SwethaPulusu
