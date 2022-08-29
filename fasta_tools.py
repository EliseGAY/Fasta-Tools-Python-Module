""" Modules to play with fasta files """

#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#------------------------#
# Import modules
#------------------------#
import sys
import re

#------------------------#
#------------------------#
# Split fasta
#------------------------#
#------------------------#

def split_fasta(fasta_file, nb_seq):
    """
    Usage
    ------
    Split fasta file in 'n' fasta file with 'x' sequences
    Launch the function with 2 arguments : yourfile.fasta and nb_seq
    Python verion 3.6

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file
    nb_seq : Number of seqeunces required in each fasta file

    command line
    -------------
    Fasta_Tools.subset_fasta(yourfile.fasta, nb_seq)

    output : fasta files numeroted from 1 to 'x' will be created and will contain 'nb_seq' sequence in it
    --------

    Features to fix
    -----------------
    note : if limit we want to split fasta in file with 2 sequences
    round 1 = fasta file "1" with 2 sequence
    round 2 = compteur = 0 but the third seq is already written in the fasta file "2"
    So "compteur" variable will be = 1 then = 2 and 2 sequences will be written in addition.
    the total number of sequences in the file "2" in the round 2 will be = 3
    """
    #----------------------------#
    # read and initiate variable
    #----------------------------#

    fasta_file = open(fasta_file, "r")
    filin = open("1", "w")
    compteur = 0
    nom = 1
    nb_seq=int(nb_seq)

    #----------------------------#
    # Split fasta file
    #----------------------------#

    for seq in fasta_file :
        if ">" in seq:
            compteur += 1
        if compteur <= 2:
            filin.write(seq)
        if compteur > 2:
            filin.close()
            nom +=1
            f = str(nom)
            filin = open(f, "w")
            filin.write(seq)
            compteur = 0     
    fasta_file.close()
    filin.close()

#------------------------#
#------------------------#
# Dictionnary
#------------------------#
#------------------------#

def fasta_dict(fasta_file):
    """
    Usage
    ------
    Create dictionnary of Key=sequence_ID and value=Sequences
    Launch the function with 1 argument : yourfile.fasta 
    Python verion 3.6

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file

    command line
    -------------
    Fasta_Tools.fasta_dict(fasta.file)

    output : Dictionnary type variable
    --------
    """
    #----------------------------#
    # read and initiate variable
    #----------------------------#

    dico_fasta = {}
    seq = []
    join_seq = []
    fasta_file = open(fasta_file, "r")

    for ligne in fasta_file:
        ligne = ligne.replace("\n", "")
        if re.search('^>', ligne):
            nom=ligne[-1:]
            seq = []
            seq.append(join_seq)
        else :
            seq.append(ligne)
            join_seq = "".join(seq)
            dico_fasta[nom] = join_seq

    return dico_fasta

#------------------------#
#------------------------#
# Subset seq from ID list
#------------------------#
#------------------------#

def Select_Seq(fasta_file, ID_list):
    """
    Usage
    ------
    Subset fasta file from an ID list of sequence
    Launch the function with 2 arguments : yourfile.fasta , ID_list
    Python verion 3.6

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file
    ID_list : ["ID1", "ID2"] list of string

    command line
    -------------
    Fasta_Tools.Select_Seq(fasta.file, ID_list)

    output : Fasta file written in your directory with subset of sequences
    --------
    """

    #----------------------------#
    # read and initiate variable
    #----------------------------#
    
    # format ID string, remove '\n'
    ID_final=[]
    for ID in ID_list:
        ID_final.append(ID.replace("\n", ""))

    print ("your list Id contains",len(ID_final),"ID")

    # creation fichier fasta avec les id fournis
    fasta = file("subset.fasta", "w")
    # create dict from fasta file
    dico_fasta=fasta_dict(fasta_file)
    for i in ID_final:
        if dico_fasta.has_key(i):
           fasta.write(i)
           fasta.write("\n")
           fasta.write(dico_fasta[i])
           fasta.write("\n")
    fasta.close()

#-------------------------------------#
#-------------------------------------#
# Compute N percent in from fast file
#-------------------------------------#
#-------------------------------------#

def get_N_percent(fasta_file):
    """
    Usage
    ------
    Count number of "N" or "n" character in fast sequence
    Launch the function with 1 argument : yourfile.fasta
    Dependency : fasta_dict(fasta_file) function
    Python verion 3.6

    Arguments
    ---------
    fasta.file : PATH/to_your/fasta.file
    
    command line
    -------------
    Fasta_Tools.get_N_percent(fasta.file)

    output : ID percent_N in standard output
    --------
    """

    #----------------------------#
    # read and initiate variable
    #----------------------------#
    
    # create dictionary of all seqeunce with their ID
    dict_seq=fasta_dict(fasta_file)
    
    #----------------------------#
    # Compute N count and percent
    #----------------------------#
    
    for id in dict_seq.keys():
        N_count=int(dict[id].upper().count("N"))
        Seq_len=float(length(dict[id]))
        Percent=float(N_count)/float(Seq_len)*100
        print(id," ",Percent,"\n")
