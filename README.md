# Cazy Batch Search
A way to batch search the Carbohydrate-Active enZYmes Database GenBank accession, using Python.

CAZy website is here: http://www.cazy.org

So, you will need a file named `enzylist.csv`, in the same folder, for this to work.
This list should contain the desired Enzymes Access Code. Here take this:

    BAI68730
    BAH05588
    ACV62532
    EAL90874
    ABG47447
    ACT04224

Then you can run this script by simply typing:

    python cazybs.py

If things works, you should get the Glycosil Hydrolase family as the output below
on console:

    EnzymeCode     ; GHFamily
    BAI68730       ; GH57
    BAH05588       ; GH94
    ACV62532       ; GH94
    EAL90874       ; GH13
    ABG47447       ; GH18
    ACT04224       ; GH51

And also a file `enzytable.csv` with a copy of the above output.

Author: Érico Vieira Porto
