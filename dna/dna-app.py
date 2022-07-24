import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#####################
# Page Title
#####################

image = Image.open('dna-logoo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!
\nDesigned by Melu Natam

***
""")



#######################
# Input Text Box
#######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequemce_input = ">DNA Query\nGAACACGTGG"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height = 350)
sequence = st.text_area('Sequence input', sequemce_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence
sequence = ''.join(sequence)

st.write("""
# ***
""")
# Prints the input DNA query
st.header("INPUT (DNA QUERY)")
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# Print Dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
	d = dict([
		('A',seq.count('A')),
		('T',seq.count('T')),
		('G',seq.count('G')),
		('C',seq.count('C'))
		])
	return d

X = DNA_nucleotide_count(sequence)
X

## 2. Print text
st.subheader('2. Print Text')
st.write('There are '+str(X['A'])+ ' adenine (A)')
st.write('There are '+str(X['T'])+ ' thymine (T)')
st.write('There are '+str(X['G'])+ ' guanine (G)')
st.write('There are '+str(X['C'])+ ' cytosine (C)')

## 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

## 4. Display Bar chart
st.subheader('4. Display Barchart')
p = alt.Chart(df).mark_bar().encode(
	x='nucleotide',
	y='count'
)
p = p.properties(
	width=alt.Step(80) # Controls the width of bar Natam
)
st.write(p)
