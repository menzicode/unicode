### Summer of Code unicode application

- File image_gen.py handles the creation of the dataset from font files.
- File train.py creates embeddings of each image in dataset
- File Vector Query handles retreiving vectors by similarity

Example usage in terminal:  

```
>python3 vector_query.py
Enter a codepoint (4 characters) or type 'q': 0042

Query codepoint: 0042
Labels of nearest neighbors: ['0042', '0392', '0412', '0042', '0412', '0182', '0243', '0234']

```

Here the user queried codepoint 0042 (Latin 'B') and received the 10 closest matches.  
These matches were Latin 'B' of another font, Greek letter beta, Cyrillic letter 'VE', Latin B again,
Cyrillic VE again, Latin capital B with topbar, Cyrillic capital 'BE',  and Latin capital B with stroke.  

These all look quite similar or are the same as the query character so the system seems to be doing 
an alright job with transfer learning. It seems like the project idea has been validated.
