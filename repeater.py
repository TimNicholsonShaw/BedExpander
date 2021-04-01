test_bed = "chr1	11756	11830	K00180:839:H73VLBBXY:8:2105:23348:42056	0	-"


def expandToList(bed_line): # makes a new list with all the bed lines
    out = []

    bed_line = bed_line.split("\t")
    chr, start, stop = bed_line[:3]
    start = int(start)
    stop = int(stop)

    the_rest = ("\t").join(bed_line[3:])

    while start != stop:
        out.append(
            ("\t").join(
                [chr, str(start), str(start+1), the_rest]
            )
        )

        start+=1


    return out

