class DNASequence:
    def __init__(self, identifier, data):
        self.identifier = identifier
        self.data = data
        self.valid_chars = ['A', 'T', 'C', 'G']

    def __len__(self): #lenght of self.data
        return len(self.data)

    def __str__(self): # FASTA format style
        return (f">{self.identifier}\n{self.data}")

    def mutate(self,position,value):
        # in my case it's gonna be a substitution mutation type
        self.data[position] = value

    def find_motif(self, motif): #doesn't work quite well
        start = 0
        positions_list = []
        while start < len(self.data):
            position = self.data.find(motif, start)
            if position == -1:
                break
            positions_list.append(position)
            start = position + 1
        return positions_list

    def complement(self):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement = ""
        for i, value in enumerate(self.data):
            complement += complement_dict[self.data[i]]
        return complement

    def transcribe(self):
        data_rna = self.data.replace('T', 'U')
        return RNASequence(self.identifier, data_rna)


newDNA = DNASequence(1,"ATGGGATAA")
print(newDNA)
print(newDNA.find_motif("TAA"))
print(newDNA.complement())

class RNASequence:
    def __init__(self, identifier, data):
        self.identifier = identifier
        self.data = data
        self.valid_chars = ['A', 'U', 'C', 'G']

    def __len__(self): #lenght of self.data
        return len(self.data)

    def __str__(self): # FASTA format style
        return (f">{self.identifier}\n{self.data}")

    def mutate(self,position,value):
        # in my case it's gonna be a substitution mutation type
        self.data[position] = value

    def find_motif(self, motif): #doesn't work quite well
        start = 0
        positions_list = []
        while start < len(self.data):
            position = self.data.find(motif, start)
            if position == -1:
                break
            positions_list.append(position)
            start = position + 1
        return positions_list

    def complement(self):
        complement_dict = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        complement = ""
        for i, value in enumerate(self.data):
            complement += complement_dict[self.data[i]]
        return complement

    def transcribe(self):
        data_rna = self.data.replace('T', 'U')
        return RNASequence(self.identifier, data_rna)