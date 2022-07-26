# Copied HTLM table to Markdown table

This is a mini-script that I made to convert a table in plain text, copied from HTLM, which most of the time just has line breaks in place of all borders, to a markdown-compatible table.

## Usage

I made this for myself, to help me parse some files one day, but if you want to use it:
 - The script expects a path to a text file containing only the copied table, and the number of columns, in that order
 - For example, to reproduce the below example, assuming file.txt contains only the first part of the example, you would have to run:
 `python txt_to_table.py file.txt 3`


## Example:
From this:

```
Header 1

Header 2

Header 3

Cell 11

Cell 12

Cell 13

Cell 21

Cell 22

Cell 23
```

To this:

```md
|Header 1|Header 2|Header 3|
|---|---|---|
|Cell 11|Cell 12|Cell 13|
|Cell 21|Cell 22|Cell 23|
```