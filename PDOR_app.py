import streamlit as st


### Page visualization
st.set_page_config(page_title="PDOR",layout='wide')

logo = "https://raw.githubusercontent.com/SteMIDIfactory/P-DOR/master/p-dor_logo.png"
col1, col2, col3 = st.columns(3)
col1.image(logo, width=150)
st.markdown("<h1 style='text-align: center; color: black;'>P-DOR: a Pipeline to Disentangling Outbreak Rapidly</h1>", unsafe_allow_html=True)


st.subheader("What is P-DOR?")
st.write("P-DOR is a bioinformatic pipeline for rapid WGS-based bacterial outbreak detection and characterization, carried on by integratic clinical metadata and contextualizing the genomes of interest within a well curated global genomic database.")

st.expander("Pipeline description")
with st.expander("Pipeline description"):
    st.write("""
        1) The P-DOR framework keeps an updated database of all ESKAPE genomes from the [PATRIC](https://www.patricbrc.org/) collection. Input genomes are joined with a background of the n most similar ones from the database. The selection is performed according to the k-mer distance via Mash.
2) Each genome of the resulting dataset is aligned to a reference genome and the coreSNPs are called. Core-SNPs are defined as single-nucleotide mutated positions flanked by n identical bases in all of the analyzed genomes. Two modes are available:
3) A Maximum Likelihood phylogeny is inferred using [RAxML](https://cme.h-its.org/exelixis/web/software/raxml/) software.
4) Epidemiological clusters are assessed on the basis of coreSNPs distances using a threshold value to hypothesize the epidemiological relationship among the strains. This parameter can be set manually (e.g. according to previous studies) or computed by detecting the inflection point in the distribution of the coreSNP distances between all pairs of genomes.
5) A screening for resistance and virulence determinants is also performed through [Abricate](https://github.com/tseemann/abricate).
6) If patient metadata (i.e. ward of hospitalization, date of admission and discharge) are provived, the pipeline reconstruct the route of transmission  through a temporal and spatial representation of the outbreak.
    """)
with st.expander("Output description"):
    st.write("""
1) Summary of resistance and virulence detected.
2) Core-SNPs alignment
3) Core‐SNPs histogram distribution between genome pairs. The dashed bar is set according to the threshold indicating the epidemiological clusters.
4) Heatmap and graph network representing the core-SNPs distances between all pairs of genomes.
5) Maximum Likelihood SNP-based phylogeny with annotated tips according to presence-absence of the genetic determinants of resistance and virulence.   Labels are colored based on the outbreak clusters.
6) Timeline of hospitalized patient and the bacterial samples. The timeline indicates samples isolation based on colonization and infection. The samples are linked according the their core-SNPs distance.""")


st.header("Run P-DOR")
st.subheader('Upload genomes:')
uploaded_files = st.file_uploader("", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()

st.sidebar.write("P-DOR is a bioinformatic pipeline for rapid WGS-based bacterial outbreak detection and characterization, carried on by integratic clinical metadata and contextualizing the genomes of interest within a well curated global genomic database.")
