from Bio.Seq import translate

def translate_dna(dna, ncbi):
    """
    Return protein sequence using given DNA sequence and NCBI table code
    """
    return translate(dna, stop_symbol="", table=ncbi)


def translate_index(dna, protein):
    """
    Returns NCBI table code that corresponds to protein sequence
    """
    for i in ncbi_list:
        if translate_dna(dna, i) == protein:
            return i


if __name__ == '__main__':

    # List of all possible NCBI table codes
    ncbi_list = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

    # Extract info from file:
    with open('files/rosalind_ptra.txt', 'r') as fi:
        dna = fi.readlines()[0].strip()
        protein = 'LGHSAPRLRSWGVDRYFKIGGAVDGLKHSRTRAWLAPKCATREFCPRESIWDAHLARESEPQPKTRCRSRYTPHLRGAPANQGNRKSKGRHSVYLWGALVCGNVQGATVPCSTIVALLRNPRSVNDFIAIVVNRPRRLDYFIVNRHRHGVLPPYRSLIHGTGSNQECPTAMLPLLAASIAGFVAAPRGMRADLMTVWLGLLSEIVPIEARVNRKCVLRRRGDLKSLVESRGHGSVSSERSNYRRRRANLCRRLSARTTPRWLRKQSYSRHVIPPCHTHRYEVHGHSAEPVHPCHAADSPKIVRFEEPSSIYGLLPSPKHSSDDTTPFEHTLCPPLVRQARHGEGGRGTKFPRRPLHGISPSITYVEPALLNWRAPAQVESPHFRQLTYPNLCSYNPGNDVFNYQTTIRESCVFAAYANDTDPTACCRGVRNPAGDACHGNFPPSITGVVTHAVFKAHVHYNCPLFLGGSARLPILSECTITDMTLFTCVKAVDGDCMLKQPLRITIIMILLRCMTEYLLEHHQGSECRRAGRTEASQCGLHTRSFRQVTPHLMELQTLLYCASEYTVNTCPLCFSRLEVKKLCRSRRTVSLPPQKMPPDTEVDMLEKSSVHSSIRSSPELNPVHDNGFATEAYGFALNINPMSLILEKSPIAAIEWVLIYTMVAFFSSSQSSGVLGRALSTSGLYSGILTWVTESVLPWARRNVLKYVLFADRGVFKNRVPIWPSVSLLRQTRSEPKNLTETFLLSTVAGGESSVVLPRLLCGRNVRRPYNKLKLLPVGRRIQNYSREGPHGSRKKALVSLSVNVAVQSANSQRSRMDLKLYSSVHLSLDRLERRPSISIIEEMEAAVTHILELSVQVSYKYASDVWITTMLVCASQTFRSSPCSVAPTASRDALQPLAGFTARRTNPSSRPAVIERGAHDLDGPEYKRSSNSVLYTITVTSLRALTPNYDARIGGVSDARKRGLIIMPLAYHGEYVSGTANQFPTVPVNFVGAVSGASNRSNPKRYYHICPLKLSRESKAIKDKCSTFGHVISDADGRISVCHDINQGVLPRRKTLTPLDQYAQVRAEPRHKYPATGCPYRGFFKRFRLKNSTALVVHPDPNSRRHLAVGIYEVRAFSGRVTDLLVNRTDNDMHRAILVRLGCMLPPFKGDGEGKYLASALGLPQGWTVLLPPNGATPLCAAAYDSTCICQCIGSETLNGLSPYRVNIACVYASTTLNSRAIGLQPDSRPAFVSRICTGWTTSPPAPGRDVASTHRFVRINGQYRPAFHSSRCTLDETRRNVKTDGRTMVALGQLVLSQQYNKGLQQAYPRPLAIVTSEQTTVNSSFSRRSVVSGLRTWITASQANDSRFSVHSEGGRVFNIVNNGDSTRYVGRLPIDALIARTYRRICHFRSRISKGPNLDLPTAARSILVVPIRSSRIGSFRVTIWVNSRRGELPSSTASNIMNVLGGRWEIRHGTLSNYATKRIPLIPVGGIALDLTSRIIRLRATIISYRSRTANPVVWVLGAPRRRPTVPILTAELSLRNASCAFYVETKLAERNRHDAARPGKTLHMRWVVEDVPMNLCGLLFVTFVLICEVGYGMGMVGSEDLSDARLDRAGLELTIDESPIPQWMVQLSHLPLRRCWGWIPAAICVHRLRRSCRHPTPSPFRRTHSALGTFIARCSHWSVPHLMTVANKLVRIRYSLPVTNFAPGLSSKSQAARTLAGPTFDPRHPQPQLFVLYWLHLRILIRVRRIQSRIGRESAYRAESYHRRPTISYIGVNSLNHCRFPPPLVLRGGHTIVEGHTGTEATSKYLITIAESTTGECLNTTSYCVRPLISIMFLDNKCTSSRHLVKGSRSTLQTDLTSLPTMDRLNPQVWIASLQEINRLTLKDCPVLAYGLRFDWTIGFLRLHKNVVWTGEEGHLCIEKQHTGCCIFRPLSYLVGVMLSVRRNVSHDIQSRALPMERCLSLAPNRYTVPGQVRAGSLLYAKKCRYRFSNRTNSMRLDTISCNTPAIPQVALREATPKSRRNLEGPKSLHESGVRSSGQNQVHWYAQEKNDRMKLNRLSNIAGVRIWIVRSSIYQFESLAQMAVPGLRPRDVVTRTCRLYCSSLHTLEDWSRCRHQQINVACLHRPAFQFILLIEGHKSRDGPNDITQLAEPYSRGCARRGPFCRRKGSPSQPCHRAQTFMKIRPVPSPPGMVTCRIHRRDITLCNCYGRVFRKLSIRHELKSLGCPIRLFVVCFHVPFMISQPPTLASSTVENGSALPELVQEVYIITRYPWTWPPGNLQIRRISAHIYTVQAGFGTYLIYTRLGSCDRASIGIVLSSSNGERLIPIYSWKSLLRECQHSDASSTDAVVLKIMFHAPRFGTCESTGACTLLFACHSFNNLEVGRDRRPLSSTRALHLGSGEMQCTQAIRRPGVKWLHHDTGCPDGRYIDAFTCVKMSDLFNWLPLALPSAGHLLPVPGNNPGLAARNHLDRYVRFRIRLLSAGLALTRSLRASQKGFLHKEDAGNGRSRYRRRFCEPRMGLVSGAEALAKYYVLKLRPSQCGLVTSARLTTKCCHSGFRSKGQSLASVGPAIVTMARAPHASSTTIPCSRAERSPTEHHRDASSLDNTAVIQRGVSAAISLWVKANVSRGHLARLPQVKSPIQRRLSFTPDPTLLVPDNFTSRLRILLEFNPRDIIAQSIDSGRHGYSRCTFLRANSDIILNMGACRSLRSPLSILASCSRNMVSLYEREEETTRHAVCTPLPNGDPPTATIDDGNRLASYERLVCLCLRAHLYFLAYTTLPTHVQATGSRLMSTASTGPPPAAQQQGPNLRLVSGRGKMERVASSIQKQRQSARRHGVMFFMIAVTSCHYQAREDMPRLSRGHALLCVRMLCRKSCISVVVRIWVRFRGDKLASRRIEPPRNVAEYPIATDLATAFWWLFVAKRRTMLRADGQPPVPQVPLSWSLVGGKWYEPGFATDFLCPVYSVREIEGCSLQGLTHPIDERQEQHTRTEFRNDKVLGGSGEYSSAALVCLEFTRRNRSHSCPHVFEGASPEPLGKSPIVFGLGCSFGLRVVPGVGIMVRAPVKSWMGSCWGPFLHYGRKYKNLTLGCKWYLRVTSEGRPHMCSHLMDSLRGVLLRRTTGDCAPITPGRRCLVITHCYVDILHPRLCSGFMYRLVYLKAPSGRSRGFVPSAYIRMVNGHRFKCFKLETLTGPGRMQN'

    # Run the process 
    print(translate_index(dna, protein))
