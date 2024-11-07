import music21

def main():
    score = music21.converter.parse("example_scores/fearless.xml")
    for x in score.flatten().notes:
        print(x.duration.fullName, [p.name for p in x.pitches])

if __name__=="__main__":
    main()